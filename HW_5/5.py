'''Упражнение 5.
Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
Операцией возведения в степень пользоваться нельзя!
'''

N = list(str(bin(int(input('введите N: ')))))
amount_of_1 = N.count('1')

if amount_of_1 < 2:
    print('Yes')
else:
    print('No')
