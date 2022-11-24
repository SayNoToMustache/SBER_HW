'''Упражнение 2. 
Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру. 
'''


def count_amount_of_strs_with_num(s: str) -> int:
    s_split = s.split()
    answ = 0
    for _list in s_split:
        if any(i.isdigit() for i in _list):
            answ += 1
    return answ
