import random
from xmlrpc.client import boolean

#Module for securely generating random prime numbers to be used in RSA
def generateRandomPrimes(min: int, max: int) -> int:
    assert type(min) and type(max) == int, "min and max must be integers"
    '''Generates a random Prime number,
    input:
            -min: int
            -max: int
    output:
            -g: int'''
    assert min < max, "min value must be smaller than max value"
    A = True
    while A:
        q = random.SystemRandom().randint(min -1, max)
        if is_prime(q):
            g = q
            return g

#Most efficient way I could find to verify primality 
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    assert type(n) == int, "n must be an integer"
    
    if not n%2 or not n%3:
        return False
    stop = int(n**0.5)
    i = 5
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

