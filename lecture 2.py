s = set()
new_element = None
while new_element != exit:
    new_element = input()
    if new_element in s:
        print('Уже есть!')
    else:
        s.update(new_element)
        print(s)
