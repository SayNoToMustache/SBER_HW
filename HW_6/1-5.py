'''
Упражнение 1. 
Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста. Создать экземпляр и вывести информацию о человеке.

Упражнение 2. 
Доработать предыдущий класс, чтобы вся информация о человеке была доступна при вызове str над экземпляром.

Упражнение 3. 
Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате "Привет! Меня зовут Петров Василий, мне 12 лет".

Упражнение 4. 
Добавить поле grades, в котором будет храниться список оценок. Создать список учеников, заполняя оценки каждого случайными числами.

Упражнение 5. 
Вывести информацию об учениках в порядке убывания среднего балла. Подсчёт среднего балла вынести в отдельный метод.
'''


class Man:
    def __init__(self, name, sec_n, age):
        self.name = name
        self.sec_n = sec_n
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.sec_n}: {self.age} y.o'

    def greet(self):
        print(f'Hi! me name is{self.name} {self.sec_n}, i\'m {self.age} y.o')

    def set_grade(self, grades):
        self.grades = grades

    def get_grade(self):
        return self.grades
    
    @staticmethod 
    def mean_grade(lst: list) -> int:
        sum = 0
        for i in lst:
            sum += i.get_grade()
        sum /= len(lst)
        return sum



name = 'a'
second_name = 'b'
list_man = []
for i in range(32):
    list_man.append(Man(name, second_name, i))
    grade = (i % 7 + i % 11) % 5
    list_man[i].set_grade(grade)
    name = chr(ord(name) + 1)
    second_name = chr(ord(second_name) + 1)

list_man.sort(key=lambda x: x.get_grade(), reverse=True)

for i in list_man:
    print(i, i.get_grade())



print("mean =", Man.mean_grade(list_man))
