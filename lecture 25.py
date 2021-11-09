"""
Очередь FIFO. Для добавления и удаления принято использовать комманды add и remove.
Стек LIFO. Для добавления и удаления элементов принято использовать push и pop.
"""
"""
N, M = map(int, input().split())
graph = {i: set() for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
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


from collections import deque
distances = {v: None for v in graph}
parents = {v: None for v in graph}

start_vertex = 'a1'
end_vertex = 'h8'

distances[start_vertex] = 0
queue = deque([start_vertex])


while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)



path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]

print(graph)
print(path[::-1])
