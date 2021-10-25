# list comprehensions

# first version
A = [x ** 2 for x in range(10)]
print(A)

# second version
B = []
for i in range(10):
    B.append(i ** 2)
print(B)
print('*' * 50)

# Квадратичные сортировки O(N**2)

A = [4, 2, 5, 1, 3]


def insert_sort(A):
    """
    Сортировка списка А вставками.
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choice_sort(A):
    """
    Сортировка списка А методом выбора.
    """
    N = len(A)
    for pos in range(N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """
    Пузырьковая сортировка списка А.
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print(f"test_case #1: ", end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print(f"test_case #2: ", end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print(f"test_case #3: ", end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    print('*' * 50)


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)


# Сортировка подсчётом O(N).
def count_sort(A):
    """
    Сортировка подсчётом списка А.
    """
    A_sorted = []
    N = len(A)
    F = [0] * 10
    for i in range(N):
        x = A[i]
        F[x] += 1
    for digit in range(10):
        A_sorted.append(digit*F[digit])
    print(A_sorted)


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print(f"test_case #1: ", end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print(f"test_case #2: ", end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print(f"test_case #3: ", end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    print('*' * 50)


if __name__ == "__main__":
    test_sort(count_sort)
