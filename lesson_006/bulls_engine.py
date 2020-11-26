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


# TODO в Движке принтов быть не должно, часть этой функции которая отвечает за логическую проверку оставить тут,
# TODO а часть вынести в отдельную функцию в главном модуле, там у вас будут принты

# TODO не понимаю. у меня написана функция которая принимает и обрабатывает ввод введенного. смысл ее разбивать?
#  TODO чтобы перенести принты в другую функцию? и как тогда вынести принты при вводе неправильного числа? получается
# TODO что вся эта проверка переезжает в главный модуль.

def user_input(user_number):
    """Ввод числа пользователем и проверка четырехзначного числа на наличие ноля в первой позиции
    и повторяющихся цифр"""
    user_number = input(colored('Введите четырехзначное число (число не должно начинаться с нуля и содержать '
                                'повторяющихся цифр): ', color='red'))
    if (len(list(user_number)) != 4) or (user_number.isdigit() is False):
        cprint('Вы ввели неправильное число!', color='yellow')
        return False
    elif set(user_number[0]) == set('0') or len(user_number) != len(set(user_number)):
        cprint('Вы ввели неправильное число!', color='yellow')
        return False
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

