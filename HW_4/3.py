'''Упражнение 3. 
Дана строка s и символ k. Реализуйте функцию, рисующую рамку из символа k вокруг данной строки, например: 
 
********** 
*Текст в рамке* 
********** 
'''


def text_frame(s: str, k: str) -> str:
    if len(k) > 1:
        print('it\'s not a char')
        return -1
    answ = (len(s)+2) * k
    answ += '\n'+k + s + k+'\n'
    answ += (len(s)+2) * k
    return answ


print(text_frame('lol it\'s working', '+'))
