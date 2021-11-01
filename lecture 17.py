# Рекурсия и динамическое программирование.


# Рекурсивная реализация последовательности Фибоначчи.
def fib(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(15))


# Динамическая реализация последовательности Фибоначчи.

def fib2(n):
    assert n >= 0
    fib = [None] * (n + 1)
    fib[:2] = [0, 1]
    for k in range(2, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]
    return fib[n]


print(fib2(16))

# Реализация первого варианта с использованием динамического программирования.
F = [None] * 1000


def fib3(n):
    assert 0 <= n < 1000
    if F[n] is None:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fib3(n - 1) + fib3(n - 2)
    return F[n]


print(fib3(17))

# Задача о рюкзаке.
# Суммарная масса предметов не должна привышать заданного значения.
# Суммарная стоимость предметов должна быть максимальной.
m = [1, 2, 3, 5, 7, 11, 16]  # список предметов по массе
v = [5, 25, 10, 50, 7, 11, 32]  # список предметов по стоимости
# M = 15 # максимальная масса, которую выдержит рюкзак
# m1 = [1, 2, 3, 5] <= 15
# v1 = [5, 25, 10, 50] == 90
# NP-полная задача. На текущих вычислительных ресурсах эти задачи не имеют другого решения
# кроме решения при помощи полного перебора.

# Дискретная задача о рюкзаке. Метод - динамическое программирование.
# F(i, k) - максимальная стоимость предметов, которые помещаются в рюкзак массы к.
# При этом можно использовать только первые i предметов.
N = 7
M = 20


# def bag(M: int, N: int, m: list, v: list):
    # F = [[0] * (N + 1) for i in range(M + 1)]
    # for i in range(1, N + 1):
        # for k in range(1, M + 1):
            # if m[i] <= k:
                # F[k][i] = max(F[k][i - 1], v[i] + F[k - m[i]][i - 1])
            # else:
                # F[k][i] = F[k][i - 1]
    # return F[M][N]


# print(bag(M, N, m, v))



stuffdict = {'couch_s':(300,75),
             'couch_b':(500,80),
             'bed':(400,100),
             'closet':(200,50),
             'bed_s':(200,40),
             'desk':(200,70),
             'table':(300,80),
             'tv_table':(200,30),
             'armchair':(100,30),
             'bookshelf':(200,60),
             'cabinet':(150,20),
             'game_table':(150,30),
             'hammock':(250,45),
             'diner_table_with_chairs':(250,70),
             'stools':(150,30),
             'mirror':(100,20),
             'instrument':(300,70),
             'plant_1':(25,10),
             'plant_2':(30,20),
             'plant_3':(45,25),
             'sideboard':(175,30),
             'chest_of_drawers':(25,40),
             'guest_bed':(250,40),
             'standing_lamp':(20,30),
             'garbage_can':(30,35),
             'bar_with_stools':(200,40),
             'bike_stand':(100,80),
             'chest':(150,25),
             'heater':(100,25)
            }

def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value


def get_memtable(stuffdict, A=2000):
    area, value = get_area_and_value(stuffdict)
    n = len(value)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            # базовый случай
            if i == 0 or a == 0:
                V[i][a] = 0

            # если площадь предмета меньше площади столбца,
            # максимизируем значение суммарной ценности
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]], V[i - 1][a])

            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:
                V[i][a] = V[i - 1][a]
    return V, area, value


def get_selected_items_list(stuffdict, A=2000):
    V, area, value = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]  # начинаем с последнего элемента таблицы
    a = A  # начальная площадь - максимальная
    items_list = []  # список площадей и ценностей

    for i in range(n, 0, -1):  # идём в обратном порядке
        if res <= 0:  # условие прерывания - собрали "рюкзак"
            break
        if res == V[i - 1][a]:  # ничего не делаем, двигаемся дальше
            continue
        else:
            # "забираем" предмет
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]  # отнимаем значение ценности от общей
            a -= area[i - 1]  # отнимаем площадь от общей

    selected_stuff = []

    # находим ключи исходного словаря - названия предметов
    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)

    return selected_stuff


print(get_selected_items_list(stuffdict, A=2000))