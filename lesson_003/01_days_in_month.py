# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

day_month={'1':['январь', 31],
           '2':['февраль', 28],
           '3':['март', 31],
           '4':['апрель', 30],
           '5':['май', 31],
           '6':['июнь', 30],
           '7':['июль', 31],
           '8':['август', 31],
           '9':['сентябрь', 30],
           '10':['октябрь', 31],
           '11':['ноябрь', 30],
           '12':['декабрь', 31]}

if 0 > month or month>13:
    print('Вы ввели некоректный месяц!')
for day in day_month:
    if day == user_input:
        days = day_month[day]
        print(days[1])
        break

