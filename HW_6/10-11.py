'''Упражнение 10. 
Создать класс для часов. Должна быть возможность установить время при создании объекта. 
Также необходимо реализовать методы, с помощью которых можно добавлять по одной минуте/секунде
или по одному часу к текущему времени. Помнить, что значения минут и секунд не могут превышать 59, а часов 23.
'''


class Watch:
    def __init__(self, __hour, __minute, __sec) -> None:
        if __hour > 23 or __hour < 0:
            raise Exception("LOX")
        if __minute > 59 or __minute < 0:
            raise Exception("LOX")
        if __sec > 59 or __sec < 0:
            raise Exception("LOX")

        self.__hour = __hour
        self.__minute = __minute
        self.__sec = __sec

    def add_hour(self):
        self.__hour = (self.__hour + 1) % 24

    def add_minute(self):
        self.__minute = (self.__minute + 1) % 60

    def add_sec(self):
        self.__sec = (self.__sec + 1) % 60

    def __str__(self) -> str:
        text = ''
        if self.__hour < 10:
            text += ''.join(f'0{self.__hour}')
        else:
            text += ''.join(f'{self.__hour}')
        if self.__minute < 10:
            text += ''.join(f':0{self.__minute}')
        else:
            text += ''.join(f':{self.__hour}')
        if self.__sec < 10:
            text += ''.join(f':0{self.__sec}')
        else:
            text += ''.join(f':{self.__sec}')
        return text

    def __add__(self, other):
        new_sec = (self.__sec + other.__sec) % 60
        print(new_sec)
        new_minute = (self.__minute + other.__minute +
                      (self.__sec + other.__sec) // 60) % 60
        print(new_minute)
        new_hour = (self.__hour + other.__hour + (self.__minute +
                    other.__minute + (self.__sec + other.__sec) // 60) // 60) % 24
        print(new_hour)
        return Watch(new_hour, new_minute, new_sec)


dodo = Watch(23, 2, 4)
print(dodo)
dodo.add_hour()
print(dodo)
dodo.add_sec()
print(dodo)
dada = Watch(22, 58, 5)
didi = dada + dodo
print(didi)
