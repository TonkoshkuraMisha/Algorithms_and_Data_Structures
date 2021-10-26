# Рекуррентные сортировки.


# I. Сортировка слиянием

# I.1. Слияние отсортированных массивов

def merge(A, B):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


# I.2. Рекурсивная функция.

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


# example merge sort
M = [-4, 5, 67, -9, 10, 1]
merge_sort(M)
print(*M)



# II. Сортировка Хоара

# II.1. Сортирующее действие
def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


# example hoar_sort (or quick sort)
K = [-4, -102, -2000, 234, 45, -67, -9, 1234, 10, 1]
hoar_sort(K)
print(*K)




# III. Проверка массива на сортированность.

def check_sorted(A, ascending=True):
    """ Проверка отсортированности массива за O(len(A))"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag

# example check_sorted
P1 = [1, 2, 3, 4, 5, 6]
P2 = [1, 2, 3, 4, 6, 5]
print(check_sorted(P1))
print(check_sorted(P2))


# IV. Бинарный поиск в массиве. Реализуется для отсортированного массива.

def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left+right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left+right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

def bin_find(A, key):
    if right_bound(A, key) - left_bound(A, key) > 1:
        print(f"[...index = {left_bound(A, key)}, indexes of our element(s), index = {right_bound(A, key)}...]")
    else:
        print(f"{key} not find in A")

bin_find(P1, 3)
bin_find(P1, 9)

