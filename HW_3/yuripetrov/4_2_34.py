'''
Вводится список из n годовых вкладов, предлагаемых банками, в формате:
Банк Сумма Процент
где:

    все значения разделены пробелом и сами не содержат пробелов;

    наименование банка уникально;

    Сумма: сумма для открытия вклада в руб. (целое число, >0

);

Процент: годовой процент по вкладу (вещественное число, (0,100]

    ).

Сохраните введенные данные в виде списка словарей:
[
    {"name": "Банк 1", "initial_sum": 50000, "rate": 5.2},
    ...
]
Далее определите (гарантируется, что искомый банк - один):

    самый доступный банк (с наименьшей первоначальной суммой);

    самый выгодный банк, принимая, что за год прибыль = сумма * процент / 100.

При выводе финансовых значений оставьте два знака после запятой.
'''

N = int(input('Введите кол-во банков: '))
_list = []

for i in range(N):
    bank = {}
    bank["name"] = input('Введите название банка: ')
    bank["initial_sum"] = int(input('Введите сумму: '))
    bank["rate"] = float(input('Введите процент: '))
    _list.append(bank)

if _list:
    min_initial_sum = _list[0]["initial_sum"]
    min_initial_sum_index = 0

    for _index, init_sum_dict in enumerate(_list):
        buf = min(min_initial_sum, init_sum_dict["initial_sum"])
        if buf != min_initial_sum:
            min_initial_sum_index = _index
            min_initial_sum = buf

print('Самый доступный банк - {}, начальный взнос = {}'.format(
    _list[min_initial_sum_index]["name"], min_initial_sum))

max_profit = _list[0]["initial_sum"]*_list[0]["rate"]/100
max_profit_index = 0

for _index, profit_dict in enumerate(_list):
    buf = max(max_profit, profit_dict["initial_sum"]*profit_dict["rate"]/100)
    if buf != max_profit:
        max_profit_index = _index
        max_profit = buf

print('Самый выгодный банк - {}, возможный профит = {:.2f}'.format(
    _list[max_profit_index]["name"], max_profit))
