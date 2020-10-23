import random

comp_position = {}
user_position = {}


def random_int():
    """Генерируем четырехзначное число без ноля в первой позиции и повторяющихся цыфр,"""
    number = '0'
    while '0' in number[0] or len(set(number)) < 4 or number.isdigit() is False:
        number = str(random.randint(1000, 10000))
    # print(number)
    return number


def check_int(number):
    """Проверка четырехзначного числа на наличие ноля в первой позиции и повторяющихся цифр.
    Возвращает False, если проверка не пройдена."""
    if '0' in number[0] or len(set(number)) < 4 or number.isdigit() is False:
        return False
    else:
        return True


def convert(first_number, second_number):
    """Конвертирует числа компьютера и пользователя в списки"""
    comp_number = list(map(int, first_number))
    user_number = list(map(int, second_number))
    return comp_number, user_number


def check_bulls_cows(comp, user):
    """Сравнивает числа компьютера и пользователя"""
    bulls = 0
    cows = 0

    for i, num in enumerate(comp):
        if num in user:
            if comp[i] == user[i]:
                bulls += 1
            else:
                cows += 1
    return {'bulls': bulls, 'cows': cows}
