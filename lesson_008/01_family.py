# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


#  ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


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
        if self.cat_food is False:
            return 'В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(
                self.food, self.money, self.mud)
        else:
            return 'В доме еды осталось {}, денег осталось {}.\nВ доме осталось кошачей еды {}, уровень грязи {}'.format(
                self.food, self.money, self.cat_food, self.mud)

    def muds(self):
        """добавляем грязь в дом"""
        self.mud += 5

    def food_incidents(self):
        self.food //= 2

    def money_incidents(self):
        self.money //= 2


class Man:
    """ класс человек"""

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}, уровень счастья {}'.format(self.name, self.fullness, self.happy)

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            portion = randint(10, 31)
            self.fullness += portion
            House.food_year += portion
            self.happy += 10
            self.house.food -= 10
            cprint('{} съел {} единиц еды '.format(self.name, portion), color='yellow')
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def go_to_the_house(self, house):
        """ метод заселение в дом """
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал(а) в дом'.format(self.name), color='cyan')

    def live_dead(self):
        """ метод проверки на живой мертвый"""
        if self.fullness < 0 or self.happy <= 10:
            cprint('{} умер(ла)...'.format(self.name), color='red')
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
            cprint('Взяли {}'.format(cat.name), color='cyan')
            self.house.cat_food = 30

    def pet_the_cat(self):
        """ гладим кота"""
        cprint('{} гладил(а) кота'.format(self.name), color='green')
        self.happy += 5


class Husband(Man):
    """ класс муж"""

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
        cprint('{} сходил на работу'.format(self.name), color='blue')
        salary = randint(50, 401)
        self.house.money += salary
        self.fullness -= 10
        House.money_year += salary

    def gaming(self):
        """ метод отдых"""
        cprint('{} играл на приставке целый день'.format(self.name), color='green')
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
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            sale = randint(30, 61)
            self.house.money -= sale
            self.house.food += sale
            self.fullness -= 10
        else:
            self.fullness -= 10
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shop_food_the_cat(self):
        """ метод поход в магазин за едой для кота"""
        if self.house.money >= 20 * len(cats):
            cprint('{} сходила в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.cat_food += len(cats) * 20
            self.house.money -= len(cats) * 20
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        """ метод поход за шубой"""
        if self.house.money > 400:
            cprint('{} сходила в магазин за шубой'.format(self.name), color='magenta')
            self.house.money -= 350
            self.happy += 60
            self.fullness -= 10
            House.coat_year += 1
        else:
            self.happy -= 20
            self.fullness -= 10
            cprint('{} хочет шубу, но нет денег!'.format(self.name), color='red')

    def clean_house(self):
        """ метод уборка в доме"""
        if self.house.mud > 100:
            cprint('{} прибралась дома'.format(self.name), color='blue')
            self.house.mud -= 100
            self.fullness -= 20
        else:
            self.happy += 10
            cprint('{} в доме чисто.'.format(self.name), color='blue')


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
            cprint('{} поел(а)'.format(self.name), color='yellow')
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        """ метод ребенок спит """
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        """ метод еда кота"""
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            portion = randint(5, 11)
            self.house.cat_food -= portion
            self.fullness += portion * 2
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        """ метод кот спит """
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def play_wallpapper(self):
        """ метод кот играет """
        cprint('{} драл обои целый день'.format(self.name), color='green')
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
            cprint('{} умер(ла)...'.format(self.name), color='red')
            return True
        else:
            return False


cat_names = ['Кот', 'Пушистик']  # , 'Киска' ,'Мохнатый ублюдок', 'Облезлый', 'Длинный хвост'
cats = []

home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')

serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
kolya.go_to_the_house(house=home)

for name in cat_names:
    cat = Cat(name=name)  # создаем обьект из класса сат
    serge.go_to_the_cat_house(cat)
    cats.append(cat)

live = False

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    home.muds()
    serge.happys()
    masha.happys()
    serge.act()
    masha.act()
    kolya.act()
    if serge.live_dead() or masha.live_dead() or kolya.live_dead():
        break
    for cat in cats:
        cat.cat_act()
    for cat in cats:
        if cat.live_dead():
            live = True
    if live:
        break
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    for cat in cats:
        cprint(cat, color='cyan')
    cprint(home, color='cyan')
    print('')
    # incidents = randint(1, 11)
    # if incidents == 2:
    #     home.food_incidents()
    #     cprint('В доме пропала еда! ', color='red')
    #     print('')
    # elif incidents == 9:
    #     home.money_incidents()
    #     cprint('В доме пропали деньги! ', color='red')
    #     print('')

cprint('За год заработано денег: {} монгольских тугриков. съедено еды: {} единиц, куплено шуб: {}'.format(
    House.money_year, House.food_year, House.coat_year), color='green')

#   ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         """метод активности человека"""
#         dice = randint(1, 6)
#         if self.fullness <= 20:
#             self.eat()
#         elif self.house.money <= 50:
#             self.work()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.eat()
#         elif dice == 4:
#             self.gaming()
#         else:
#             self.work()
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


print('')

#  ####################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)
#
# class Child(Man):
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     # def act(self):
#     #     """метод активности человека"""
#     #     dice = randint(1, 6)
#     #     if self.fullness <= 20:
#     #         self.eat()
#     #
#     #     else:
#     #         self.buy_fur_coat()
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass

#   ####################################################### Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
print('')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
