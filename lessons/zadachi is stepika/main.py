import math
import random


def igra():
    y = int(input('Укажите диапазон чисел от 1 до ....'))
    n = random.randint(1, y)
    def is_valid(x):
        if 1 <= x <= y:
            return True
        else:
            return False

    count = 0
    while True:
        x = float(input('Введите число '))
        count += 1
        if not is_valid(x):
            x = float(input('Вы ввели некорректное число, введите снова!! '))
        if is_valid(n):
            x = round(x, 0)
            if x < n:
                print('Ваше число МЕНЬШЕ загаданного, попробуйте еще разок...')
            if x > n:
                print('Ваше число БОЛЬШЕ загаданного, попробуйте еще разок...')
            if x == n:
                print('Вы угадали, поздравляем!')
                break
    print('Число попыток: ', count)
    print('Спасибо, что играли в числовую угадайку')
    print('Хотите сыграть еще, (n/y)')
    s = str(input())
    if s == 'y':
        igra()
    else:
        print('Увидимся!')
    return

print('Добро пожаловать в числовую угадайку! ' )

igra()
