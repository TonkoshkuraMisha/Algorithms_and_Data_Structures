# Связанные списки.
a = [1]

a.append([2])

a[1].append([3, None])

p = a

while p is not None:
    print(p[0])
    p = p[1]

a = [0, a]
print(a)


# Создаём класс односвязного списка.

class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not  None, "List empty!"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x

a = LinkedList()
a.insert(5)
a.insert(10)
a.insert(18)


print(a.pop())
print(a.pop())
print(a.pop())
#print(a.pop()) # Выведет сообщение: "List empty!"