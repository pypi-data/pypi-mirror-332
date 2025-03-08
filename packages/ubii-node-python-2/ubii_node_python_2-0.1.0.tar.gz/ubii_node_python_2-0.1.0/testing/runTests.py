import time
import unittest
import random
import uuid
import asyncio
import threading
import multiprocessing as mp

from proto.clients.client_pb2 import ClientList
from proto.services.serviceRequest_pb2 import ServiceRequest
from proto.topicData.topicDataRecord_pb2 import TopicDataRecord
from ubii.ubii_client_node import UbiiClientNode


def publish_immediately_random_int(node, topic):
    record = TopicDataRecord()
    record.topic = topic
    random_int = random.randint(1,100)
    record.int32 = random_int
    node.publish_immediately(record)
    return random_int

def publish_random_int(node, topic):
    record = TopicDataRecord()
    record.topic = topic
    random_int = random.randint(1,100)
    record.int32 = random_int
    node.publish(record)
    return random_int

def multiprocessing_target(queue, topic_string):
    node = UbiiClientNode("python testing multiprocessing")
    node.wait_for_connection()
    
    random_int = publish_random_int(node, topic_string)
    queue.put(random_int)
    
    time.sleep(1)
    node.stop_node()


        #def process_target(queue):
            #nonlocal topicString
            #print("process_target")

            #node = UbiiClientNode()
            #node.wait_for_connection()

            #loop = asyncio.get_event_loop()
            #print("process_target, loop:", loop)
            #futureTestFinished = loop.create_future()

            #def sub_callback(record):
            #    nonlocal futureTestFinished
            #    print("sub_callback, int32:", record.int32)
            #    queue.put(record.int32)
            #    futureTestFinished.set_result(True)

            #node.subscribe_topic(topicString, sub_callback)
            #random_int = publishRandomInt(self.node, topicString)

'''
class TestUbiiSync(unittest.TestCase):
    def setUp(self):
        self.node = UbiiClientNode("Python Testing - Synchronous")
        self.node.wait_for_connection()

    def tearDown(self):
        self.node.stop_node()
        
    def test_publishSync(self):
        print('start: test_publishSync')
        
        counterRecordsReceived = 0
        targetNumberPublishes = 10
        topicString = str(uuid.uuid4())
        print("topicString:", topicString)
        
        def callback(record):
            print("callback - record:" + record)
            nonlocal counterRecordsReceived
            nonlocal targetNumberPublishes
            nonlocal topicString
            if record.HasField('int32'):
                counterRecordsReceived += 1
                print("callback() - targetNumberPublishes : counterRecordsReceived = " + str(targetNumberPublishes) + ":" + str(counterRecordsReceived))
                if (counterRecordsReceived < targetNumberPublishes):
                    print("publishRandomInt next")
                    publishRandomInt(self.node, topicString)
        
        node2 = UbiiClientNode()
        node2.wait_for_connection()
        token = node2.subscribe_topicSync(topicString, callback)
        print("token ID for callback(): " + str(token.id))
        
        publishRandomInt(self.node, topicString)
        
        timeout = 0
        max_timeout = 5          
        def checkTestFinished():
            nonlocal timeout
            nonlocal max_timeout
            nonlocal counterRecordsReceived
            nonlocal targetNumberPublishes
            print("checkTestFinished() - targetNumberPublishes : counterRecordsReceived = " + str(targetNumberPublishes) + ":" + str(counterRecordsReceived))
            if (targetNumberPublishes == counterRecordsReceived or timeout >= max_timeout):
                return
            else:
                timeout += 0.1
                time.sleep(0.1)
                checkTestFinished()
        t = threading.Thread(target=checkTestFinished, args = ())
        t.start()
        t.join()
        self.assertEqual(targetNumberPublishes, counterRecordsReceived)
        
        node2.stop_node()
        print('end: test_publishSync')
        
    
    def testSubscribeRegex(self):
        print('start: testSubscribeRegex')
        testString = ''
        stringShouldBe = 'abc'
        regex = '[abc]+[123]*[abc]+'

        def callbackTestString(record):
            print("+++++ callbackTestString +++++")
            print(record)
            nonlocal testString
            if record.HasField('string'):
                testString = testString + record.string

        subscribeNode = UbiiClientNode()
        subscribeNode.wait_for_connection()
        token = subscribeNode.subscribeRegex(regex, callbackTestString)
        time.sleep(2)

        topicShouldWork1 = TopicDataRecord()
        topicShouldWork1.topic = 'a1a'
        topicShouldWork1.client_id = self.node.get_id()
        topicShouldWork1.string = 'a'
        self.node.publish_immediately(topicShouldWork1)
        time.sleep(1)

        topicShouldNotWork1 = TopicDataRecord()
        topicShouldNotWork1.topic = 'd'
        topicShouldNotWork1.client_id = self.node.get_id()
        topicShouldNotWork1.string = 'z'
        self.node.publish_immediately(topicShouldNotWork1)
        time.sleep(1)

        topicShouldWork2 = TopicDataRecord()
        topicShouldWork2.topic = 'aa'
        topicShouldWork2.client_id = self.node.get_id()
        topicShouldWork2.string = 'b'
        self.node.publish_immediately(topicShouldWork2)
        time.sleep(1)

        topicShouldNotWork2 = TopicDataRecord()
        topicShouldNotWork2.topic = 'a'
        topicShouldNotWork2.client_id = self.node.get_id()
        topicShouldNotWork2.string = 'y'
        self.node.publish_immediately(topicShouldNotWork2)
        time.sleep(1)

        topicShouldWork3 = TopicDataRecord()
        topicShouldWork3.topic = 'ab'
        topicShouldWork3.client_id = self.node.get_id()
        topicShouldWork3.string = 'c'
        self.node.publish_immediately(topicShouldWork3)
        time.sleep(1)

        topicShouldNotWork3 = TopicDataRecord()
        topicShouldNotWork3.topic = '2'
        topicShouldNotWork3.client_id = self.node.get_id()
        topicShouldNotWork3.string = 'x'
        self.node.publish_immediately(topicShouldNotWork3)
        time.sleep(1)

        subscribeNode.unsubscribe(token)
        time.sleep(2)

        topicShouldWorkButNotSubscribed = TopicDataRecord()
        topicShouldWorkButNotSubscribed.topic = 'a1a'
        topicShouldWorkButNotSubscribed.client_id = self.node.get_id()
        topicShouldWorkButNotSubscribed.string = 'shouldntWork'
        self.node.publish_immediately(topicShouldWorkButNotSubscribed)
        time.sleep(1)

        topicShouldWorkButNotSubscribed2 = TopicDataRecord()
        topicShouldWorkButNotSubscribed2.topic = 'aa'
        topicShouldWorkButNotSubscribed2.client_id = self.node.get_id()
        topicShouldWorkButNotSubscribed2.string = 'shouldntWork2'
        self.node.publish_immediately(topicShouldWorkButNotSubscribed2)
        time.sleep(1)

        #print(testString)
        #print(stringShouldBe)

        self.assertEqual(testString,stringShouldBe)

        subscribeNode.stop_node()

        print('end: testSubscribeRegex')
'''

'''
    def testMultiprocessingMixed(self):
        topicString = str(uuid.uuid4())

        async def process_target(queue, ubii_node):
            print("process_target")
            loop = asyncio.get_running_loop()
            print("process_target, loop:", loop)
            futureTestFinished = loop.create_future()

            def sub_callback(record):
                nonlocal futureTestFinished
                print("sub_callback")
                queue.put(record.int32)
                futureTestFinished.set_result(True)

            await ubii_node.subscribe_topic(topicString, sub_callback)
            await futureTestFinished

        print("start: testMultiprocessingMixed")
        queue = mp.Queue()
        process = mp.Process(target=process_target, args=(queue, self.node,))
        random_int = publishRandomInt(self.node, topicString)
        int_from_queue = queue.get()
        print("queue:", int_from_queue)
        self.assertEqual(random_int, int_from_queue)
        process.join()
        print("end: testMultiprocessingMixed")
'''
        
class TestUbiiAsync(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.node = UbiiClientNode("python testing")
        self.node.wait_for_connection()

    def tearDown(self):
        self.node.stop_node()
    
    '''
    async def testServiceCalls(self):
        print('start: testServiceCalls')
        nodeList = []
        resultShouldEqual = ClientList()
        resultShouldEqual.elements.append(self.node.clientSpecification)

        async def make_repeated_service_calls(node):
            request = ServiceRequest()
            request.topic = '/services/client/get_list'
            reply = await node.call_service(request)

        numThreads = 5
        for i in range(numThreads):
            nodeI = UbiiClientNode("testServiceCalls node " + str(i))
            nodeI.wait_for_connection()
            resultShouldEqual.elements.append(nodeI.clientSpecification)
            nodeList.append(nodeI)

        request = ServiceRequest()
        request.topic = '/services/client/get_list'
        response = self.node.call_service(request).result().client_list

        self.assertEqual(response, resultShouldEqual)
        for n in nodeList:
            n.stop_node()

        print('end: testServiceCalls')
    '''
       
    async def test_publish(self):
        print('start: test_publish')
        loop = asyncio.get_running_loop()
        future_test_finished = loop.create_future()
        
        counter_records_received = 0
        number_of_publishes = 10
        ints_published = []
        ints_received = []
        def callback(record):
            nonlocal counter_records_received
            nonlocal number_of_publishes
            nonlocal future_test_finished
            if record.HasField('int32'):
                counter_records_received += 1
                ints_received.append(record.int32)
                if (counter_records_received == number_of_publishes):
                    future_test_finished.set_result(True)
                else:
                    int = publish_random_int(self.node, topic_string)
                    ints_published.append(int)
        
        topic_string = str(uuid.uuid4())
        token = await self.node.subscribe_topic(topic_string, callback)
        
        int = publish_random_int(self.node, topic_string)
        ints_published.append(int)
        
        await future_test_finished
        self.assertEqual(ints_published, ints_received)
        
        print('end: test_publish')
       
    async def test_publish_immediately(self):
        print('start: test_publish_immediately')
        loop = asyncio.get_running_loop()
        future_test_finished = loop.create_future()
        
        counter_records_received = 0
        number_of_publishes = 10
        ints_published = []
        ints_received = []
        def callback(record):
            nonlocal counter_records_received
            nonlocal number_of_publishes
            nonlocal future_test_finished
            if record.HasField('int32'):
                counter_records_received += 1
                ints_received.append(record.int32)
                if (counter_records_received == number_of_publishes):
                    future_test_finished.set_result(True)
                else:
                    int = publish_immediately_random_int(self.node, topic_string)
                    ints_published.append(int)
        
        topic_string = str(uuid.uuid4())
        token = await self.node.subscribe_topic(topic_string, callback)
        
        int = publish_immediately_random_int(self.node, topic_string)
        ints_published.append(int)
        
        await future_test_finished
        self.assertEqual(ints_published, ints_received)
        
        print('end: test_publish_immediately')


    '''
    async def test_publish_topic_list(self):
        print('start: test_publish_topic_list')
        loop = asyncio.get_running_loop()
        allTopicsPublished = loop.create_future()
        numTopics = 100

        topicsShouldBe = []
        for i in range(numTopics):
            topicDataRecord = TopicDataRecord()
            topicDataRecord.topic = self.node.get_id() + '/test-topic:' + str(i)
            topicDataRecord.string = 'testString:' + str(i)
            await self.node.subscribe_topic(topicDataRecord.topic, lambda record : topicsShouldBe.append(record.topic))
            #topicsShouldBe.append(topicDataRecord.topic)
            self.node.publish(topicDataRecord)
            
        while (len(topicsShouldBe) < numTopics):
            await asyncio.sleep(0.5)
            
        request = ServiceRequest()
        request.topic = '/services/topic_list'

        response = self.node.call_service(request).result().string_list.elements
        setShould = set(topicsShouldBe)
        setIs = set(response)

        self.assertTrue(setShould.issubset(setIs))

        print('end: test_publish_topic_list')
    '''
        
    
    async def test_publish_from_multiprocessing_subprocess(self):
        print("start: test_publish_from_multiprocessing_subprocess")
        
        loop = asyncio.get_running_loop()
        future_topic_int = loop.create_future()
        
        def callback_topic(record):
            nonlocal future_topic_int
            future_topic_int.set_result(record.int32)
        
        topic_tring = str(uuid.uuid4())
        await self.node.subscribe_topic(topic_tring, callback_topic)
        
        mp.set_start_method('spawn')
        queue = mp.Queue()
        process = mp.Process(target=multiprocessing_target, args=(queue, topic_tring,))
        process.start()
        int_from_queue = queue.get()
        process.join()
        
        await future_topic_int
        self.assertEqual(int_from_queue, future_topic_int.result())
        print("end: test_publish_from_multiprocessing_subprocess")


if __name__ == '__main__':
    unittest.main()