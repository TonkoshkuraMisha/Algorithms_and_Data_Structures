# Рекурсия

def matryoshka(n):
    if n == 1:
        print(f"Матрёшечка:{n}")
    else:
        print(f"Верх матрёшки:{n}")
        matryoshka(n - 1)
        print(f"Низ матрёшки:{n}")


matryoshka(3)

import graphics as gr

window = gr.GraphWin("Recursion", 600, 600)
alpha = 0.1


def fractal_rectangle(A, B, C, D, deep=23):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, deep - 1)


# fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 50)
# input()

# Factorial
# n! = (n-1)!*n
# f(n) = { 1 if n <= 1, f(n-1)*n if n > 1

def f(n):
    assert n >= 0, "Число должно быть положительным."
    if n <= 1:
        return 1
    return f(n - 1) * n


print(f(15))


# GCD(greatest common divisor) == Euclidean algorithm
# first realization
def gcd1(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd1(a - b, b)
    else:
        return gcd1(a, b - a)


print(gcd1(247, 1001))


# second realization

def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a % b)


print(gcd2(247, 1001))


# third realization

def gcd3(a, b):
    return a if b == 0 else gcd3(b, a % b)


print(gcd3(161, 1001))


# fast exponentiation first realization
def pow1(a, n):
    return a if n == 1 else pow1(a, n - 1) * a


print(pow1(5, 11))


# fast exponentiation second realization
def pow2(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow2(a, n - 1) * a
    else:
        return pow2(a ** 2, n // 2)


print(pow2(3, pow2(3, 3)))


# Hanoi tower

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


moveTower(3, "A", "B", "C")
