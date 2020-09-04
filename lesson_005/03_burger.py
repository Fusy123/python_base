# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger as mb

print('Добрый день. Давайте приготовим ваш любимый бургер!')
print('Выберите нужный компонент')

# вывод соответствия номера - компоненту
for ingredient in enumerate(mb.components):
    print(ingredient[0], ": ", ingredient[1][1])

# выбор компонента и проверка правильности ввода
user_burgers = []
while True:
    user_input = input('Что добавим? : ')
    if user_input.isdigit():
        user_input = int(user_input)
        if 0 <= user_input <= 10:
            user_burgers.append(mb.components[user_input][1])
            mb.components[user_input][2]()
        elif user_input == 11:
            print("Ваш бургер: ", ', '.join(user_burgers))
            break
        else:
            print('У нас нет такого продукта!')
    else:
        print('Введите корректное значение')

# зачет!
