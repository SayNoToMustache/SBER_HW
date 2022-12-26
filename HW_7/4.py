'''Упражнение 4 (Задача просто на классы, без обработки исключений).
Для одной задачи необходимо реализовать следующее - при соединении двух элементов получается новый. 
У нас есть 4 базовых элемента: Вода, Воздух, Огонь, Земля. Из них как раз и получаются новые: Шторм, Пар, Грязь, Молния, Пыль, Лава.
Вот таблица преобразований:
  Вода + Воздух = Шторм
  Вода + Огонь = Пар
  Вода + Земля = Грязь
  Воздух + Огонь = Молния
  Воздух + Земля = Пыль
  Огонь + Земля = Лава

Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс. 
Если результат не определен - то возвращается None.
'''


class BaseElement:
    def __init__(self) -> None:
        self.name = ''

    def __str__(self) -> str:
        return self.name

    def __add__(self, other):

        if type(self) == Water or type(other) == Water:
            if type(other) == Air or type(self) == Air:
                return Storm()
            if type(other) == Fire or type(self) == Fire:
                return Steam()
            if type(other) == Earth or type(self) == Earth:
                return Mud()
        if type(self) == Air or type(other) == Air:
            if type(other) == Fire or type(self) == Fire:
                return Light()
            if type(other) == Earth or type(self) == Earth:
                return Dust()
        if type(self) == Fire or type(other) == Fire:
            if type(self) == Earth or type(other) == Earth:
                return Lave()
        if type(self) == Storm or type(other) == Storm:
            if type(self) == Dust or type(other) == Dust:
                return DustStorm()


class Water(BaseElement):
    def __init__(self) -> None:
        self.name = "Вода"


class Fire(BaseElement):
    def __init__(self) -> None:
        self.name = "Огонь"


class Earth(BaseElement):
    def __init__(self) -> None:
        self.name = "Земля"


class Air(BaseElement):
    def __init__(self) -> None:
        self.name = "Воздух"


class Storm(BaseElement):
    def __init__(self) -> None:
        self.name = "Шторм"


class Steam(BaseElement):
    def __init__(self) -> None:
        self.name = "Пар"


class Mud(BaseElement):
    def __init__(self) -> None:
        self.name = "Грязь"


class DustStorm(BaseElement):
    def __init__(self) -> None:
        self.name = "Песчаная Буря"


class Light(BaseElement):
    def __init__(self) -> None:
        self.name = "Молния"


class Dust(BaseElement):
    def __init__(self) -> None:
        self.name = "Пыль"


class Lave(BaseElement):
    def __init__(self) -> None:
        self.name = "Лава"


w = Water()
a = Air()
d = Dust()
f = Fire()
e = Earth()
fe = f + e
print(fe)
ds = a + w + d
print(ds)
