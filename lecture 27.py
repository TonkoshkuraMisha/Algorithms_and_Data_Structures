
"""
 Двоичные деревья поиска. (Бинарные деревья. Зачем они нужны? Как их баллансировать.)
 Дерево - это граф, у которого нет цикла! Корневое дерево - это дерево, у которого выделена одна вершина.
 Бинарное дерево - корневое дерево, где у каждой вершины не более двух дочерних вершин.
 Высота дерева - максимальное количество рёбер от корня до листа.
 Дерево, у которого важен порядок рассположения дочерних вершин называется упорядоченным.
 Дерево называется сбалансированным, если для каждой его вершины, высота левого и правого поддеревьев
 отличается не более чем на еденицу.
 Два основных алгоритма для двоичных деревьев поиска:
  - АВЛ-деревья;
  - Красно-чёрные деревья;
"""

# Реализация двоичного дерева поиска. (Д.Д.П. - структура данных, хранящая в вершинах некоторые элементы, содержащие ключ.)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# Алгоритм Флойда-Уоршолла.
