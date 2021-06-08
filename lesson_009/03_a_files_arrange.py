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


# TODO усложненная версия

import os
import zipfile


class Sortetd:
    """сортировка файлов по папкам в формате /год/месяц"""

    def __init__(self, start, finish):
        self.src_file = start
        self.dst_path = finish
        self.src_file_zip = None

    def norm_path(self):
        """нормализация пути"""
        src_norm_path_file = os.path.abspath(self.src_file)
        dst_norm_path = os.path.abspath(self.dst_path)
        self._collect(src=src_norm_path_file, dst=dst_norm_path)

    def _collect(self, src, dst):
        """ метод проверки типа файла: если zip то вызвать метод распаковки"""
        if src.endswith('.zip'):
            self.src_file_zip = zipfile.ZipFile(src, 'r')
            self._sorted_in_zip(self.src_file_zip, dst)
        else:
            print('Это не файл в формате zip!!')

    def _sorted_in_zip(self, src, dst):
        """метод проверки файла на дату создания и распаковки в нужную папку год/месяц"""
        for file in src.namelist():
            file_time = src.getinfo(file).date_time
            path_year = str(file_time[0])
            path_month = str(file_time[1])
            if file[-1] == '/':
                continue
            file_name = os.path.basename(file)
            finish_folder_path = os.path.normpath(os.path.join(dst, path_year, path_month))
            os.makedirs(finish_folder_path, exist_ok=True)
            finish_file_path = os.path.normpath(os.path.join(finish_folder_path, file_name))
            data_file_zip = self.src_file_zip.read(file)
            dst_file = open(finish_file_path, 'wb')
            dst_file.write(data_file_zip)
            dst_file.close()



start_file = 'icons.zip'
finish_folder = 'icons_by_year'

sorter_file = Sortetd(start_file, finish_folder)
sorter_file.norm_path()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
