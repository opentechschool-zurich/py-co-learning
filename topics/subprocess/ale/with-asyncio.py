# https://stackoverflow.com/a/50758540/5239250
import asyncio

async def read_key():
    for i in range(3):
        await asyncio.sleep(2)
        print('reading a key')

    print('key pressed')
    raise Exception('key pressed')

async def read_process():
    for i in range(10):
        await asyncio.sleep(1)
        print('processing')

    raise Exception('no more process')

async def main():
    gathering = asyncio.gather(
        read_key(),
        read_process()
    )
    try:
        await gathering
    except Exception:
        for task in gathering._children:
            task.cancel() 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
