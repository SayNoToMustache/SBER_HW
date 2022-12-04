'''Упражнение 2.
Ханойские башни
переложить с 1 на 3
'''


class HanoiTower:
    def __init__(self, disks) -> None:
        self.first = self.__add_it(disks)
        self.second = []
        self.third = []
        self._dist = len(self.first)

    def __add_it(self, disks) -> list:
        return [i for i in range(1, disks+1)]

    def move(self, start, end):
        if start == 1:
            last_start = self.first.pop(0)
        if start == 2:
            last_start = self.second.pop(0)
        if start == 3:
            last_start = self.third.pop(0)
        if end == 1:
            self.first.append(last_start)
            self.first.sort()
        if end == 2:
            self.second.append(last_start)
            self.second.sort()
        if end == 3:
            self.third.append(last_start)
            self.third.sort()

    def play_tower_of_hanoi(self, amount, start, another, end):
        if (amount == 1):
            self.move(start, end)
            print(self)
            return None
        self.play_tower_of_hanoi(amount - 1, start, end, another)
        self.move(start, end)
        print(self)
        self.play_tower_of_hanoi(amount - 1, another, start, end)

    def __str__(self) -> str:
        longest = self._dist
        text = ''
        for i in range(0, longest):
            if len(self.first) > i:
                text += self.first[i]*'*' + (longest - self.first[i] + 1)*' '
            else:
                text += longest*'-' + ' '
            if len(self.second) > i:
                text += self.second[i]*'*' + (longest - self.second[i] + 1)*' '
            else:
                text += longest*'-' + ' '
            if len(self.third) > i:
                text += self.third[i]*'*' + (longest - self.third[i] + 1)*' '
            else:
                text += longest*'-' + ' '
            text += '\n'
        return text


if __name__ == "__main__":
    N = int(input('Введите кол-во дисков'))

    def play_tower_of_hanoi(amount, start, another, end):
        if amount == 1:
            print(f'1 {start} {end}')
            return None
        play_tower_of_hanoi(amount - 1, start, end, another)
        print(f'{amount} {start} {end}')
        play_tower_of_hanoi(amount - 1, another, start, end)

    play_tower_of_hanoi(N, 1, 2, 3)
else:
    N = int(input('Введите кол-во дисков'))
    a = HanoiTower(N)
    a.play_tower_of_hanoi(N, 1, 2, 3)
