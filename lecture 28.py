

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

print(list(itertools.takewhile(lambda x : x <= 31, primes())))