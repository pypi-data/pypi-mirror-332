# Python client node v.2 for Ubi-Interact
This is the package for the [python client node v2](https://github.com/SandroWeber/ubii-node-python-v2) for the [Ubi-Interact](https://github.com/SandroWeber/ubi-interact/wiki) framework 

## Requirements and installation

- Tested for:
  - Linux and Windows
  - Python 3.10, 3.12

### Installation with [pip](https://pypi.org/project/Ubii-Python-Node-v2/)
```
$ pip install ubii-node-python-2
```



## How to use 
- Import the UbiiClientNode module and instanciate the client node 
    ```python
  from ubii.ubii_client_node import UbiiClientNode
  
  node = UbiiClientNode('pythonNodev2', 'http://localhost:8102/services/binary', 'ws://localhost:8104')
 
- Use the node to make service calls, subscribe to topics, publish topic data 
  ```python
  request = ServiceRequest()
  request.topic = '/services/topic_list'
  response = self.node.call_service(request)
  
  
  topicDataRecord = TopicDataRecord()
  topicDataRecord.topic = 'testTopic'
  node.publish(topicDataRecord)
   
  def printTopicDataRecord(record):
    print(record)
   
  node.subscribeTopic('testTopic', printTopicDataRecord)
  
  
  node.stopNode()
  ```
- For more information on the module check the documentation (index.html)


## ubii-msg-formats
To communicate with the masternode the client node uses protocol buffers. The framework provides a number of protobuf message definitions, to update to the newest message
definitions with [pip](https://pypi.org/project/ubii-msg-formats/) use:
```
$ pip install --upgrade ubii-msg-formats
```


## Testing

### test the published package

once:
```
virtualenv venv
source venv/bin/activate (linux) OR .\venv\Scripts\Activate.ps1 (windows)
pip install Ubii-Python-Node-v2
```

every time:
```
source venv/bin/activate (if not active)
python test/test.py
```

### test local code

Setup:
```
python -m virtualenv venv-testsrc
source venv-testsrc/bin/activate (linux) OR .\venv-testsrc\Scripts\Activate.ps1 (windows)
pip install -e .
```

```
python ./testing/runTests.py (linux) OR python .\testing\runTests.py (windows)
```

## Building
```
python3 -m pip install --upgrade build
python3 -m build / py -m build
```

## Bugs

- There is a problem in python 3.9 and 3.10 where starting threads while the interpreter shuts down can lead to a RuntimeError: 'cannot schedule new futures after interpreter shutdown'. If this occurs one quck fix is to add a time.sleep to the end of the main file.