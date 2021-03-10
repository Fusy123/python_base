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
    def __init__(self):
        self.name = 'Вода'

    def add(self, other):
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

    def __str__(self):
        return 'Вода'


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def add(self, other):
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

    def __str__(self):
        return 'Воздух'


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def add(self, other):
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

    def __str__(self):
        return 'Огонь'


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def add(self, other):
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

    def __str__(self):
        return 'Земля'


class Witch:
    def __init__(self):
        self.name = 'Ведьма'

    def add(self, other):
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

    def __str__(self):
        return 'Ведьма'


class Storm:
    def __init__(self):
        self.name = 'Шторм'


    def _str__(self):
        return print(self.name)


class Overflow:
    def _str__(self):
        return print('Наводнение')


# class Experiences:



print('-' * 25 + ' Игра Алхимия ' + '-' * 25)
print('')
#
# composition = {'1': [Water(name='Вода')],
#                '2': [Air(name='Воздух')],
#                '3': [Fire(name='Огонь')],
#                '4': [Earth(name='Земля')],
#                '5': [Witch(name='Ведьма')]
#                }
#
water = Water()
air = Air()
fire = Fire()
earth = Earth()
witch = Witch()

print(' У нас есть следующие элементы: ')
# for elements in composition:
print(water.name, air.name)
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


# experiences = water + air
# print(experiences)
print(water.name, '+', air.name, '=', Water.add(self=water, other=air))


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
