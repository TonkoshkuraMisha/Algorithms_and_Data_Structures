"""
Очередь FIFO. Для добавления и удаления принято использовать комманды add и remove.
Стек LIFO. Для добавления и удаления элементов принято использовать push и pop.
"""
# эффективная реализация очереди
"""from collections import deque
queue = deque(range(100_000))
queue.append(1)

%%time
x = queue.popleft()"""
"""
N, M = map(int, input().split())
G = {i: set() for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input().split())
    G[v1].add(v2)
    G[v2].add(v1)

from collections import deque
distances = [None]*N
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in G[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            queue.append(neigh_v)
"""

# Восстановление траектории движения коня.
letters = 'abcdefgh'
numbers = '12345678'
graph = dict()
for i in letters:
    for j in numbers:
        graph[i + j] = set()


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)

        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)
print(graph)
