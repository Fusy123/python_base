# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
import textwrap
import district.central_street.house1.room1 as room1
import district.central_street.house1.room2 as room2
import district.central_street.house2.room1 as room3
import district.central_street.house2.room2 as room4
import district.soviet_street.house1.room1 as room5
import district.soviet_street.house1.room2 as room6
import district.soviet_street.house2.room1 as room7
import district.soviet_street.house2.room2 as room8

folks_list_district = []

folks_list_district.extend(room1.folks)
folks_list_district.extend(room2.folks)
folks_list_district.extend(room3.folks)
folks_list_district.extend(room4.folks)
folks_list_district.extend(room5.folks)
folks_list_district.extend(room6.folks)
folks_list_district.extend(room7.folks)
folks_list_district.extend(room8.folks)

print("На районе живут: ", textwrap.fill(', '.join(folks_list_district), width=85))

# зачет!
