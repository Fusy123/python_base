# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.
import zipfile
from termcolor import cprint


class Parsing:
    """ класс подсчета символов в файле. """

    def __init__(self, file_name):
        self.stat_for_generate = []
        self.totals = 0
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        """ метод распаковки файла из архива """
        zfile = zipfile.ZipFile(self.file_name, 'r')
        # TODO нейминг пишем в стиле snake_case
        for filename in zfile.namelist():
            zfile.extract(filename)
        # TODO у вас filename находиться в не области видимости
        self.file_name = filename

    def collect(self):
        """ метод проверки типа файла: если zip то вызвать метод распаковки"""
        if self.file_name.endswith('.zip'):  # если файл в формате зип, происходит вызов метода распаковки
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:  # читаем файл построчно
            for line in file:
                self._collect_for_line(line=line[:-1])  # отбрасываем символ перевода каретки

    def _collect_for_line(self, line):
        """ метод подсчета символов"""

        for char in line:
            if char in self.stat:
                if char.isalpha():
                    self.stat[char] += 1
                    self.totals += 1
            else:
                if char.isalpha():
                    self.stat[char] = 1
                    self.totals += 1

    def prepare(self):
        """ метод фильтрации по частоте использования по убыванию от большего к меньшему"""
        for char, count in self.stat.items():
            self.stat_for_generate.append([count, char])
            self.stat_for_generate.sort(reverse=True)  # утрать реверс будет по возрастанию

    def results(self, out_file_name=None):
        """ метод записи результатов в файл"""
        # если не указан файл куда записывать результат то выпадает с ошибкой
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            return cprint("Не указан файл для записи результатов", color='red')

        file.write('+{txt:^13}+{txt:^13}+'.format(txt=("-" * 13)))
        file.write('\n')
        file.write('|{txt:^13}|{txt2:^13}|'.format(txt="Буква", txt2="Частота"))
        file.write('\n')
        file.write('+{txt:^13}+{txt:^13}+'.format(txt=("-" * 13)))
        file.write('\n')
        for coint, char in self.stat_for_generate:
            file.write('|{txt:^13}|{txt2:^13}|'.format(txt=char, txt2=coint))
            file.write('\n')
            file.write('+{txt:^13}+{txt:^13}+'.format(txt=("-" * 13)))
            file.write('\n')
        file.write('|{txt:^13}|{txt2:^13}|'.format(txt="Итого", txt2=self.totals))
        file.write('\n')
        file.write('+{txt:^13}+{txt:^13}+'.format(txt=("-" * 13)))
        file.write('\n')
        if file:
            file.close()


# TODO нейминг
class Parsing_up(Parsing):
    """ метод фильтрации по частоте использования по возрастанию"""

    def prepare(self):
        super().prepare()
        self.stat_for_generate.sort()


class Parsing_A_Z(Parsing):
    """ метод фильтрации по алфавиту в прямом направлении"""

    def prepare(self):
        super().prepare()
        self.stat_for_generate.sort(key=lambda i: i[1])


class Parsing_Z_A(Parsing):
    """ метод фильтрации по алфавиту в обратном направлении"""

    def prepare(self):
        super().prepare()
        self.stat_for_generate.sort(key=lambda i: i[1], reverse=True)


filename = 'voyna-i-mir.txt.zip'

# TODO стараемся объекты не вызывать в списках или в словарях
# TODO заранее их обявить
# TODO и использовать только тот который нужен

metods = {'1': ['По убыванию', Parsing(file_name=filename)],
          '2': ['По возрастанию', Parsing_up(file_name=filename)],
          '3': ['По алфавиту от А до Я', Parsing_A_Z(file_name=filename)],
          '4': ['По алфавиту от Я до А', Parsing_Z_A(file_name=filename)],
          }

print('Выберите тип фильтрации подсчета символов в файле:', filename)
for metod in metods.items():
    print(metod[0], ':', metod[1][0])

while True:
    user_metod = input('Введите выбранный метод: ')
    if user_metod in metods.keys():
        parser = metods[user_metod][1]
        break
    else:
        print('Вы ввели неправильный номер метода!')

parser.collect()
parser.prepare()  # фильтрация по частоте букв
parser.results(out_file_name='out.txt')

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
