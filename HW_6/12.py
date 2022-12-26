'''Упражнение 12. 
Создать классы для травоядного животного и травы. Животное должно уметь поедать траву, 
если испытывает голод, в противном случае отказываться от лакомства. 
Трава должна обладать питательностью, в зависимости от которой животное будет насыщаться.
'''


class Grass:
    def __init__(self, nutritional_value, population=2) -> None:
        self.nutritional_value = nutritional_value
        self.population = population


class Animal:
    def __init__(self) -> None:
        self.__hunger = 10

    def __str__(self) -> str:
        if self.__hunger <= 0:
            return f"Press F"
        if self.__hunger < 5:
            return f"Очень хочется кушать, я сыто на {self.__hunger * 10}%"
        else:
            return f"Ну я еще не голодно, сыто на {self.__hunger * 10}%"

    def new_day(self, grass):
        self.__hunger -= 1
        print(self)
        self.feed(grass)

    def feed(self, grass):
        if self.__hunger < 5 and grass.population > 0:
            self.__hunger += grass.nutritional_value
            grass.population -= 1


anima = Animal()
grass = Grass(2)
for i in range(15):
    anima.new_day(grass)
