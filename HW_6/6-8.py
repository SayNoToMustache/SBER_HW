'''Упражнение 6. 
Создайте класс Point, экземпляры которого будут создаваться из координат x и y.

Упражнение 7. 
Создайте класс прямоугольник — Rectangle. Метод __init__ принимает две точки — левый нижний и правый верхний угол. 
Каждая точка представлена экземпляром класса Point. Реализуйте методы вычисления площади и периметра прямоугольника.

Упражнение 8. 
Добавьте в класс Rectangle метод contains. Метод принимает точку и возвращает True, если точка находится внутри прямоугольника 
и False в противном случае.
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        if self.x > other.x or self.y > other.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point_1, point_2) -> None:
        if point_1 > point_2:
            buf = point_1
            point_1 = point_2
            point_2 = buf

        self.point_1 = point_1
        self.point_2 = point_2

    def __str__(self) -> str:
        return f"left [{self.point_1.x}; {self.point_1.y}], right [{self.point_2.x}; {self.point_2.y}]"

    def perimeter(self):
        return (self.point_2.x - self.point_1.x) * (self.point_2.y - self.point_1.y)

    def contains(self, point):
        if self.point_1.x < point.x and self.point_2.x > point.x:
            if self.point_1.y < point.y and self.point_2.y > point.y:
                return True

        return False


p1 = Point(2, 3)
p2 = Point(3, 6)
rec = Rectangle(p1, p2)

print(rec)
print(rec.perimeter())
print(rec.contains(Point(2.5, 4)))  # True
print(rec.contains(Point(2.5, 7)))  # False
