# -*- coding: utf-8 -*-

from random import randint, choice
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class House:
    """ класс дом. основные параметры"""

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 0
        self.mud = 0

    def __str__(self):
        if len(cats) == 0:
            return 'В доме еды осталось {}, денег осталось {}'.format(
                self.food, self.money)
        else:
            return 'В доме еды осталось {}, денег осталось {}.\nВ доме осталось кошачей еды {}, уровень грязи {}'.format(
                self.food, self.money, self.cat_food, self.mud)


class Man:
    """класс человек. задаем основные параметры и методы"""

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        """ метод работа"""
        cprint('{} сходил(а) на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play_sega(self):
        """ метод отдых"""
        cprint('{} играл(а) на приставке целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        """ метод поход в магазин"""
        if self.house.money >= 100:
            cprint('{} сходил(а) в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cat_food_shopping(self):
        """ метод поход в магазин за едой для кота"""
        if self.house.money >= 50:
            cprint('{} сходил(а) в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        """ метод уборка в доме"""
        if self.house.mud >= 100:
            cprint('{} Прибрался дома'.format(self.name), color='blue')
            self.house.mud -= 100
            self.fullness -= 20
        else:
            cprint('{} в доме чисто.'.format(self.name), color='blue')

    def go_to_the_house(self, house):
        """ метод заселение в дом """
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал(а) в дом'.format(self.name), color='cyan')

    def man_act(self):
        """метод активности человека"""
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif len(cats) > 0 and self.house.cat_food <= len(cats) * 10:
            self.cat_food_shopping()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.mud >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 4:
            self.clean_house()
        else:
            self.play_sega()

    def live_dead(self):
        """ метод проверки на живой мертвый"""
        if self.fullness < 0:
            cprint('{} умер(ла)...'.format(self.name), color='red')
            return True
        else:
            return False

    def go_to_the_cat_house(self, cat):
        """" метод добавления кота в дом"""
        if self.house:
            cat.house = self.house
            # self.fullness -= 10  # убавляем сытость человека
            cprint('Взяли {}'.format(cat.name), color='cyan')  # вывод


class Cat:
    """класс кот. основные параметры и методы"""

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        """ метод еда кота"""
        if citisen.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            citisen.house.cat_food -= 10
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def play_wallpapper(self):
        """ метод кот играет """
        cprint('{} драл обои целый день'.format(self.name), color='green')
        self.fullness -= 10
        citisen.house.mud += 5

    def sleep(self):
        """ метод кот спит """
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def cat_act(self):
        """ метод выбора активностей кота"""
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif self.fullness >= 30:
            self.play_wallpapper()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.play_wallpapper()
        else:
            self.sleep()

    def live_dead(self):
        """ метод проверки на живой мертвый"""
        if self.fullness < 0:
            cprint('{} умер(ла)...'.format(self.name), color='red')
            return True
        else:
            return False


citizens = [Man(name='Муж'),
            Man(name='Жена')
            ]

cat_names = ['Кот', 'Пушистик', 'Киска', 'Мохнатый ублюдок', 'Облезлый', 'Длинный хвост']
#             'ДИАВОЛ', 'Васька', 'Мурзик', 'Рыжий', 'Одноухий', 'Ушлепок', 'Боксер', 'Р2Д2', 'Мячик']

cats = []

my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for name in cat_names:
    cat = Cat(name=name)  # создаем обьект из класса сат
    citizens[0].go_to_the_cat_house(cat)
    cats.append(cat)

live = False
for day in range(1, 366):  # берем день начиная с 1 по 365 с шагом 1
    print('================ день {} =================='.format(day))
    for citisen in citizens:  # после чего берем жителя из списка жителей
        citisen.man_act()  # производим активность жителя
    for cat in cats:  # берем кота из списка котов
        cat.cat_act()  # производим активность кота

    print('--- в конце дня ---')
    for citisen in citizens:  # вывод показателей жителя
        print(citisen)
    for cat in cats:  # вывод показателей кота
        print(cat)
    print(my_sweet_home)
    print('')

    for citisen in citizens:
        if citisen.live_dead():
            live = True
    for cat in cats:
        if cat.live_dead():
            live = True
    if live:
        break


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# зачет!
