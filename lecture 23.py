"""
Варианты хранения графа в памяти.
A -- B -- C -- D
Первый способ:
    1) список вершин.
    2) список рёбер.
Второй способ:
    Матрица смежности.
    V = ['A', 'B', 'C', 'D']
    index = {V[i]:i for i in range(len(V))} - dict comprehension
    A = [[0,1,0,0], [1,0,1,0], [0,1,0,1], [0,0,1,0]]
Третий способ:
    Списки смежности.
    G = {'A':{'B'}, 'B':{'A', 'C'}, 'C':{'B', 'D'}, 'D':{'C'}}
"""

M, N = [int(x) for x in input().split()]
V = []
index = {}
A = [[0]*N for i in range(N)]
for i in range(N):
    v1, v2 = input().split()
    for v in v1, v2:
        if v not in index:
            V.append(v)
            index[v] = len(V) - 1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1


