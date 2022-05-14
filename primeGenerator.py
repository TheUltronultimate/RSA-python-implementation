import random
import primeList


def generateRandomPrimes(min, max):
    '''Generates a random Prime number,
    input:
            -min: int
            -max: int
    output:
            -g: int'''
    assert min < max, "min value must be smaller than max value"
    A = True
    while A:
        q = random.SystemRandom().randint(min, max)
        if is_prime(q):
            g = q
            return g

def is_prime(n: int):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    for i in primeList.primeList:
        if n % i == 0:
            return False
    i = primeList.primeList[-1]
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

