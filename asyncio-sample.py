import asyncio


async def test_async_func():
    while True:
        await asyncio.sleep(1)
        print('come')
    return True


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_async_func())

