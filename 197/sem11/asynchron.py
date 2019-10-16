import asyncio
from datetime import datetime


async def sleep_(task_num):
    print(f'Go to sleep, task_num: {task_num} {datetime.now()}')
    await asyncio.sleep(5)
    print(f'Awake, task_num: {task_num} {datetime.now()}')


async def notify(sec: int):
    print(f'Enter notify {datetime.now()}')
    await asyncio.sleep(sec)
    print(f'Booo {datetime.now()}')
    # while True:
    #     if datetime.now() > dt:
    #         print('Booo')
    #         return
    #     else:
    #         await asyncio.sleep(0.000001)


async def main():
    await asyncio.create_task(notify(2))
    await asyncio.sleep(5)
    print('Exit')
    # await asyncio.gather(sleep_(1),
    #                      sleep_(2),
    #                      sleep_(3),
    #                      notify(datetime.now() +
    #                             timedelta(seconds=2)))

asyncio.run(main())
