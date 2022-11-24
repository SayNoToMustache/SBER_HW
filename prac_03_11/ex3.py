'''Упражнение 3. Григорианский календарь в порядковый
Порядковая дата содержит номер года и порядковый номер дня в этом году – оба в целочисленном формате. При этом 
год может быть любым согласно григорианскому календарю, а номер дня – числом в интервале от 1 до 366 (чтобы учесть
високосные годы). Порядковые даты удобно использовать при расчете разницы в днях, когда счет ведется именно в днях,
а не месяцах. Например, это может касаться 90-дневного периода возврата товара для покупателей, расчета срока 
годности товаров или прогнозируемой даты появления малыша на свет.
Напишите функцию с именем ordinalDate, принимающую на вход три целых числа: день, месяц и год. 
Функция должна возвращать порядковый номер заданного дня в указанном году. В основной программе у пользователя должны запрашиваться день,
месяц и год соответственно и выводиться на экран порядковый номер дня в заданном году.
'''

# index_data = (index_year:int, day_number:int), day = 1 to 366

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_bis_sextus(_year) -> bool:
    """
    Args:
        _year (int)

    Returns:
        bool: if _year is bis sextus year return true else false
    """
    if _year % 400 == 0:
        return True
    elif _year % 100 == 0:
        return False
    elif _year % 4 == 0:
        return True
    else:
        return False


def ordinalDate(day: int, month: int, year: int) -> int:
    """ordinal data by grigorian

    Args:
        day (int): by grigorian
        month (int): by grigorian
        year (int): by grigorian

    Returns:
        int: ord
    """

    if month > 12 or month < 0:
        #print('Введите нормальный месяц')
        return -1
    if day > DAYS_IN_MONTH[month-1] and day < 0:
        #print('Введите нормальный день')
        return -1

    if is_bis_sextus(year):
        DAYS_IN_MONTH[1] = 29

    return sum(DAYS_IN_MONTH[:month-1])+day


if __name__ == "__main__":
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    ordDate = ordinalDate(day, month, year)
    if day < 10:
        day = '0' + str(day)
    if month < 10:
        month = '0' + str(month)
    _text = '\nДата по Григорианскому календар:\n  {day}:{month}:{year}\nПорядковая дата:\n  {ordDate}'
    print(_text.format(day=day, year=year, month=month,
                       ordDate=ordDate))
