import asyncio
import multiprocessing
import uuid
from pyomyo import Myo, emg_mode
from ubii.ubii_client_node import UbiiClientNode
from proto.topicData.topicDataRecord_pb2 import TopicDataRecord

'''
async def deferred_entry_async():
    await asyncio.sleep(1)
    print("hello from deferred_entry_async()")

def entry_sync():
    try:
        loop = asyncio.get_running_loop()
        print("entry_sync - event loop: ", loop)
    except Exception:
        print("entry_sync - no event loop found!")
        loop = asyncio.run(deferred_entry_async())
        print("entry_sync - event loop from asyncio.run(): ", loop)
'''

def worker(q):
	m = Myo(mode=emg_mode.RAW)
	m.connect()
	
	def add_to_queue(emg, movement):
		q.put(emg)

	m.add_emg_handler(add_to_queue)
	
	def print_battery(bat):
		print("Battery level:", bat)

	m.add_battery_handler(print_battery)

	# Orange logo and bar LEDs
	m.set_leds([128, 0, 0], [128, 0, 0])
	# Vibrate to know we connected okay
	m.vibrate(1)
	
	"""worker function"""
	while True:
		m.run()
	print("Worker Stopped")

async def entry_async():
    ubii_node = UbiiClientNode("test myo")
    ubii_node.wait_for_connection()
    topic_emg = str(uuid.uuid4())
    
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    
    try:
        while True:
            while not(q.empty()):
                emg = list(q.get())
                #print(emg)
                record = TopicDataRecord()
                record.topic = topic_emg
                record.int32_list.elements.extend(emg)
                ubii_node.publish(record)
                
    except KeyboardInterrupt:
        print("Quitting")
        quit()

if __name__ == '__main__':
    #entry_sync()
    asyncio.run(entry_async())