# Тип list

A = [True, 2, 5.3, 'Hello']
for i in A:
    print(type(i))

B = (True, 2, 5.3, A)
print(type(B))

print(B)
A[0] = False
print(B)

A = [(1, 5), (-3, 4), (-7, 2), (8, 3), (0, 0)]
for x, y in A:
    print((x, y))

# Строки в Python. ("Не дай Вам бог работать со строками на чистом С. Never!" Т. Хирьянов)
# Срезы строк.



