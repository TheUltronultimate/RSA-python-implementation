#import DiffieHellman;
import random

alice_number = random.SystemRandom().randint(1, 10000) #private number for Alice
bob_number = random.SystemRandom().randint(1, 10000) #private number for Bob
#Alice_key = DiffieHellman.DiffieHellman(alice_number, bob_number)
#Bob_key = DiffieHellman.DiffieHellman(alice_number, bob_number)
def generateRandomPrimes(min, max):
    assert min < max, "min value must be smaller than max value"
    A = True
    p = 1
    while A:
        q = random.SystemRandom().randint(min, max)
        #primes = [i for i in range(p,q) if isPrime(i)]
        if isPrime(q):
            g = q
            return g

def isPrime(n):
    
    '''Checks if a number n is Prime
    Input: int;
    Output: Boolean;
    '''
    flag = True
    for i in range(1, round((n**0.5)+1), 2 ):
        #print(i)
        if (n % i) == 0 and i != 1:
            return False
        
    return flag


print("h")
p = generateRandomPrimes(200*10**20,200*10**100)#should be 512 bits or 1024 bits
q = generateRandomPrimes(200*10**20, 200*10**100)#Should be 512 or 1024 bits
print("p and q:", p, q)
class PK():
    def __init__(self,p, q ):
        self.p = p 
        self.q = q
    
    def ComputeN(self):
        self.n = (self.p) * (self.q)
        return self.n
    def ComputeThi(self):
        self.thi = (self.p-1) * (self.q-1)
        
        
K = PK(p, q)
n = K.ComputeN()#Gives the secure parameter ex: RSA-1024
thi = K.ComputeThi()


print(n)
        
        
