# -*- coding: utf-8 -*-

import os
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import os
import time

# TODO задание переписать в объектном стиле ООП

# TODO возвращает абсолютный путь и уже его нормализует по сути второй вызов normpath был не нужен
# что делает функция abspath ? возвращает абсолютный путь
# TODO тогда все пути формируем через os.path.join
# TODO мы выходим ../ а потом заходим в lesson_009/
# TODO чтобы получить корень запуска абсолютный путь можно воспользоваться
# TODO os.path.abspath(__file__)
# TODO потом применить os.path.join()  добавить имя файла и папки

start_path = '../lesson_009/icons'
finish_path = '../lesson_009/icons_by_year'
# что делает функция normpath ? убирает лишние знаки и производит замену \ /
start_norm_path = os.path.normpath(start_path)
finish_norm_path = os.path.normpath(finish_path)
for dir_path, dir_names, file_names in os.walk(start_norm_path):
    for file in file_names:
        start_file_path = os.path.join(dir_path, file)
        secs = os.path.getmtime(start_file_path)
        file_time = time.gmtime(secs)
        path_year = str(file_time[0])
        path_month = str(file_time[1])
        finish_file_path = os.path.join(finish_norm_path, path_year, path_month, file)
        # TODO используем не перенос а копирование через shutil.copy2

        # TODO логика может быть такой
        # TODO мы проверяем если такой путь если его нет то создаем в одну команду
        # TODO используем методы у os.path.
        if os.path.dirname(finish_file_path):
            os.renames(start_file_path, finish_file_path)
        else:
            os.makedirs(os.path.dirname(finish_file_path), mode=True)
            os.renames(start_file_path, finish_file_path)

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
