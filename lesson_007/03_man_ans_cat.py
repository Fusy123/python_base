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


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.life = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            # TODO уменьшаем сытость
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил(а) на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play_sega(self):
        cprint('{} играл(а) на приставке целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 100:
            cprint('{} сходил(а) в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cat_food_shopping(self):
        if self.house.cat_food < len(cats) * 10 and self.house.money >= 50:
            cprint('{} сходил(а) в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        if self.house.mud >= 100:
            cprint('{} Прибрался дома'.format(self.name), color='blue')
            self.house.mud -= 100
            self.fullness -= 20
        else:
            cprint('{} в доме чисто.'.format(self.name), color='blue')

    def go_to_the_house(self, house):
        self.house = house
        # TODO что за параметр ?
        self.life = 1
        self.fullness -= 10
        # TODO что за параметр ?
        life.append(citisen.name)
        cprint('{} Въехал(а) в дом'.format(self.name), color='cyan')

    def go_to_the_cat_house(self):
        # TODO что тут происходит опишите каждую строку
        if len(dead) == 0:
            cat = Cat()
            cats.append(cat)
            cat.life = 1
            life.append(cat.name)
            self.fullness -= 10
            cprint('{} Взяли'.format(cat.name), color='cyan')

    def man_act(self):
        # TODO проверку на жизнь выносим в отдельный метод
        if self.fullness <= 0:
            cprint('{} умер(ла)...'.format(self.name), color='red')
            self.life = 0
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif len(cats) > 0 and self.house.cat_food <= 10:
            self.cat_food_shopping()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.mud >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.go_to_the_cat_house()
        else:
            self.play_sega()


class Cat:

    def __init__(self):
        self.name = choice(cat_names)
        self.fullness = 50
        self.house = citisen.house
        self.life = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def play_wallpapper(self):
        cprint('{} драл обои целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.house.mud += 5

    def sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def cat_act(self):
        # TODO проверку на жизнь выносим в отдельный метод
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            cat.life = 0
            return

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


class House:
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


citizens = [Man(name='Муж'),
            Man(name='Жена')
            ]

cat_names = ['Кот', 'Пушистик', 'Киска', 'Мохнатый ублюдок', 'Облезлый', 'Длинный хвост',
             'ДИАВОЛ', 'Васька', 'Мурзик', 'Рыжий', 'Одноухий', 'Ушлепок', 'Боксер', 'Р2Д2', 'Мячик']

cats = []
dead = []
life = []

my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

# TODO опишите логику вашего цикла по блокам и подробней
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.man_act()
        if citisen.life == 0:
            dead.append(citisen.name)
            life.remove(citisen.name)
            citizens.remove(citisen)
        else:
            continue

    for cat in cats:
        cat.cat_act()
        if cat.life == 0:
            if cat.name is not dead:
                dead.append(cat.name)
            life.remove(cat.name)
            cats.remove(cat)
        else:
            continue
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)
    print('')

print('')
print('Живут в доме: ', end='')
print(', '.join(map(str, life)))
print('')
print('Умер:', ', '.join(map(str, dead)))

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
