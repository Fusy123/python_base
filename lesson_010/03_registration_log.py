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


# TODO правим нейминг подчеркиваний быть не должно ни параметра ни имени функции
def Valid(line):
    if 2 < line.count(' '):
        raise ValueError('Не хватает полей')
    name_user, email_user, age_user = line.split(' ')
    if name_user.isalpha() is False:
        raise NotNameError('Некорректное имя')
    if email_user.index('@') and email_user.index('.') is False:
        raise NotEmailError('Некорректный адрес')
    if age_user.isdigit and (10 <= int(age_user) <= 99) is False:
        raise ValueError('Некорректный возраст')
    return line


activ_valid_user = []
with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            valid_user = Valid(line)
            activ_valid_user.append(line)

        except (ValueError, NotEmailError, NotNameError) as exc:
            no_corrected_log = open('registrations_bad.log', 'a', encoding='utf8')
            no_corrected_log.write(f'в строке {line} ошибка {exc}')
            no_corrected_log.write('\n')
            no_corrected_log.close()

corrected_log = open('registrations_good.log', 'w', encoding='utf8')
# TODO переменная i за что тут отвечает?
for i in activ_valid_user:
    corrected_log.write(i + '\n')
corrected_log.close()
print('Проверка завершена!')
