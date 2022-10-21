'''
Задача 3. 
Дано слово объектно-ориентированный. Используя индексацию и срезы составьте из него слова 
объект, ориентир, тир, кот, рента и выведите их на экран.
'''

#Я так понял все нужно ручками? Без автоматизации?
#Честно не хочется считать индексы честно

# да, плнировалось именно ручками

# _str_1 = _str[:6]
# print(_str_1)

_str = 'объектно-ориентированный'

index = _str.find('т') + 1
print(_str[:index])

index = _str.find('-') + 1
index_2 = _str.rfind('о')
print(_str[index:index_2])

index = _str.rfind('т')
index_2 = _str.rfind('р') + 1
print(_str[index:index_2])

index = _str.find('к')
index_2 = _str.find('-') + 1
index_3 = _str.find('т')
print(_str[index:index+1] + _str[index_2:index_2+1] + _str[index_3:index_3+1])

index = _str.find('р')
index_2 = _str.find('а')
print(_str[index:index+1] + _str[index+2:index+5] + _str[index_2:index_2+1])
