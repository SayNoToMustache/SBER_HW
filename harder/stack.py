class Stack(list):
    def __init__(self):
        self._list = []

    def push(self, what):
        self._list.append(what)

    def pop(self):
        return self._list.pop()


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
