import asyncio
import concurrent
from concurrent import futures
from threading import Thread, Event
from typing import Callable

from proto.clients.client_pb2 import Client
from proto.services.serviceRequest_pb2 import ServiceRequest
from proto.topicData.topicDataRecord_pb2 import TopicDataRecord, TopicDataRecordList
from ubii.ubii_network_client import UbiiNetworkClient
from events import Events

from ubii.topic_data_buffer import TopicDataBuffer, SubscriptionToken
from ubii.topic_data_proxy import TopicDataProxy

#project structure was adapted from the ubii-node-unity3D https://github.com/SandroWeber/ubii-node-unity3D
class UbiiClientNode:
    
    LOG_TAG = '[ubii node]'
    
    """
    This class represents the python client node v.2 https://github.com/SandroWeber/ubii-node-python-v2 for the UBI-Interact framework https://github.com/SandroWeber/ubi-interact/wiki.

    :ivar events: Four Events ('onPublishError', 'onReadError', 'onServiceCallError', 'onConnectionError') for error handling, each event can be subscribed to with a callback that takes exactly one Exception as parameter. Whenever an Error occurs the associated events gets called.

        "Events"::

            def handleExc(e):
                print(e)

            node = UbiiClientNode()
            node.events.onConnectionError += handleExc

    """
    
    #TODO: hook callbacks to current event loop if no specific event loop is passed
    def __init__(self, name='pythonNodeV2', service_endpoint='http://localhost:8102/services/binary',
                 topicdata_endpoint='ws://localhost:8104', separateEventLoop=None):
        """
        Constructor for the UbiiClientNode

        After initialising the attributes a thread is started that handles the initialisation with the masternode asynchronous:
        :param name: The name of the node
        :type name: str, optional
        :param service_endpoint: The endpoint to connect to the masternode for the binary service calls.
        :type service_endpoint: str, optional
        :param topicdata_endpoint: The endpoint to connect to the masternode for the websocket topicdata connection
        :type topicdata_endpoint: str, optional
        """
        self.name = name
        self.serviceEndpoint = service_endpoint
        self.topicDataEndpoint = topicdata_endpoint
        
        self.eventLoop = None
        if separateEventLoop != None:
            self.eventLoop = separateEventLoop
        else:
            try:
                self.eventLoop = asyncio.get_event_loop()
            except Exception:
                self.eventLoop = asyncio.new_event_loop()
        #print(self.LOG_TAG, "event loop: ", self.eventLoop)
        
        self.connected = Event()
        self.events = Events(('onPublishError', 'onReadError', 'onServiceCallError', 'onConnectionError'))
        self.IS_DEDICATED_PROCESSING_NODE = False
        self.clientSpecification = Client()
        self.topicDataBuffer = TopicDataBuffer()
        self.networkClient = UbiiNetworkClient(self.serviceEndpoint, self.topicDataEndpoint, self.clientSpecification,
                                               self)
        self.topicDataProxy = TopicDataProxy(self.topicDataBuffer, self.networkClient, self)
        t1 = Thread(target=self.init, args=[])
        t1.daemon = True
        t1.start()

    def init(self):
        self.init_client_specs()
        asyncio.run(self.init_network())
        self.connected.set()

    def init_client_specs(self):
        self.clientSpecification.name = self.name
        self.clientSpecification.is_dedicated_processing_node = self.IS_DEDICATED_PROCESSING_NODE

    async def init_network(self):
        print(self.LOG_TAG, 'connecting to service=' + self.serviceEndpoint + ', topicdata=' + self.topicDataEndpoint)
        await self.networkClient.init()
        self.clientSpecification = self.networkClient.clientSpecification
        self.topicDataProxy = TopicDataProxy(self.topicDataBuffer, self.networkClient, self)
        
    def get_callback_event_loop(self):
        return self.eventLoop

    def call_service(self, request: ServiceRequest) -> concurrent.futures.Future:
        """
        Makes a service request to the masternode.

        This happens asynchronous but returns a future with the ServiceReply from the masternode once finished or None if the process raised an exception.

        :param request: The ServiceRequest sent to the masternode.
        :type request: ServiceRequest
        :return: The Future with the ServiceReply or with None.
        :rtype: Future
        """

        return self.networkClient.callService(request)


    def publish(self, record: TopicDataRecord):
        """
        Publishes the topicDataRecord in the next interval.

        Ads the TopicDataRecord to a list of TopicDataRecords that will be sent to the masternode in the next publish interval.
        If the list already contains a TopicDataRecord with the specified topic the TopicDataRecord in the list will be overwritten with this one.
        The process of sending the TopicDataRecord to the masternode happens asynchronous in a different thread.

        :param record: The TopicDataRecord to publish.
        :type record: TopicDataRecord
        """
        self.networkClient.publish(record)

    def publish_list(self, recordList: TopicDataRecordList):
        """
        Publishes the elements of the TopicDataRecordList in the next interval.

        Ads every TopicDataRecord from the TopicDataRecordList to a list of TopicDataRecords that will be sent to the masternode in the next publish interval.
        If the list already contains a TopicDataRecord with the specified topic the TopicDataRecord in the list will be overwritten with this one.
        The process of sending the TopicDataRecords to the masternode happens asynchronous in a different thread.

        :param recordList: The TopicDataRecordList with the topics to publish
        :type recordList: TopicDataRecordList
        """

        if not recordList is None and recordList.elements:
            for record in recordList.elements:
                self.publish(record)

    def publish_immediately(self, data: TopicDataRecord):
        """
        Publishes the topicDataRecord instantly.

        Sends the TopicDataRecord directly to the masternode.
        The process of sending the topic to the masternode happens asynchronous in a different thread.

        :param data: The TopicDataRecord to publish.
        :type data: TopicDataRecord
        """
        self.networkClient.publish_immediately(data)

    async def subscribe_topic(self, topic: str, callback: Callable[[TopicDataRecord], None], asyncio_loop = None) -> SubscriptionToken:
        """
        Subscribes to a topic.

        Whenever a topicDataRecord is published at the masternode for this topic, that topicData will be sent to this nodeand the callback passed is invoked for this topicDataRecord.
        The process to subscribe at the masternode happens asynchronous in a different thread.

        :param topic: The topic that should be subscribed to
        :type topic: str
        :param callback: The callback that takes exactly one TopicDataRecord as parameter and returns nothing
        :return: The SubscriptionToken that contains a unique token id, the regex, the callback, and the SubscriptionTokenType.
        :rtype: SubscriptionToken
        """
        return await self.topicDataProxy.subscribe_topic(topic, callback, asyncio_loop)
    
    def subscribe_topic_sync(self, topic: str, callback: Callable[[TopicDataRecord], None], asyncio_loop = None) -> SubscriptionToken:
        """
        Subscribes to a topic.

        Whenever a topicDataRecord is published at the masternode for this topic, that topicData will be sent to this nodeand the callback passed is invoked for this topicDataRecord.
        The process to subscribe at the masternode happens asynchronous in a different thread.

        :param topic: The topic that should be subscribed to
        :type topic: str
        :param callback: The callback that takes exactly one TopicDataRecord as parameter and returns nothing
        :return: The SubscriptionToken that contains a unique token id, the regex, the callback, and the SubscriptionTokenType.
        :rtype: SubscriptionToken
        """
        return self.eventLoop.run_until_complete(self.topicDataProxy.subscribe_topic(topic, callback, asyncio_loop))

    def subscribe_regex(self, regex: str, callback: Callable[[TopicDataRecord], None], asyncio_loop = None) -> SubscriptionToken:
        """
        Subscribes to a regular expression.

        Whenever a topicDataRecord is published at the masternode for a topic that fits this regular expression that topicDataRecord will be sent to this node and the callback passed is invoked for this topicDataRecord.
        The process to subscribe at the masternode happens asynchronous in a different thread.

        :param regex: The regular expression that should be subscribed to.
        :type regex: str
        :param callback: The callback that takes exactly one TopicDataRecord as parameter and returns nothing.
        :type callback: Callable[[TopicDataRecord], None]
        :return: The SubscriptionToken that contains a unique token id, the regex, the callback, and the SubscriptionTokenType.
        :rtype: SubscriptionToken
        """
        return self.topicDataProxy.subscribe_regex(regex, callback, asyncio_loop)

    def unsubscribe(self, token: SubscriptionToken) -> bool:
        """
        Unsubscribes the subscription token.

        The callback that was passed when subscribing is no longer executed when a topicDataRecord is received for this topic.
        When there are no more subscribers for a topic at this node, the node unsubscribes at the masternode and won't receive any published topicData.
        The callback will be unsubscribed synchronous, but the process to unsubscribe at the masternode happens asynchronous in a different thread.

        :param token: The subscriptionToken that was returned when subscribing.
        :type token: SubscriptionToken
        :return: The success of the operation.
        :rtype: bool
        """
        return self.topicDataProxy.unsubscribe(token)

    def set_publish_frequency(self, frequency):
        """
        Changes the frequency the node sends the published topicdata to the masternode.

        :param frequency: the time interval.
        :type frequency: float
        """
        self.topicDataProxy.set_publish_frequency(frequency)

    def stop_node(self):
        """
        Needs to be called when the node is no longer used in any form to disconnect it from the masternode and to stop background threads.
        The disconnection process happens asynchronous in a different thread.
        """
        self.topicDataProxy.stop_node()

    def wait_for_connection(self):
        """
        Pauses the current thread until the node is connected to the masternode.
        """
        if not self.is_connected():
            self.connected.wait()

    def is_connected(self):
        """
        :return: The connection status with the masternode.
        :rtype: bool
        """
        return self.connected.is_set()

    def get_id(self):
        """
        :return: The id the node got from the masternode if connected, None else.
        :rtype: str or None
        """
        if self.is_connected():
            return self.clientSpecification.id
        else:
            return None
        
    def on_topicdata_received(self, record):
        self.eventLoop.call_soon_threadsafe(self.topicDataBuffer.publish, record)
        
    def to_string(self):
        if self.is_connected():
            return 'ubii client node "' + self.clientSpecification.name + '" (ID ' + self.clientSpecification.id + ')'
        else:
            return 'ubii client node "' + self.name + '" (not connected)' 
