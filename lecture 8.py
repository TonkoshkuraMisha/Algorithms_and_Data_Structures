def generate_numbers(N, M, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep='')
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()


#generate_numbers(10, 5)


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
    else:
        gen_bin(M - 1, prefix + "0")
        gen_bin(M - 1, prefix + "1")


#gen_bin(10)


def generate_permutations(N, M=-1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, с префиксом prefix.
    """
    M = N if M == -1 else M  # по умолчанию N чисел в M позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()


def find(number, A):
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

generate_permutations(4)
