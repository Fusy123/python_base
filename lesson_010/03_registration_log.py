# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotEmailError(NameError):
    pass


class NotNameError(NameError):
    pass


# TODO применить рекомендации данные ранее в 02
def Valid(line):
    if 2 < line.count(' '):
        raise ValueError('Не хватает полей')
    nameuser, emailuser, ageuser = line.split(' ')
    if nameuser.isalpha() is False:
        raise NotNameError('Некорректное имя')
    if emailuser.index('@') and emailuser.index('.') is False:
        raise NotEmailError('Некорректный адрес')
    if ageuser.isdigit and (10 <= int(ageuser) <= 99) is False:
        raise ValueError('Некорректный возраст')
    return line


activvaliduser = []
with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            validuser = Valid(line)
            activvaliduser.append(line)

        except (ValueError, NotEmailError, NotNameError) as exc:
            nocorrectedlog = open('registrations_bad.log', 'a', encoding='utf8')
            nocorrectedlog.write(f'в строке {line} ошибка {exc}')
            nocorrectedlog.write('\n')
            nocorrectedlog.close()

correctedlog = open('registrations_good.log', 'w', encoding='utf8')
# переменная i за что тут отвечает?
# TODO за построчную запись данных из списка в файл
for i in activvaliduser:
    correctedlog.write(i + '\n')
correctedlog.close()
print('Проверка завершена!')
