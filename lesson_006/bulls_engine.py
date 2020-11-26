import random
from termcolor import cprint, colored


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
    user_number = input(colored('Введите четырехзначное число (число не должно начинаться с нуля и содержать '
                                'повторяющихся цифр): ', color='red'))
    if (len(list(user_number)) != 4) or (user_number.isdigit() is False):
        cprint('Вы ввели неправильное число!', color='yellow')
        return user_input()
    elif set(user_number[0]) == set('0') or len(user_number) != len(set(user_number)):
        cprint('Вы ввели неправильное число!', color='yellow')
        return user_input()
    else:
        return user_number


def check_bulls_cows(comp_number, user_number):
    """Сравнивает числа компьютера и пользователя"""
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
    return bulls, cows


# TODO принтов тут быть не должно, есл ивы хотите написать функцию которая проверяет только на выигрыш
# TODO все принты должны быть в главном модуле.
# как тогда понимать вашу ??? # TODO Вторая как раз будет функция новая_игра() в ней мы совместим общение с пользователем если он выиграл
# TODO + попросим выбрать его будет ли он играть еще раз или выходим!
def games(bulls, cows):
    count_games = 1
    if bulls != 4:
        print(colored('Текущий счет игры: Быки -', color='red'), colored(bulls, color='yellow'),
              colored('Коровы -', color='red'), colored(cows, color='yellow'), end='.\n')
        print('Вы не угадали. Попробуйте еще раз: ')
        count_games += 1
        user_input()
        check_bulls_cows(comp_number, user_number)
    else:
        print(colored('Текущий счет игры: Быки -', color='green'), colored(bulls, color='yellow'),
              colored('Коровы -', color='red'), colored(cows, color='yellow'), end='.\n')
        print(colored('Поздравляем! Вы угадали за', color='green', attrs=['bold']),
              colored(count_games, color='green', attrs=['bold']),
              colored('попыток', color='green', attrs=['bold']))
        question = input('Хотите сыграть еще одну партию? (y/n)')
        if question.lower() == 'n':
            print('Игра окончена. Удачи!')
            break




