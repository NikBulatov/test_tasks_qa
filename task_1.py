from time import time

"""
Python 1
Задание:
Напишите код функций так, 
чтобы одна из них выводила в консоль свою запись через 2 секунды,
а вторая через 5.
Функции должны работать "одновременно"
(допускается небольшая погрешность по времени)
"""


def my_fun_1():
    current = time()
    try:
        my_fun_1.passed += current - my_fun_1.prev_time
    except Exception:
        my_fun_1.passed = 0

    my_fun_1.prev_time = current

    if my_fun_1.passed >= 2:
        print('2 seconds have passed')
        my_fun_1.passed = 0


def my_fun_2():
    """Write your code here"""
    current = time()
    try:
        my_fun_2.passed += current - my_fun_2.prev_time
    except Exception:
        my_fun_2.passed = 0

    my_fun_2.prev_time = current

    if my_fun_2.passed >= 5:
        print('5 seconds have passed')
        my_fun_2.passed = 0


def main():
    while True:
        my_fun_1()
        my_fun_2()


if __name__ == '__main__':
    main()
