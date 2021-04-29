# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:
    """ класс дом"""
    food_year = 0
    money_year = 0
    coat_year = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mud = 0
        self.cat_food = None

    def __str__(self):
        # TODO все лишнее удаляем из кода!
        # if self.cat_food is False:
        #     return 'В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(
        #         self.food, self.money, self.mud)
        # else:
        #     return 'В доме еды осталось {}, денег осталось {}.\nВ доме осталось кошачей еды {}, уровень грязи {}'.format(
        #         self.food, self.money, self.cat_food, self.mud)
        pass

    def muds(self):
        """добавляем грязь в дом"""
        self.mud += 5


class Man:
    """ класс человек"""

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None

    # def __str__(self):
    # # return 'Я - {}, сытость {}, уровень счастья {}'.format(self.name, self.fullness, self.happy)

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            portion = randint(10, 31)
            self.fullness += portion
            House.food_year += portion
            self.happy += 10
            self.house.food -= 10
            # cprint('{} съел {} единиц еды '.format(self.name, portion), color='yellow')
        else:
            self.fullness -= 10
            # cprint('{} нет еды'.format(self.name), color='red')

    def go_to_the_house(self, house):
        """ метод заселение в дом """
        self.house = house
        self.fullness -= 10
        # cprint('{} Въехал(а) в дом'.format(self.name), color='cyan')

    def live_dead(self):
        """ метод проверки на живой мертвый"""
        if self.fullness < 0 or self.happy <= 10:
            # cprint('{} умер(ла)...'.format(self.name), color='red')
            return True
        else:
            return False

    def happys(self):
        if self.house.mud > 90:
            self.happy -= 10

    def go_to_the_cat_house(self, cat):
        """" метод добавления кота в дом"""
        if self.house:
            cat.house = self.house
            # cprint('Взяли {}'.format(cat.name), color='cyan')
            self.house.cat_food = 30

    def pet_the_cat(self):
        """ гладим кота"""
        # cprint('{} гладил(а) кота'.format(self.name), color='green')
        self.happy += 5


class Husband(Man):
    """ класс муж"""
    salary = 50

    def act(self):
        """метод активности человека"""
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.gaming()
        elif dice == 4:
            self.pet_the_cat()
        else:
            self.work()

    def work(self):
        """ метод работа"""
        # cprint('{} сходил на работу'.format(self.name), color='blue')
        salary = 50
        self.house.money += salary
        self.fullness -= 10
        House.money_year += salary

    def gaming(self):
        """ метод отдых"""
        # cprint('{} играл на приставке целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happy += 20


class Wife(Man):
    """ класс жена"""

    def act(self):
        """метод активности человека"""
        dice = randint(1, 6)
        if self.house.food <= 10:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.shop_food_the_cat()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.mud > 100:
            self.clean_house()
        elif dice == 1:
            self.clean_house()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.shopping()
        elif dice == 5:
            self.pet_the_cat()
        elif dice == 4:
            self.shop_food_the_cat()
        else:
            self.buy_fur_coat()

    def shopping(self):
        """ метод поход в магазин"""
        if self.house.money >= 10:
            # cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            sale = randint(30, 61)
            self.house.money -= sale
            self.house.food += sale
            self.fullness -= 10
        else:
            self.fullness -= 10
            # cprint('{} деньги кончились!'.format(self.name), color='red')

    def shop_food_the_cat(self):
        """ метод поход в магазин за едой для кота"""
        if self.house.money >= 20 * len(Simulation.cats):
            # cprint('{} сходила в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.cat_food += len(Simulation.cats) * 20
            self.house.money -= len(Simulation.cats) * 20
        # else:
        # cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        """ метод поход за шубой"""
        if self.house.money > 400:
            # cprint('{} сходила в магазин за шубой'.format(self.name), color='magenta')
            self.house.money -= 350
            self.happy += 60
            self.fullness -= 10
            House.coat_year += 1
        else:
            self.happy -= 20
            self.fullness -= 10
            # cprint('{} хочет шубу, но нет денег!'.format(self.name), color='red')

    def clean_house(self):
        """ метод уборка в доме"""
        if self.house.mud > 100:
            # cprint('{} прибралась дома'.format(self.name), color='blue')
            self.house.mud -= 100
            self.fullness -= 20
        else:
            self.happy += 10
            # cprint('{} в доме чисто.'.format(self.name), color='blue')


class Child(Man):

    def act(self):
        """метод активности человека"""
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        else:
            self.sleep()

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            self.fullness += 10
            House.food_year += 10
            self.happy = 100
            self.house.food -= 10
            # cprint('{} поел(а)'.format(self.name), color='yellow')
        else:
            self.fullness -= 10
            # cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        """ метод ребенок спит """
        # cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        # return 'Я - {}, сытость {}'.format(self.name, self.fullness)
        pass

    def eat(self):
        """ метод еда кота"""
        if self.house.cat_food >= 10:
            # cprint('{} поел'.format(self.name), color='yellow')
            portion = randint(5, 11)
            self.house.cat_food -= portion
            self.fullness += portion * 2
        else:
            self.fullness -= 10
            # cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        """ метод кот спит """
        # cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def play_wallpapper(self):
        """ метод кот играет """
        # cprint('{} драл обои целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.house.mud += 5

    def cat_act(self):
        """ метод выбора активностей кота"""
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif self.fullness > 50:
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
            # cprint('{} умер(ла)...'.format(self.name), color='red')
            return True
        else:
            return False


class Simulation:
    """ класс симуляции"""
    cats = []

    # TODO что класс должен принимать на вход ?
    def __init__(self, name):
        self.name = name
        # TODO все объекты нужно инициализировать тут
        self.house = None
        self.husband = None
        self.wife = None
        self.children = None
        # TODO эта переменная дублируется
        self.cats = None

    #
    # def __str__(self):
    #     # return 'Прошел год, все выжили. Зарплата {} '.format(salary)
    #     pass

    # TODO метод пересоздания нужно будет пересоздать все экземпляры заново
    def new_family(self, house, husband, wife, children):
        """ создание новой семьи, при каждом вызове метода обнуляем данные"""
        self.house = house
        self.husband = husband
        self.wife = wife
        self.children = children

    # def add_cat(self, serge, cats):
    #     """метод добавленяи котов из списка"""
    #     cat_names = ['Кот', 'Пушистик', 'Киска', 'Мохнатый ублюдок', 'Облезлый', 'Длинный хвост']
    #     cat = Cat(name=random(cat_names))  # создаем обьект из класса сат
    #     serge.go_to_the_cat_house(cat)
    #     cats.append(cat)

    # TODO без дополнительных проверок и условий, сразу ретурним True|False
    def new_year(self):
        """ Метод жизнь 1 год"""
        house = self.house
        self.husband.go_to_the_house(house=house)
        self.wife.go_to_the_house(house=house)
        self.children.go_to_the_house(house=house)
        live = False
        for day in range(1, 366):
            # cprint('================== День {} =================='.format(day), color='red')
            house.muds()
            self.husband.happys()
            self.wife.happys()
            self.husband.act()
            self.wife.act()
            self.children.act()
            if self.husband.live_dead() or self.wife.live_dead() or self.children.live_dead():
                break
            for cat in self.cats:
                cat.cat_act()
            for cat in self.cats:
                if cat.live_dead():
                    live = True
            if live:
                break
        if live is False:
            # return cprint('Кто-то умер', color='red')
            return True
        else:
            # return cprint('Все выжили', color='green')
            return False

    # TODO если вы коментируете код и он нужен отавляйте комментарии в виде TODO
    # def food_incidents(self, home):
    #     home.food //= 2
    #
    # def money_incidents(self, home):
    #     home.money //= 2

    # def salary_new(self, salary):
    #     salary += 50
    #     if salary >= 400:
    #         salary = 400
    #     return salary

    def experiments(self):
        """ метод эксперимент, 3 раза имитируем жизнь. если два раза из трех никто не умер, то эксперимент удачный"""
        lacky = 0
        for _ in range(3):
            if self.new_year():
                lacky += 1
        if lacky >= 2:
            cprint('Эксперимент удачный!', color='green')
        else:
            cprint('Эксперимент неудачный!', color='red')


# Его нужно делать в отдельном файле, скопировав тут нужные классы из 01 и написать новый класс симуляции.
# В классах семьи убрать все принты из кода и метод стр они нам не нужны, нам нужна только логика их работы!
# В классе симуляция у вас будут следующие методы, во первых инит, метод_обнуления всех объектов(создание заново)
# , метод_добавления котов (по количеству), метод запуска цикла на один год который будет возвращать TRUE
# если дойдет до конца, методы которые генерят инциденты с едой и деньгами, и сам метод эксперимент в котором
# мы будем запускать нашу симуляцию три раза!

life = Simulation(name='Идеальная семья')
life.new_family(house=House(), husband=Husband(name='Сережа'), wife=Wife(name='Маша'), children=Child(name='Коля'))
# salary = Simulation.salary_new(husband.salary)
life.experiments()

# TODO метод запуска должен быть такой
# TODO задайте вопросы что еще не хватает, код ниже вам подсказывает
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
