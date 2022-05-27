import random


# Module for securely generating random prime numbers to be used in RSA

def generateRandomPrimes(n):
    '''Generates a random Prime number,
        - input : \n
                - min: int\n
                - max: int\n
        - output :
                - g: int'''
    
    A = True
    while A:
        # random.SystemRandom allows us to use cryptographically secure random numbers
        q = random.SystemRandom().randint(2**(n-1) + 1, 2**n -1)
        if q %2 != 0:
            if isMillerRabinPassed(q, 40): #40 rounds of rabin miller is standard for good enough security
                return q

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

def isMillerRabinPassed(miller_rabin_candidate, numberOfRabinTrials):
    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1
    
    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
        
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)

    def trialComposite(round_tester):
        if pow(round_tester, evenComponent,miller_rabin_candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent,miller_rabin_candidate)== miller_rabin_candidate-1:
                return False
            return True
        
        
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2,miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
        return True
