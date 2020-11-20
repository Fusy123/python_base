import random
from termcolor import cprint, colored

comp_position = {}
user_position = {}


def random_int():
    """Генерируем четырехзначное число без ноля в первой позиции и повторяющихся цыфр,"""
    while True:
        comp_number = str(random.randint(1000, 9999))
        if len(comp_number) == len(set(comp_number)):
            print(comp_number)
            break
    return comp_number


def user_input():
    """Ввод числа пользователем и проверка четырехзначного числа на наличие ноля в первой позиции
    и повторяющихся цифр"""
    while True:
        user_number = input(colored('Введите четырехзначное число (число не должно начинаться с нуля и содержать '
                                    'повторяющихся цифр): ', color='red'))
        if (len(list(user_number)) != 4) or (user_number.isdigit() is False):
            return user_input()
        elif set(user_number[0]) == set('0') or len(user_number) != len(set(user_number)):
            return user_input()
        else:
            return user_number


def check_bulls_cows(comp_number, user_number, count_games):
    """Сравнивает числа компьютера и пользователя"""
    total = ()
    bulls = 0
    cows = 0
    comp_number = list(map(int, comp_number))
    user_number = list(map(int, user_number))

    for i, num in enumerate(comp_number):
        if num in user_number:
            if comp_number[i] == user_number[i]:
                bulls += 1
            else:
                cows += 1
    while bulls != 4:
        print(colored('Текущий счет игры: Быки -', color='red'), colored(bulls, color='yellow'),
              colored('Коровы -', color='red'), colored(cows, color='yellow'), end='.\n')
        print('Вы не угадали. Попробуйте еще раз: ')
        user_input()
        count_games += 1
        total = check_bulls_cows(comp_number, user_number)

    return total, count_games


def finish(total, count_games):
    if total['bulls'] == 4:
        print(colored('Текущий счет игры: Быки -', color='green'), colored(total['bulls'], color='yellow'),
              colored('Коровы -', color='red'), colored(total['cows'], color='yellow'), end='.\n')
        cprint('Поздравляем! Вы угадали число!', color='green', attrs=['bold'])
        print(colored('Вы угадали за', color='green', attrs=['bold']), colored(count_games,
                                                                               color='green', attrs=['bold']),
              colored('попыток', color='green', attrs=['bold']))
