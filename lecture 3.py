from random import randint

N = 3
M = 4


# функция вывода матрицы на экран
def output_matrix(matrix):
    for row in matrix:
        for item in row:
            print("%3d" % item, end='')
        print()


# заполнение матрицы
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(1, 99))
    a.append(b)

# вывод матрицы до сортировки
output_matrix(a)
print()

# сортировка в строках матрицы
for i in range(N):
    for j in range(M - 1):
        for k in range(M - j - 1):
            if a[i][k] > a[i][k + 1]:
                a[i][k], a[i][k + 1] = a[i][k + 1], a[i][k]

# вывод матрицы после сортировки
output_matrix(a)

from random import randint

N = 5
# заполняем и сразу выводим
a = []
for i in range(N):
    b = []
    for j in range(N):
        n = randint(1, 9)
        b.append(n)
        print("%3d" % n, end='')
    a.append(b)
    print()
# находим сумму элементов главной и побочной диагоналей
diagonal1 = 0
diagonal2 = 0
for i in range(N):
    diagonal1 += a[i][i]
    diagonal2 += a[i][N - 1 - i]
print(diagonal1)
print(diagonal2)
