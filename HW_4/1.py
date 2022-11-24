'''Упражнение 1.  
Дан список из чисел. 
Определите их НОК (наименьшее общее кратное) и НОД (наибольший общий делитель). 
'''


def gcd(a: int, b: int) -> int:
    a_max = max(a, b)
    b_min = min(a, b)
    while b_min != 0:
        a_max -= b_min
        if a_max < b_min:
            temp = a_max
            a_max = b_min
            b_min = temp
    return a_max


def lcm(a: int, b: int) -> int:
    # |ab|/gcd(a,b)
    return a*b//gcd(a, b)
