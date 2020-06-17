#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# Стол
table_code = goods['Стол']
table_item = store[table_code][0]
table_item1 = store[table_code][1]
tables_quantity1 = table_item['quantity']
tables_quantity2 = table_item1['quantity']
tables_price1 = table_item['price']
tables_price2 = table_item1['price']
tables_quantity=tables_quantity1+tables_quantity2
tables_cost1 =tables_quantity1 * tables_price1
tables_cost2 =tables_quantity2 * tables_price2
tables_cost=tables_cost1+tables_cost2

print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')

#диван
sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_item1 = store[sofa_code][1]
sofas_quantity1 = sofa_item['quantity']
sofas_quantity2 = sofa_item1['quantity']
sofas_price1 = sofa_item['price']
sofas_price2 = sofa_item1['price']
sofas_quantity=sofas_quantity1+sofas_quantity2
sofas_cost1 =sofas_quantity1 * sofas_price1
sofas_cost2 =sofas_quantity2 * sofas_price2
sofas_cost=sofas_cost1+sofas_cost2
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')

#стул
chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_item1 = store[chair_code][1]
chair_item2 = store[chair_code][2]
chairs_quantity1 = chair_item['quantity']
chairs_quantity2 = chair_item1['quantity']
chairs_quantity3 = chair_item2['quantity']
chairs_price1 = chair_item['price']
chairs_price2 = chair_item1['price']
chairs_price3 = chair_item2['price']
chairs_quantity=chairs_quantity1+chairs_quantity2+chairs_quantity3
chairs_cost1 =chairs_quantity1 * chairs_price1
chairs_cost2 =chairs_quantity2 * chairs_price2
chairs_cost3 =chairs_quantity3 * chairs_price3
chairs_cost=chairs_cost1+chairs_cost2+chairs_cost3
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






