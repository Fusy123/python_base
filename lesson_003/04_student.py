# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме
educational_grant, expenses = 10000, 12000
# TODO Нейминг переменных, никакого транслита
# TODO Используйте например https://multitran.com
dolg_1 = expenses-educational_grant
# TODO Нейминг Это наверное месяц
a = 1
dolg_2 = 0
while a<10:
    # TODO округление лучше производить перед вывод и после вычислений всех, теряется точность
    expenses += round(expenses*0.03, 2)
    dolg_2 += round(expenses-educational_grant, 2)
    a += 1
# TODO Все вычисления и преобразования лучше выполнять до, а в принте выводить эту переменную
print('Студенту надо попросить', dolg_1 + dolg_2, 'рублей')

