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
    """Write your code here"""
    print('2 seconds have passed')


def my_fun_2():
    """Write your code here"""
    print('5 seconds have passed')


def main():
    while True:
        my_fun_1()
        my_fun_2()


if __name__ == '__main__':
    main()
