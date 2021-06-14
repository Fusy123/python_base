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


# когда мы получили его нужно распаковать на переменные name email age
# TODO у меня так и сделано
# у вас будем всего 4 if проверки
# TODO  их и сейчас 4 проверки
# первая на то что имя не число
# TODO первая проверяет, что у меня в строке 3 обьекта разделенных пробелами
# вторая на то что валидный email
# TODO Вторая проверяет имя, что оно состоит из букв
# третья что возраст в рамках
# TODO третья проверяет email на вхождение @ и "."
# TODO  и последняя проверяет возраст на вхождение в рамки от 10 до 99
# и четверная на то что все 3 переменные не None
# TODO вот тут можно записать в список положительных логов.
def Valid(line):
    if line.count(' ') >= 2:
        name_user, email_user, age_user = line.split(' ')
        if name_user.isalpha():
            if email_user.index('@') and email_user.index('.'):
                if age_user.isdigit and (int(age_user) >= 10 and int(age_user) <= 99):
                    return line
                else:
                    raise ValueError('Некорректный возраст')
            else:
                raise NotEmailError('Некорректный адрес')
        else:
            raise NotNameError('Некорректное имя')
    else:
        raise ValueError('Не хватает полей')




list_valid_user = []
with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            valid_user = Valid(line)
            list_valid_user.append(line)

        except (ValueError, NotEmailError, NotNameError) as exc:
            no_corrected_log = open('registrations_bad.log', 'a', encoding='utf8')
            no_corrected_log.write(f'в строке {line} ошибка {exc}')
            no_corrected_log.write('\n')
            no_corrected_log.close()



corrected_log = open('registrations_good.log', 'w', encoding='utf8')
for i in list_valid_user:
    corrected_log.write(i + '\n')
corrected_log.close()
print('Проверка завершена!')
