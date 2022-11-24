'''Упражнение 4. 
Для введенного предложения выведите статистику символ=количество. Регистр букв не учитывается. 
'''


def symbol_statistic(s: str) -> dict:
    answ = {}
    s = s.lower()
    s_set = set(s)
    for i in s_set:
        answ[i] = s.count(i)
    return answ


s = 'adW awsd asd'
print(symbol_statistic(s))
