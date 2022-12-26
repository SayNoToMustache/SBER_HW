class Stack(list):
    def __init__(self):
        super().__init__()
        self._list = []

    def push(self, what):
        self._list.append(what)

    def pop(self):
        return self._list.pop()

class StackTeacher:
    def __init__(self):
        self.__stack = list()

    def __str__(self):
        return '; '.join(self.__stack)

    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop()

    def push(self, item):
        self.__stack.append(item)

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]

st = Stack()

st.push(2)
st.push(3)

answ = st.pop()
answ += st.pop()

print(answ)

st.push(4)
st.push('*')

answ = st.pop()*st.pop()

print(answ)
