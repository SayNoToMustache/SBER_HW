'''Упражнение 9. 
Описать класс десятичного счётчика. Он должен обладать внутренней переменной, хранящей текущее значение,
методами повышения значения (increment) и понижения (decrement), получения текущего значения get_counter. 
Учесть, что счётчик не может опускаться ниже 0.
'''

class DCount:
    def __init__(self, k = 0):
        if k < 0:
            self.__dcount = 0
        else:
            self.__dcount = k
        
    def increment(self, k=1):
        self.__dcount += k
        
    def decrement(self, k=1):
        if self.__dcount < k:
            self.__dcount -= 0
            print('Слишком много отнимаешь')
        else:
            self.__dcount -= k
        
    def get_counter(self):
        return self.__dcount
    
d = DCount(-1)
print(d.get_counter())
d.increment(5)
d.decrement(6)
print(d.get_counter())