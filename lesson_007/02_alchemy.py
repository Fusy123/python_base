# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Water):
            return Overflow()  # наводнение = Вода + Вода
        elif isinstance(other, Air):
            return Storm()  # шторм = Вода + Воздух
        elif isinstance(other, Fire):
            return Steam()  # пар = Вода + Огонь
        elif isinstance(other, Earth):
            return Mud()  # грязь = Вода + Земля
        elif isinstance(other, Witch):
            return WetWitch()  # мокрая ведьма = Вода + Ведьма
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()  # шторм = Вода + Воздух
        elif isinstance(other, Air):
            return Hurricane()  # ураган = Воздух + Воздух
        elif isinstance(other, Fire):
            return Lightning()  # молния = Воздух + Огонь
        elif isinstance(other, Earth):
            return Dust()  # пыль = Воздух + Земля
        elif isinstance(other, Witch):
            return Bastinda()  # Бастинда = Ведьма + Воздух
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()  # пар = Вода + Огонь
        elif isinstance(other, Air):
            return Lightning()  # молния = Воздух + Огонь
        elif isinstance(other, Fire):
            return Salute()  # салют = Огонь + Огонь
        elif isinstance(other, Earth):
            return Lava()  # лава = Земля + Огонь
        elif isinstance(other, Witch):
            return Inquisition()  # Inquisition = Ведьма + Огонь
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()  # грязь = Вода + Земля
        elif isinstance(other, Air):
            return Dust()  # пыль = Земля + Воздух
        elif isinstance(other, Fire):
            return Lava()  # лава = Земля + Огонь
        elif isinstance(other, Earth):
            return Earthquake()  # землятрясение = Земля + Земля
        elif isinstance(other, Witch):
            return DirtyGirl()  # грязная девчонка = Ведьма + Земля
        else:
            return None


class Witch:
    def __str__(self):
        return 'Ведьма'


def __add__(self, other):
    if isinstance(other, Water):
        return WetWitch()  # мокрая ведьма = Ведьма + Вода
    elif isinstance(other, Air):
        return Bastinda()  # Бастинда = Ведьма + Воздух
    elif isinstance(other, Fire):
        return Inquisition()  # Inquisition = Ведьма + Огонь
    elif isinstance(other, Earth):
        return DirtyGirl()  # грязная девчонка = Ведьма + Земля
    elif isinstance(other, Witch):
        return WomenMudFights()  # женские бои в грязи = Ведьма + Ведьма
    else:
        return None


class Hurricane(object):
    def __str__(self):
        return 'Ураган'


class Storm:
    def __str__(self):
        return 'Шторм'


class Overflow:
    def __str__(self):
        return 'Наводнение'


class Steam(object):
    def __str__(self):
        return 'Пар'


class Mud(object):
    def __str__(self):
        return 'Грязь'


class WetWitch(object):
    def __str__(self):
        return 'Мокрая ведьма'


class Bastinda(object):
    def __str__(self):
        return 'Бастинда раздавленная домиком Элли'


class Inquisition(object):
    def __str__(self):
        return 'Святые Костры Инквизиции'


class DirtyGirl(object):
    def __str__(self):
        return 'Грязная девчонка'


class WomenMudFights(object):
    def __str__(self):
        return 'Женские бои в грязи'


class Earthquake(object):
    def __str__(self):
        return 'Землятрясение'


class Lava(object):
    def __str__(self):
        return 'Лава'


class Dust(object):
    def __str__(self):
        return 'Пыль'


class Salute(object):
    def __str__(self):
        return 'Салют'


class Lightning(object):
    def __str__(self):
        return 'Молния'


print('-' * 25 + ' Игра Алхимия ' + '-' * 25)
print('')

composition = [['1', 'Вода'],
               ['2', 'Воздух'],
               ['3', 'Огонь'],
               ['4', 'Земля'],
               ['5', 'Ведьма']
               ]

water = Water()
air = Air()
fire = Fire()
earth = Earth()
witch = Witch()

print(' У нас есть следующие элементы: ')
# for elements in composition:
print(water, air)
print('')
# while True:
#     first_element = (input('Введите первый элемент: '))
#     if first_element in composition.keys():
#         first_user_element = composition[first_element][0]
#     else:
#         print('Вы ввели неправильный номер элемента!')
#         continue
#     second_element = (input('Введите второй элемент: '))
#     if second_element in composition.keys():
#         second_user_element = composition[second_element][0]
#         break
#     else:
#         print('Вы ввели неправильный номер элемента!')


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.