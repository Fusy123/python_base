from random import randint

_herd = []
user_input = []


def gather_herd():
    """загадываем число"""
    # TODO Можно упростить заводим бесконечный цикл
    # TODO final_result присваиваем строку в которой randint(1000, 9999)
    # TODO Потом проверяем если set этой строки без дублей, (и прочекать длину)
    # TODO то выходим из цикла
    # TODO и возвращаем нужный нам результат
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
    return _herd

# TODO нет проверки на первый 0 у числа у пользователя!

# TODO эту функцию разбиваем на две части та которая выводит инпут мы описываем в главном модуле.
# TODO ту часть которая отвечает за логику проверки оставляем тут! По скольку принты тут не должны быть!
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


def check(number, herd):
    """сравнение чисел"""
    bulls, cows = 0, 0
    for i, num in enumerate(number):
        if num in herd:
            if number[i] == herd[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows
