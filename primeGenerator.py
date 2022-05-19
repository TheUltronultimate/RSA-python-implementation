import random


# Module for securely generating random prime numbers to be used in RSA

def generateRandomPrimes(min: int, max: int):
    '''Generates a random Prime number,
        - input : \n
                - min: int\n
                - max: int\n
        - output :
                - g: int'''
    assert min < max, "min value must be smaller than max value"
    assert type(min) and type(max) == int, "min and max must be integers"
    A = True
    while A:
        # random.SystemRandom allows us to use cryptographically secure random numbers
        q = random.SystemRandom().randint(min -1, max)
        if is_prime(q):
            g = q
            return g

# Most efficient way I could find to verify primality 
def is_prime(n: int):
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

