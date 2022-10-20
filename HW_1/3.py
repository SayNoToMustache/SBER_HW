'''
Вычислите значение следующего выражения (аргументы - целые числа и вводятся с клавиатуры):
f = ...
Округлите результат до 3-х знаков после запятой, используя функцию round().

'''


#Я увидел странное описание num_vec[2]*mody, как я понял имеется в виду num_vec[2](mody)
def f(num_vec):
    numerator = num_vec[0]**5 + 7
    denominator = abs(-6) * num_vec[1]
    numerator /= denominator
    numerator = numerator ** (1./3.)
    denominator = 7 - num_vec[2]%num_vec[1]
    numerator /= denominator
    return round(numerator, 3)

str = input('Введите 3 числа через пробел: ')

vec = str.split(' ')
num_vec = []

del str

for i in vec:
    num_vec.append(int(i))
    
del vec

print(f'f({num_vec[0]}, {num_vec[1]}, {num_vec[2]}) =', f(num_vec))