import re
from enum import Enum
from typing import Callable
from typing import List

from proto.topicData.topicDataRecord_pb2 import TopicDataRecord


class SubscriptionTokenType(Enum):
    TOPIC = 1
    REGEX = 2


class SubscriptionToken:
    def __init__(self, id: int, topic: str, callback: Callable[[TopicDataRecord], None], type: SubscriptionTokenType, loop = None):
        self.id: int = id
        self.topic: str = topic
        self.callback: Callable[[TopicDataRecord], None] = callback
        self.type: SubscriptionTokenType = type
        self.loop = loop


class TopicDataBuffer:
    # buffer functionality and logic was adapted from the ubii-node-unity3D https://github.com/SandroWeber/ubii-node-unity3D
    def __init__(self):
        self.localTopics: dict[str, TopicDataRecord] = {}
        self.dictTopicSubscriptionTokens: dict[str, List[SubscriptionToken]] = {}
        self.dictRegexSubscriptionTokens: dict[str, List[SubscriptionToken]] = {}
        self.dictTopic2RegexMatches: dict[str, List[str]] = {}
        self.currentTokenId = -1

    def publish(self, topicDataRecord: TopicDataRecord):
        topic = topicDataRecord.topic
        if not topic in self.localTopics:
            if not topic in self.dictTopic2RegexMatches:
                self.dictTopic2RegexMatches[topic] = []
                for regex in self.dictRegexSubscriptionTokens:
                    if re.match(regex, topic):
                        self.dictTopic2RegexMatches[topic].append(regex)

        self.localTopics[topic] = topicDataRecord
        self.notifySubscribers(topicDataRecord)

    def notifySubscribers(self, topicDataRecord):
        topic = topicDataRecord.topic
        if topic in self.dictTopicSubscriptionTokens:
            for token in self.dictTopicSubscriptionTokens[topic]:
                token.callback(topicDataRecord)

        if topic in self.dictTopic2RegexMatches:
            for regex in self.dictTopic2RegexMatches[topic]:
                for token in self.dictRegexSubscriptionTokens[regex]:
                    token.callback(topicDataRecord)

    def subscribeTopic(self, topic: str, callback: Callable[[TopicDataRecord], None], loop = None) -> SubscriptionToken:
        if not topic in self.dictTopicSubscriptionTokens:
            self.dictTopicSubscriptionTokens[topic] = []
        token = self.generateToken(topic, callback, SubscriptionTokenType.TOPIC, loop)
        self.dictTopicSubscriptionTokens[topic].append(token)
        return token

    def subscribeRegex(self, regex: str, callback: Callable[[TopicDataRecord], None], loop = None) -> SubscriptionToken:
        token = self.generateToken(regex, callback, SubscriptionTokenType.REGEX, loop)

        if not regex in self.dictRegexSubscriptionTokens:
            self.dictRegexSubscriptionTokens[regex] = []
        self.dictRegexSubscriptionTokens[regex].append(token)

        for topic in self.localTopics:
            if re.match(regex, topic):
                if not topic in self.dictTopic2RegexMatches:
                    self.dictTopic2RegexMatches[topic] = []
                self.dictTopic2RegexMatches[topic].append(regex)

        return token

    def unsubscribe(self, token: SubscriptionToken) -> bool:
        topic = token.topic
        existingTopic = False
        if topic in self.dictTopicSubscriptionTokens:
            self.dictTopicSubscriptionTokens[topic] = list(
                filter(lambda a: a.id != token.id, self.dictTopicSubscriptionTokens[topic]))
            existingTopic = True

        elif topic in self.dictRegexSubscriptionTokens:
            self.dictRegexSubscriptionTokens[topic] = list(
                filter(lambda a: a.id != token.id, self.dictRegexSubscriptionTokens[topic]))
            for key, value in self.dictTopic2RegexMatches.items():
                value = list(filter(lambda entry: entry != topic, value))
            existingTopic = True
        return existingTopic

    def remove(self, topic: str):
        if topic in self.localTopics:
            del self.localTopics[topic]

    def pull(self, topic: str) -> TopicDataRecord:
        return self.localTopics.get(topic)

    def getTopicSubscriptionTokens(self, topic: str) -> List[SubscriptionToken]:
        return self.dictTopicSubscriptionTokens.get(topic)

    def getRegexSubscriptionTokens(self, regex: str) -> List[SubscriptionToken]:
        return self.dictRegexSubscriptionTokens.get(regex)

    def generateToken(self, topic: str, callback: Callable[[TopicDataRecord], None],
                      type: SubscriptionTokenType, loop) -> SubscriptionToken:
        self.currentTokenId += 1
        return SubscriptionToken(self.currentTokenId, topic, callback, type, loop)
