# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

global cats, home, serge, masha, kolya


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

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            portion = randint(10, 31)
            self.fullness += portion
            House.food_year += portion
            self.happy += 10
            self.house.food -= 10
        else:
            self.fullness -= 10

    def go_to_the_house(self, house):
        """ метод заселение в дом """
        self.house = house
        self.fullness -= 10

    def live_dead(self):
        """ метод проверки на живой мертвый"""
        if self.fullness < 0 or self.happy <= 10:
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
            self.house.cat_food = 30

    def pet_the_cat(self):
        """ гладим кота"""
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
        self.salary = salary
        self.house.money += self.salary
        self.fullness -= 10
        House.money_year += self.salary

    def gaming(self):
        """ метод отдых"""
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
            sale = randint(30, 61)
            self.house.money -= sale
            self.house.food += sale
            self.fullness -= 10
        else:
            self.fullness -= 10

    def shop_food_the_cat(self):
        """ метод поход в магазин за едой для кота"""
        if self.house.money >= 20 * len(cats):
            self.house.cat_food += len(cats) * 20
            self.house.money -= len(cats) * 20

    def buy_fur_coat(self):
        """ метод поход за шубой"""
        if self.house.money > 400:
            self.house.money -= 350
            self.happy += 60
            self.fullness -= 10
            House.coat_year += 1
        else:
            self.happy -= 20
            self.fullness -= 10

    def clean_house(self):
        """ метод уборка в доме"""
        if self.house.mud > 100:
            self.house.mud -= 100
            self.fullness -= 20
        else:
            self.happy += 10


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
        else:
            self.fullness -= 10

    def sleep(self):
        """ метод ребенок спит """
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def eat(self):
        """ метод еда кота"""
        if self.house.cat_food >= 10:
            portion = randint(5, 11)
            self.house.cat_food -= portion
            self.fullness += portion * 2
        else:
            self.fullness -= 10

    def sleep(self):
        """ метод кот спит """
        self.fullness -= 10

    def play_wallpapper(self):
        """ метод кот играет """
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
            return True
        else:
            return False

class Family(Husband, Wife, Child, House):
    """класс создания семьи"""

    def __init__(self):
        self.serge = Husband(name='Сережа')
        self.masha = Wife(name='Маша')
        self.kolya = Child(name='Коля')
        self.house = House()

    def occupation_house(self):
        """ метод заселения в дом"""
        self.house = home
        serge.go_to_the_house(house=home)
        masha.go_to_the_house(house=home)
        kolya.go_to_the_house(house=home)


class Simulation:
    """ класс симуляции"""

    #  принимаем только money_incidents, food_incidents но они не должны быть подчеркнуты
    def __init__(self):
        self.money_incidents = None
        self.food_incidents = None
        self.cats = None


    def new_family(self):
        """ создание новой семьи, при каждом вызове метода обнуляем данные"""
        self.cats = []
        self.money_incidents = []
        self.food_incidents = []
        #  сразу написать классы так чтобы можно было через атрибут передать экземпляр дом
        Family.occupation_house()


    def add_cat(self, count):
        """метод добавления котов из списка"""
        cat_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        for i in range(count):
            cat = Cat(name=random(cat_names))  # создаем обьект из класса сат
            serge.go_to_the_cat_house(cat)
            cats.append(cat)

    #  нужно написать два метода которые будут фомировать два одноименных списка с датами
    #  по которым мы будем потом проходиться и подрезать ресурсы

    def money_incident(self, count_money_incident):
        """формируем список дат когда произойдет инцидент с пропажей монет"""
        for _ in range(count_money_incident):
            self.money_incidents.append(randint(1, 366))
        self.money_incidents = sorted(self.money_incidents)

    def food_incident(self, count_food_incident):
        """формируем список дат когда произойдет инцидент с пропажей еды"""
        for _ in range(count_food_incident):
            self.food_incidents.append(randint(1, 365))
        self.food_incidents = sorted(self.food_incidents)


    #  без дополнительных проверок и условий, сразу ретурним True|False
    def new_year(self):
        """ Метод жизнь 1 год"""
        for day in range(1, 366):
            # cprint('================== День {} =================='.format(day), color='red')
            home.muds()
            serge.happys()
            masha.happys()
            serge.act()
            masha.act()
            kolya.act()
            for cat in cats:
                cat.cat_act()
                if cat.live_dead():
                    return True
            if serge.live_dead() or masha.live_dead() or kolya.live_dead():
                return True
            else:
                return False

    #  заводим цикл по количеству котов от 10 до 0 с шагом -1  +
    #  объявляем переменную которая будет отвечать за верификацию +
    #  заводим цикл по range(3) +
    #  обнуляемся - пересоздаем экземпляры +
    #  передаем ЗП +
    #  создаем нужное количество котов +
    #  генерим инциденты +
    #  условие запускаем цикл, если тру то +
    #  увеличиваем верификацию на 1 +
    #  вложенное условие проверяем если верификацию = 2 +
    #  то ретурним количество котов
    def experiments(self):
        """ метод эксперимент, 3 раза имитируем жизнь. если два раза из трех никто не умер, то эксперимент удачный"""
        for count_cats in range(10, 0, -1):
            lacky = 0
            for _ in range(3):
                self.new_family()
                for salary in range(50, 401, 50):
                    self.add_cat(count_cats)
                    for food_incidents in range(6):
                        for money_incidents in range(6):
                            life = Simulation(money_incidents, food_incidents)
                            life.new_family()

                        if self.new_year():
                            lacky += 1
                        if lacky >= 2:
                            cprint('Эксперимент удачный!', color='green')
                            print(f'При зарплате {salary} максимально можно прокормить {count_cats} котов')
                        else:
                            cprint('Эксперимент неудачный!', color='red')


# Его нужно делать в отдельном файле, скопировав тут нужные классы из 01 и написать новый класс симуляции.
# В классах семьи убрать все принты из кода и метод стр они нам не нужны, нам нужна только логика их работы!
# В классе симуляция у вас будут следующие методы, во первых инит, метод_обнуления всех объектов(создание заново)
# , метод_добавления котов (по количеству), метод запуска цикла на один год который будет возвращать TRUE
# если дойдет до конца, методы которые генерят инциденты с едой и деньгами, и сам метод эксперимент в котором
# мы будем запускать нашу симуляцию три раза!

for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            life.new_family()
            max_cats = life.experiments(salary)
            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
