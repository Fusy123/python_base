# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
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

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(self.food, self.money, self.mud)

    def inspektion(self, money, food):
        pass



class Husband:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None


    def __str__(self):    # super().__str__(),
        return 'Я - {}, сытость {}, уровень счастья {}'.format(
            self.name, self.fullness, self.happy)

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
        elif dice == 4:
            self.gaming()
        else:
            self.work()

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            portion = randint(10, 31)
            self.fullness += portion
            self.happy += 10
            self.house.food -= 10
            cprint('{} поел(а)'.format(self.name), color='yellow')
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        """ метод работа"""
        cprint('{} сходил(а) на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        """ метод отдых"""
        cprint('{} играл(а) на приставке целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happy += 20

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


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None
        self.coat = 0

    def __str__(self):       # super().__str__(),
        return 'Я - {}, сытость {}, уровень счастья {}, у меня {} шуб'.format(
            self.name, self.fullness, self.happy, self.coat)

    def act(self):
        """метод активности человека"""
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.mud >= 90:
            self.clean_house()
        elif dice == 1:
            self.clean_house()
        elif dice == 2:
            self.eat()
        elif dice == 4:
            self.buy_fur_coat()
        else:
            self.buy_fur_coat()

    def eat(self):
        """метод поел"""
        if self.house.food >= 10:
            portion = randint(10, 31)
            self.fullness += portion
            self.happy += 10
            self.house.food -= 10
            cprint('{} поел(а)'.format(self.name), color='yellow')
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def shopping(self):
        """ метод поход в магазин"""
        if self.house.money >= 10:
            cprint('{} сходил(а) в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 10
            self.house.food += 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        """ метод поход за шубой"""
        if self.house.money >= 350:
            cprint('{} сходил(а) в магазин за шубой'.format(self.name), color='magenta')
            self.house.money -= 350
            self.happy += 60
            self.coat += 1
        else:
            cprint('{} хочет шубу, но нет денег!'.format(self.name), color='red')

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

    def live_dead(self):
        """ метод проверки на живой мертвый"""
        if self.fullness < 0 or self.happy <= 10:
            cprint('{} умер(ла)...'.format(self.name), color='red')
            return True
        else:
            return False


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')



coat = 0

serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)



for day in range(1, 365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    home.mud += 5
    if home.mud > 90:
        serge.happy -= 10
        masha.happy -= 10
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
    print('')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
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


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


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
