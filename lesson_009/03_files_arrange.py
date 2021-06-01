# -*- coding: utf-8 -*-
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
import shutil


class Sortetd:
    """сортировка файлов по папкам в формате /год/месяц"""

    def __init__(self, start, finish):
        self.start_path = start
        self.finish_path = finish

    def norm_path(self):
        """нормализация пути"""
        start_norm_path = os.path.abspath(self.start_path)
        finish_norm_path = os.path.abspath(self.finish_path)
        self._transfer_file(start=start_norm_path, finish=finish_norm_path)

    def _transfer_file(self, start, finish):
        """модуль сортировки переноса файлов по папкам"""
        for dir_path, dir_names, file_names in os.walk(start):
            for file in file_names:
                start_file_path = os.path.join(dir_path, file)
                secs = os.path.getmtime(start_file_path)
                file_time = time.gmtime(secs)
                path_year = str(file_time[0])
                path_month = str(file_time[1])
                finish_folder_path = os.path.normpath(os.path.join(finish, path_year, path_month))
                finish_file_path = os.path.normpath(os.path.join(finish_folder_path, path_month))
                os.makedirs(finish_folder_path, exist_ok=True)
                shutil.copy2(start_file_path, finish_file_path)


start_folder = 'icons'
finish_folder = 'icons_by_year'

sorter_file = Sortetd(start_folder, finish_folder)
sorter_file.norm_path()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
