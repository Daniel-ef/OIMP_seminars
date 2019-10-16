import asyncio
from datetime import datetime


async def count_print():
    a = []
    for i in range(5000000):
        a.append(i)


async def sleep(task_num):
    print(f'Go to sleep, task_num: {task_num} {datetime.now()}')
    await asyncio.create_task(count_print())
    print(f'Awaking, task_numk {task_num} {datetime.now()}')


async def main():
    await asyncio.gather(sleep(1), sleep(2), sleep(3))

asyncio.run(main())
