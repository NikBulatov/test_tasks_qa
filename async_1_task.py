import asyncio
import time

"""
Python 1
Задание:
Напишите код функций так, 
чтобы одна из них выводила в консоль свою запись через 2 секунды,
а вторая через 5.
Функции должны работать "одновременно"
(допускается небольшая погрешность по времени)
"""


async def my_fun_1():
    """Write your code here"""
    await asyncio.sleep(2)
    print('2 seconds have passed')


async def my_fun_2():
    """Write your code here"""
    await asyncio.sleep(5)
    print('5 seconds have passed')


async def main():
    start = time.time()
    
    while True:
        task_1 = asyncio.create_task(my_fun_1())
        task_2 = asyncio.create_task(my_fun_2())
        
        for task in task_1, task_2:
            await task
            print(time.time() - start, '\n')



if __name__ == '__main__':
    asyncio.run(main())
