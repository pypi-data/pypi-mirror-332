import asyncio
from ubii.ubii_client_node import UbiiClientNode

async def deferred_entry_async():
    await asyncio.sleep(1)
    print("hello from deferred_entry_async()")

async def entry_async():
    try:
        loop = asyncio.get_event_loop()
        print("entry_async - event loop: ", loop)
    except Exception:
        loop = asyncio.run(deferred_entry_async())
        print("entry_async - event loop from asyncio.run(): ", loop)

def entry_sync():
    try:
        loop = asyncio.get_running_loop()
        print("entry_sync - event loop: ", loop)
    except Exception:
        print("entry_sync - no event loop found!")
        loop = asyncio.run(deferred_entry_async())
        print("entry_sync - event loop from asyncio.run(): ", loop)

if __name__ == '__main__':
    entry_sync()
    #asyncio.run(entry_async())