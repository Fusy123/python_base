# -*- coding: utf-8 -*-

from random import randint
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
            cprint('{} нет еды'.format(self.name), color='red')
            # TODO дополнительные методы в методах не вызываем, так у нас будет два действия за место одного
            self.shopping()

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
        # TODO На каждый if пишем else
        if cat_house.catfood < len(cats) * 10 and self.house.money >= 50:
            cprint('{} сходил(а) в магазин за едой для кота'.format(self.name), color='magenta')
            cat_house.catfood += 50
            self.house.money -= 50

    def clean_house(self):
        # TODO пишем else говорим что еще чисто в доме
        if cat_house.mud >= 100:
            cprint('{} Прибрался дома'.format(self.name), color='blue')
            cat_house.mud -= 100
            self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал(а) в дом'.format(self.name), color='cyan')

    def act(self):
        # TODO Выносим в отдельный метод и будем запускать в цикле
        if self.fullness <= 0:
            cprint('{} умер(ла)...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif cat_house.catfood <= len(cats) * 10:
            self.cat_food_shopping()
        elif self.house.food <= 20:
            self.shopping()
        elif cat_house.mud >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_sega()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        # TODO переменные пишем в стиле snake_case
        self.cathouse = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if cat_house.catfood >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            cat_house.catfood -= 10
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')
            # TODO Аналогично ТУДУ выше
            citisen.cat_food_shopping()

    def play_wallpapper(self):
        cprint('{} драл обои целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.cathouse.mud += 5

    def sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    # TODO у кота не может быть этого метода его должен заселять человек
    def go_to_the_cathouse(self, house):
        self.cathouse = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='cyan')

    def act(self):
        # TODO Аналогично
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
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

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money,
        )


# TODO у человека и кота должен быть одна крыша над головой
class CatHouse:
    def __init__(self):
        self.catfood = 0
        self.mud = 0

    def __str__(self):
        return 'В доме осталось кошачей еды {}, уровень грязи {}'.format(
            self.catfood, self.mud,
        )


citizens = [Man(name='Муж'),
            Man(name='Жена')
            ]
cats = [Cat(name='Кот'),
        Cat(name='Пушистик'),
        Cat(name='Киска'),
        Cat(name='Мохнатый ублюдок'),
        Cat(name='Облезлый'),
        Cat(name='Длинный хвост'),
        Cat(name='ДИАВОЛ'),
        Cat(name='Васька')
        ]

my_sweet_home = House()
cat_house = CatHouse()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for cat in cats:
    cat.go_to_the_cathouse(house=cat_house)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)
    print(cat_house)
    # TODO в конце цикла чекаем людей и животных на жизнь

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
