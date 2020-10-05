from random import randint

_herd = []
user_input = []

def gather_herd():
    """загадываем число"""
    global _herd
    tmp = randint(1, 9)
    _herd.append(tmp)
    while True:
        for i in range(3):
            tmp = randint(0, 9)
            while _herd[i] == tmp:
                tmp = randint(0, 9)
            _herd.append(tmp)
        if len(set(_herd)) == 4:
            break
    print(_herd)


def input_number():
    """ввод числа пользователем"""
    global user_input
    while True:
        user_input = input('Введите 4 неповторяющиеся цифры: ')
        if len(user_input) != 4 or not user_input.isdigit():
            continue
        user_input = list(map(int, user_input))
        if len(set(user_input)) == 4:
            break
    return user_input


def check(user_input, _herd):
    """сравнение чисел"""
    bulls, cows = 0, 0
    for i, num in enumerate(user_input):
        if num in _herd:
            if user_input[i] == _herd[i]:
                bulls += 1
            else:
                cows += 1
    print(bulls, cows)
    return bulls, cows



def del_bad_answer():
    """удаление неподходящих вариантов"""
    pass


gather_herd()
input_number()
check(user_input, _herd)