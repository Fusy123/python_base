# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import zipfile
import os



class Log_parser:
    """ класс подсчета символов в файле. """

    def __init__(self, file_name, time1, date1):
        self.file_name = file_name
        self.time_analiz = time1
        self.date_analiz = date1
        self.statistic_log = {}
        self.start_log = {}
        self.hours_log = {}
        self.date = ' '
        self.time = ' '
        self.blok = 'NOK'

    def unzip(self):
        """ метод распаковки файла из архива """
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        """ метод проверки типа файла: если zip то вызвать метод распаковки"""
        if self.file_name.endswith('.zip'):  # если файл в формате зип, происходит  вызов метода распаковки
            self.unzip()
        with open(self.file_name, 'r', encoding='utf8') as file:  # читаем файл построчно
            for line in file:
                line = line[1:-1]
                line = line.replace(']', '')
                self._first_analiz(line=line)  # отбрасываем символ перевода каретки

    def _first_analiz(self, line):
        """ анализируем строку на вхождение NOK"""
        self.start_log = line.split(' ')
        # time1 = ''.join(['self.start_log', self.time_analiz])
        # date1 = ''.join(['self.start_log', self.date_analiz])
        time = eval(''.join(['self.start_log', self.time_analiz]))
        date = eval(''.join(['self.start_log', self.date_analiz]))
        if self.blok in self.start_log:
            if self.date in self.statistic_log:
                if self.time in self.statistic_log[self.date]:
                    self.statistic_log[self.date][self.time] += 1
                else:
                    self.statistic_log[self.date][self.time] = 1
            else:
                self.statistic_log[date] = {time: 1}
        else:
            self.date = date
            self.time = time

    def finish(self, out_file_name=None):
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None

        file.write('{txt:^12}{txt2:^7}'.format(txt="Дата", txt2="Время"))
        file.write('\n')
        for dates, time in self.statistic_log.items():
            for key, value in time.items():
                file.write('[ {} {} ] {}'.format(dates, key, value))
                file.write('\n')
        if file:
            file.close()


date_time = '[0]'  # при парсинге часов-минут передаем это значение
time_min = '[1][0:5]'   # при парсинге по минутам
time_hours = '[1][0:3]'   # при парсинге по часам

time_date = '[1][0:0]'  # при парсинге по дате передаем это значение часов-минут
time_day = '[0][0:10]'   # при парсинге по дням
time_month = '[0][0:7]'   # при парсинге по месяцу
time_year = '[0][0:4]'    # при парсинге по году

path = 'C:\!disk_D\python_kursy\project\python_base\events.txt'
path_norm = os.path.normpath(path)

''' парсинг по количеству NOK  в минуту'''
loging = Log_parser(file_name=path_norm, time1=time_date, date1=time_day)
loging.collect()
loging.finish(out_file_name='log_NOK.txt')
# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
