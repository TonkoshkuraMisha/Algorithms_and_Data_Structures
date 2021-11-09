"""
Алгоритм Дейкстры. (Поиска кратчайшего расстояния в графе)
Это обход графа в ширину с перезажиганием. Требование: веса - неотрицательные числа.
Асимптотика бывает разной, в зависимости от реализации. В идеале О(N**2)
Цель: поиск кратчайших путей от исходной вершини ко всем остальным, до которых можно дотянуться.
"""
from collections import deque

def main():
    G = read_graph()
    start = input("С какой вершины начать?")
    while start not in G:
        start = input("Такой вершины в графе нет!" + "С какой вершины начать?")
    shortest_distances = dijkstra(G, start)
    finish = input("К какой вершине построить путь?")
    while finish not in G:
        finish = input("Такой вершины в графе нет!" + "К какой вершине построить путь?")
    shortest_path = recovery_shortest_path(G, start, finish, shortest_distances)


def read_graph():
    M = int(input())
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

def dijkstra(G, start):
    Q = deque()
    s = {}
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if u not in s or s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                Q.append(u)
    return s

if __name__ == "__main__":
    main()


# Алгоритм Флойда-Уоршалла
