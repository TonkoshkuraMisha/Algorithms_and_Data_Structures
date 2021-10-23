def is_simple_number(x):
    '''
        Определяет, является ли число простым.
        Если простое, то возвращает True,
        иначе - возвращает False.
    :param x: int
    :return: bool
    '''
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True
for i in range(2, 101):
    print(f'{i} = {is_simple_number(i)}')


def factorize_number(x):
    '''
    Раскладывает число на множители.
    Печатает их на экран.
    :param x: int
    :return: int
    '''
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1
