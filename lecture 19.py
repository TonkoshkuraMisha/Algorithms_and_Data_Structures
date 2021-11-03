# Heap. Stack. Куча. (Это всё синонимы)

class Heap:

    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]

    def extract_min(self):
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        if not self.size:
            return None
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]


# min --> O(1)
# sift_down --> O(log n)
# sift_dup --> O(log n)
# memory --> O(n)
# extract_min --> O(log n)
# insert --> O(log n)


# Сортировка кучей. Heap_sort.


def heapify(Array):
    heap = Heap()
    for item in Array:
        heap.insert(item)
    return heap


# O(n*log(n)) - время работы heap_ify()

def get_sorted_arr(heap):
    Array = []
    while heap.size:
        Array.append(heap.extract_min())
    return Array

# working
A = [46, 15, 3, 4, 21, 79, 61]
B = get_sorted_arr(heapify(A))
print(B)



# O(n*log(n)) - время работы get_sorted_arr()

# Время работы как у сортировки слиянием или быстрой сортировки.

def heapify_fast(Array):
    heap = Heap()
    heap.values = Array[:]
    heap.size = len(Array)
    for i in reversed(range(len(Array) // 2)):
        heap.sift_down(i)
    return heap

# don`t working
A = [46, 15, 3, 4, 21, 79, 61]
B = get_sorted_arr(heapify_fast(A))
print(B)
