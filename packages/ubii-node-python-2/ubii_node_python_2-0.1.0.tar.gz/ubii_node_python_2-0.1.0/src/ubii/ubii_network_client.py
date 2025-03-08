import asyncio
import concurrent
import json
from concurrent import futures
from threading import Thread
from typing import Callable
from typing import List
from google.protobuf import text_format

from proto.clients.client_pb2 import Client
from proto.services.request.topicSubscription_pb2 import TopicSubscription
from proto.services.serviceRequest_pb2 import ServiceRequest
from proto.topicData.topicDataRecord_pb2 import TopicDataRecord
from proto.topicData.topicData_pb2 import TopicData

from ubii.ubii_service_client import UbiiServiceClient
from ubii.ubii_topicdata_client import UbiiTopicDataClient


class UbiiNetworkClient:
    
    LOG_TAG = '[UBII NetworkClient]'
    
    #some functionality is adapted from the ubii-node-unity3D https://github.com/SandroWeber/ubii-node-unity3D
    def __init__(self, serviceEndpoint, topicDataEndpoint, clientSpecs, node):
        self.serviceEndpoint = serviceEndpoint
        self.topicDataEndpoint = topicDataEndpoint
        self.serviceClient: UbiiServiceClient = UbiiServiceClient(serviceEndpoint, node)
        self.clientSpecification = clientSpecs
        self.topicDataClient = None
        self.node = node

    async def init(self):
        await self.get_server_config()
        self.clientSpecification = await self.registerAsClient(self.clientSpecification)
        self.topicDataClient = UbiiTopicDataClient(self.topicDataEndpoint, self.clientSpecification.id, self.node)

    def callService(self, request: ServiceRequest) -> concurrent.futures.Future:
        #using a ThreadPoolExecutor to return a future as discussed in here https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
        executor = futures.ThreadPoolExecutor()
        future = executor.submit(self.__callServiceDelegate, request)
        executor.shutdown(wait=False)
        return future

    def __callServiceDelegate(self, request: ServiceRequest):
        self.node.wait_for_connection()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        res = loop.run_until_complete(self.__callServiceDelegateAsync(request))
        loop.close()
        return res

    async def __callServiceDelegateAsync(self, request: ServiceRequest):
        try:
            return await self.serviceClient.send(request)
        except Exception as e:
            self.node.events.onServiceCallError(e)
            print(e)
            return None

    def publish(self, record: TopicDataRecord):
        if self.node.is_connected():
            self.topicDataClient.publish(record)
        else:
            t1 = Thread(target=self.__waitPublishDelegate, args=[record])
            t1.start()

    def __waitPublishDelegate(self, record: TopicDataRecord):
        self.node.wait_for_connection()
        self.topicDataClient.publish(record)

    def publish_immediately(self, record: TopicDataRecord):
        t1 = Thread(target=self.__publishImmediatelyDelegate, args=[record])
        t1.start()

    def __publishImmediatelyDelegate(self, record: TopicDataRecord):
        self.node.wait_for_connection()
        asyncio.run(self.__publishImmediatelyDelegateAsync(record))

    async def __publishImmediatelyDelegateAsync(self, record: TopicDataRecord):
        try:
            topicData = TopicData()
            topicData.topic_data_record.CopyFrom(record)
            await self.topicDataClient.sendTopicData(topicData)
        except Exception as e:
            print(e)
            self.node.events.onPublishError(e)
            
    async def get_server_config(self):
        request = ServiceRequest()
        request.topic = '/services/server_configuration'
        reply = await self.serviceClient.send(request)
        if (reply.HasField('error')):
            print(self.LOG_TAG + ' error:' + text_format.MessageToString(reply.error))
        elif (reply.HasField('server')):
            self.server_config = reply.server
            self.server_constants = json.loads(self.server_config.constants_json)

    async def registerAsClient(self, client: Client) -> Client:
        request = ServiceRequest()
        request.topic = self.server_constants['DEFAULT_TOPICS']['SERVICES']['CLIENT_REGISTRATION'] #'/services/client/registration'
        request.client.CopyFrom(client)
        success = False
        reply = None
        while not success:
            try:
                reply = await self.serviceClient.send(request)
                success = True
            except Exception as e:
                print(e)
                print(self.LOG_TAG, 'Error while registering client trying again in 15 seconds')
                self.node.events.onServiceCallError(e)
                await asyncio.sleep(15)

        if (reply is None) or (reply.HasField("error")):
            print(self.LOG_TAG, "Error at serviceRequest while registering client: ", reply.error)
            return None

        return reply.client

    async def subscribeTopic(self, topic: str, callback: Callable[[TopicDataRecord], None]):
        success = await asyncio.to_thread(self.__subscribeTopicDelegate, topic, callback)
        return success

    def __subscribeTopicDelegate(self, topic: str, callback: Callable[[TopicDataRecord], None]):
        self.node.wait_for_connection()
        if self.topicDataClient.isSubscribed(topic):
            self.topicDataClient.addTopicCallback(topic, callback)
            return

        request = ServiceRequest()
        request.topic = '/services/topic_subscription'
        topicSubscription = TopicSubscription()
        topicSubscription.client_id = self.clientSpecification.id
        topicSubscription.subscribe_topics.append(topic)
        request.topic_subscription.CopyFrom(topicSubscription)
        reply = self.callService(request)

        if (reply is None) or (reply.result().HasField("error")):
            print(self.LOG_TAG, "Error while subscribing: ", reply.error)
            #print('__subscribeTopicDelegate() - success=False')
            return False

        self.topicDataClient.addTopicCallback(topic, callback)
        #print('__subscribeTopicDelegate() - success=True')
        return True

    def subscribeRegex(self, regex: str, callback: Callable[[TopicDataRecord], None]):
        t1 = Thread(target=self.__subscribeRegexDelegate, args=[regex, callback])
        t1.start()

    def __subscribeRegexDelegate(self, regex: str, callback: Callable[[TopicDataRecord], None]):
        self.node.wait_for_connection()
        if self.topicDataClient.isSubscribed(regex):
            self.topicDataClient.addRegexCallback(regex, callback)
            return

        request = ServiceRequest()
        request.topic = '/services/topic_subscription'

        topicSubscription = TopicSubscription()
        topicSubscription.client_id = self.clientSpecification.id
        topicSubscription.subscribe_topic_regexp.append(regex)

        request.topic_subscription.CopyFrom(topicSubscription)
        reply = self.callService(request)

        if reply is None or reply.result().HasField("error"):
            print("Error while subscribing at Master")
            return

        self.topicDataClient.addRegexCallback(regex, callback)

    def unsubscribe(self, topic: str, callback: Callable[[TopicDataRecord], None]):
        t1 = Thread(target=self.__unsubscribeDelegate, args=[topic, callback])
        t1.start()

    def __unsubscribeDelegate(self, topic: str, callback: Callable[[TopicDataRecord], None]):
        self.node.wait_for_connection()
        self.topicDataClient.removeTopicCallback(topic, callback)

        if self.topicDataClient.hasTopicDataCallbacks(topic):
            return

        self.__unsubscribeTopicMaster([topic])

    def __unsubscribeTopicMaster(self, topics: List[str]):
        request = ServiceRequest()
        request.topic = '/services/topic_subscription'
        topicUnsubscription = TopicSubscription()
        topicUnsubscription.client_id = self.clientSpecification.id
        topicUnsubscription.unsubscribe_topics[:] = topics
        request.topic_subscription.CopyFrom(topicUnsubscription)
        reply = self.callService(request)
        if (reply is None) or (reply.result().HasField("error")):
            print("Error while unsubscribing at Master")
            return

        for topic in topics:
            self.topicDataClient.removeTopicDataCallbacks(topic)

    def unsubscribeRegex(self, regex: str, callback: Callable[[TopicDataRecord], None]):
        t1 = Thread(target=self.__unsubscribeRegexDelegate, args=[regex, callback])
        t1.start()

    def __unsubscribeRegexDelegate(self, regex: str, callback: Callable[[TopicDataRecord], None]):
        self.node.wait_for_connection()

        self.topicDataClient.removeRegexCallback(regex, callback)

        if self.topicDataClient.hasRegexCallbacks(regex):
            return

        self.__unsubscribeRegexAtMaster(regex)

    def __unsubscribeRegexAtMaster(self, regex: str):
        request = ServiceRequest()
        request.topic = '/services/topic_subscription'

        topicUnsubscription = TopicSubscription()
        topicUnsubscription.client_id = self.clientSpecification.id
        topicUnsubscription.unsubscribe_topic_regexp.append(regex)

        request.topic_subscription.CopyFrom(topicUnsubscription)
        reply = self.callService(request)

        if (reply is None) or (reply.result().HasField("error")):
            print("Error while unsubscribing at Master")
            return

        self.topicDataClient.removeAllRegexCallbacks(regex)

    def setPublishFrequency(self, frequency):
        if not self.topicDataClient is None:
            self.topicDataClient.setPublishFrequency(frequency)

        print("topicDataClient is not initialized")

    def stopNode(self):
        if self.node.is_connected():
            request = ServiceRequest()
            request.topic = '/services/client/deregistration'
            request.client.CopyFrom(self.clientSpecification)
            self.callService(request)

        if not self.topicDataClient is None:
            self.topicDataClient.stopNode()
