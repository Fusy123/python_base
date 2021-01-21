import random


def random_int():
    """Генерируем четырехзначное число без ноля в первой позиции и повторяющихся цыфр,"""
    while True:
        global comp_number
        comp_number = str(random.randint(1000, 9999))
        if len(comp_number) == len(set(comp_number)):
            # print(comp_number)
            break
    return comp_number


def user_valid_number(user_number):
    """Проверка четырехзначного числа на наличие ноля в первой позиции
    и повторяющихся цифр"""
    valid_params = [user_number.isdigit(),
                    len(set(user_number)) == 4,
                    str(user_number[0]) != '0',
                    len(user_number) == 4]
    if all(valid_params):
        return True


def check_bulls_cows(user_number):
    """Сравнивает числа компьютера и пользователя"""
    bulls = 0
    cows = 0
    compnumber = list(map(int, comp_number))
    user_number = list(map(int, user_number))
    for i, num in enumerate(compnumber):
        if num in user_number:
            if compnumber[i] == user_number[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows
