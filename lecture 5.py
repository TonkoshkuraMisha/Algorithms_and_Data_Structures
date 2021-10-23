# Поиск элемента в массиве.

def array_search(A: list, N: int, x: int):
    """
    Поиск числа x в массиве А от 0 до N-1.
    Возвращает индекс x в массиве или -1.
    Если несколько одинаковых x, то возвращает
    индекс первого по счёту.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


test_array_search()
print('*'*30)

# Обращение массива.

def invert_array(A, N):
    """
    Обращение массива (поворот массива задом-наперёд).
    """
    for k in range(N // 2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")


test_invert_array()
print('*'*30)

# Циклический сдвиг в массиве.

def left_shift_array(A: list, N: int):
    """
    Циклический сдвиг массива влево.
    """
    print(A)
    tmp_l = A[0]
    for k in range(N - 1):
        A[k] = A[k + 1]
    A[N - 1] = tmp_l
    print(A)


def right_shift_array(A: list, N: int):
    """
    Циклический сдвиг массива вправо.
    """
    print(A)
    tmp_r = A[N - 1]
    for k in range(N - 1, 0, -1):
        A[k] = A[k - 1]
    A[0] = tmp_r
    print(A)

A1 = [1, 2, 3, 4, 5]
A2 = [12, 32, -3, 14, 555, 0, -11]

left_shift_array(A1, len(A1))
print('*'*30)
right_shift_array(A2, len(A2))
print('*'*30)

# Решето Эратосфена.
def sieve_of_eratosthenes(N: int):
    A = [True]*N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    for k in range(2, N):
        print(k, '-', 'простое' if A[k] else 'составное')

sieve_of_eratosthenes(1000)

# В процессе вывода результата мы воспользовались тернарным оператором.
# Данный оператор выглядит следующим образом.
# [Значение 1] if [Условие] else [Значение 2]