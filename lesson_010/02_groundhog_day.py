# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


# TODO создайте константу список в котором будут храниться имена class ов чтобы их потом можно было выбрать и вызвать!
# TODO имена классов храним без их вызовов

# TODO функция one_day() должна возвращать карму от 1 до 7 или рейзит ошибку из расчета 1 к 13
# TODO мы можем объявить 2 переменные это карма равная рендинт от 1 до 7 и
# TODO сам еррор который тоже равен рендинт от 1 до 13
# TODO далее условие если еррор равен 13 то мы choice выбираем случайное исключение из списка
# TODO и его рейзим как объект используя ()
# TODO если условие не сработало то мы ретурним карму
def one_day():
    one_day_carma = randint(1, 8)
    chance_error = randint(1, 14)
    if chance_error == 3:
        raise IamGodError('Я Бог!')
    elif chance_error == 5:
        raise DrunkError('Синька - Зло!')
    elif chance_error == 7:
        raise CarCrashError('Авария - дочь мента!')
    elif chance_error == 9:
        raise GluttonyError('Очередной смертный грех')
    elif chance_error == 11:
        raise DepressionError('Я никому не нужен!!!')
    elif chance_error == 13:
        raise SuicideError('Прыгну со скалы!')
    else:
        return one_day_carma


ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0
count_day = 0

while True:
    try:
        carma += one_day()
        count_day += 1
        # TODO условие на выход задать в цикле заголовке
        if carma >= ENLIGHTENMENT_CARMA_LEVEL:
            print(f'Добро пожаловать в реальный мир!  Ваша карма {carma}')
            print(f'Вы были у сурка {count_day} дней')
            break
    except Exception as exc:
        # TODO пишем функцию на запись через with
        file = open('log_error.txt', 'a', encoding='utf8')
        file.write(f'Поймано исключение {exc} ')
        file.write('\n')
        file.close()

# https://goo.gl/JnsDqu
