'''Упражнение 10. 
 
Магическими называются даты, в которых произведение дня и месяца составляет последние две цифры года. 
Например, 10 июня 1960 года – магическая дата, поскольку 10 * 6 = 60. Напишите функцию, определяющую, 
является ли введенная дата магической. Используйте написанную функцию в главной программе для отображения 
всех магических дат в XX ве­ке. 
'''
import sys
sys.path.insert(0, 'prac_03_11')
from ex3 import is_bis_sextus as ibs
from ex3 import DAYS_IN_MONTH

DIM = DAYS_IN_MONTH.copy()
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def is_magic_date(s):
    months = MONTHS.copy()
    day, month, year = tuple(s.split())
    mb_year = int(day)*(months.index(month)+1)
    if mb_year == int(year[-2:]):
        return True
    return False

#Пример
#print(is_magic_date('10 jun 1960'))

#XX век это 1901 по 2000
for year in range(1901, 2000-1):
    if ibs(year):
        DIM[1] = 29
    else:
        DIM[1] = DAYS_IN_MONTH[1]
    for number, month in enumerate(MONTHS):
        for days in range(1, DIM[number]+1):
            buf = ' '.join([str(days), str(month), str(year)])
            if is_magic_date(buf):
                print(buf)
