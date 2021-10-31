# Динамическое программирование - сведение рекурсий к циклам.

# III. Алгоритм дискретной укладки рюкзака. (на самостоятельное изучение)

# IV. Алгоритм редакционных изменений == Алгоритм Левенштейна (асимптотика O(M*N))
# Вычисление расстояния Левинштейна. Редакционное расстояние между строками.

A = 'колокол'
B = 'молоко'


# Сколько минимум типографических опечаток нужно совершить в А чтобы получить В?
# Типы ошибок: 1. перепутали символ, 2. вставили лишний символ. 3. потеряли нужный символ
# Fij - минимальное редакционное расстояние между срезами A[:i] and B[:j] Fnm - ответ.
# Fij = { F(i-1)(j-1), if Ai == Bi
#       { 1+min[F(i-1)j, Fi(j-1), F(i-1)(j-1)]
# Fi0 = i, F0j = j, F00 = 0 - крайние случаи.

def levenstein(A, B):
    F = [[i + j if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[len(A)][len(B)]


C = 'пиво'
D = 'хлеб'

print(levenstein(C, D))


# Проверка равенства строк. O(N)
# (эквивалентно A == B)
def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


# Поиск подстроки в строке O(N*M)
s = 'abcbacdbabcbdbabdcabdcabccdbdcdbacdcbdca'
sub = 'abc'


def search_substring(s, sub):
    for i in range(len(s) - len(sub)):
        if equal(s[i:i + len(sub)], sub):
            print(i)

search_substring(s, sub)

# Префикс-функция Pi от строки.
# Собственный суффикс - суффикс, не равный строке.
# Pi - длина максимального собственного суффикса, который является префиксом.
# (лютейшая муть). (алгоритм Кнута-Морриса-Пратта - ещё одна муть.)