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
import random
from random import randint


class IamGodError(Exception):
    def __init__(self, input_data=None):
        self.message = 'Я Бог!'
        self.input_data = input_data

    def __str__(self):
        return self.message


class DrunkError(Exception):
    def __init__(self, input_data=None):
        self.message = 'Синька - Зло!'
        self.input_data = input_data

    def __str__(self):
        return self.message


class CarCrashError(Exception):
    def __init__(self, input_data=None):
        self.message = 'Авария - дочь мента!'
        self.input_data = input_data

    def __str__(self):
        return self.message


class GluttonyError(Exception):
    def __init__(self, input_data=None):
        self.message = 'Очередной смертный грех'
        self.input_data = input_data

    def __str__(self):
        return self.message


class DepressionError(Exception):
    def __init__(self, input_data=None):
        self.message = 'Я никому не нужен!!!'
        self.input_data = input_data

    def __str__(self):
        return self.message


class SuicideError(Exception):
    def __init__(self, input_data=None):
        self.message = 'Прыгну со скалы!'
        self.input_data = input_data

    def __str__(self):
        return self.message


def one_day(error_list):
    one_day_carma = randint(1, 8)
    chance_error = randint(1, 14)
    if chance_error == 13:
        karma_error = random.choice(error_list)
        raise karma_error

    return one_day_carma


ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0
count_day = 0
error_list = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]

with open('log_error.txt', 'w', encoding='utf8') as file:
    while carma <= ENLIGHTENMENT_CARMA_LEVEL:
        try:
            carma += one_day(error_list)
            count_day += 1
        except Exception as exc:
            file.write(f'Поймано исключение {exc} \n')



print(f'Добро пожаловать в реальный мир!  Ваша карма {carma}')
print(f'Вы были у сурка {count_day} дней')
# https://goo.gl/JnsDqu

# TODO применяем рекомендации данные ранее по неймингу переменных не указываем в именовании ее тип
