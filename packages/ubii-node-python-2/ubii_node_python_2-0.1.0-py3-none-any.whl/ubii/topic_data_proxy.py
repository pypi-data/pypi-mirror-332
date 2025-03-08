from typing import Callable

from proto.topicData.topicDataRecord_pb2 import TopicDataRecord

from typing import List

from ubii.topic_data_buffer import TopicDataBuffer, SubscriptionToken, SubscriptionTokenType
from ubii.ubii_network_client import UbiiNetworkClient


class TopicDataProxy:
    
    LOG_TAG = "[ubii TopicDataProxy]"
    #logic and proxy design is taken from the ubii-node-unity3D https://github.com/SandroWeber/ubii-node-unity3D
    def __init__(self, topicDataBuffer: TopicDataBuffer, networkClient: UbiiNetworkClient, node):
        self.topicDataBuffer: TopicDataBuffer = topicDataBuffer
        self.networkClient = networkClient
        self.node = node

    async def subscribe_topic(self, topic: str, callback: Callable[[TopicDataRecord], None], asyncio_loop = None) -> SubscriptionToken:
        subscriptions = self.get_topic_subscription_tokens(topic)
        if subscriptions is None or not subscriptions:
            success = await self.networkClient.subscribeTopic(topic, self.on_topicdatarecord)
            if success == True:
                return self.topicDataBuffer.subscribeTopic(topic, callback)

        return None

    async def subscribe_regex(self, regex: str, callback: Callable[[TopicDataRecord], None], asyncio_loop = None) -> SubscriptionToken:
        subscriptions = self.get_regex_subscription_tokens(regex)
        if subscriptions is None or not subscriptions:
            self.networkClient.subscribeRegex(regex, self.on_topicdatarecord)

        return self.topicDataBuffer.subscribeRegex(regex, callback, asyncio_loop)

    def unsubscribe(self, token: SubscriptionToken) -> bool:
        bufferUnsubscribe = self.topicDataBuffer.unsubscribe(token)
        if bufferUnsubscribe:
            if token.type == SubscriptionTokenType.TOPIC:
                subList = self.get_topic_subscription_tokens(token.topic)
                if (subList is None) or (not subList):
                    self.networkClient.unsubscribe(token.topic, self.on_topicdatarecord)

            elif token.type == SubscriptionTokenType.REGEX:
                subList = self.get_regex_subscription_tokens(token.topic)
                if (subList is None) or (not subList):
                    self.networkClient.unsubscribeRegex(token.topic, self.on_topicdatarecord)

            return True

        return False

    def remove(self, topic: str):
        self.topicDataBuffer.remove(topic)

    def pull(self, topic: str) -> TopicDataRecord:
        return self.topicDataBuffer.pull(topic)

    def get_topic_subscription_tokens(self, topic: str) -> List[SubscriptionToken]:
        return self.topicDataBuffer.getTopicSubscriptionTokens(topic)

    def get_regex_subscription_tokens(self, regex: str) -> List[SubscriptionToken]:
        return self.topicDataBuffer.getRegexSubscriptionTokens(regex)

    def on_topicdatarecord(self, record: TopicDataRecord):
        self.topicDataBuffer.publish(record)

    def set_publish_frequency(self, frequency):
        self.networkClient.setPublishFrequency(frequency)

    def stop_node(self):
        self.networkClient.stopNode()
