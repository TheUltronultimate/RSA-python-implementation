primeList = []
i = 0


def is_prime(n: int):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def GenPrimes(primeList, size):
    i = 0
    while len(primeList) < size:
        if is_prime(i):
            primeList.append(i)
            i += 1
        else:
            i += 1
    return primeList


primeList = GenPrimes(primeList, 800000)

print(primeList)
        
        
    
    