#import DiffieHellman;
from os import system
import random

from traitlets import Int
import primeList

alice_number = random.SystemRandom().randint(1, 10000) #private number for Alice
bob_number = random.SystemRandom().randint(1, 10000) #private number for Bob
#Alice_key = DiffieHellman.DiffieHellman(alice_number, bob_number)
#Bob_key = DiffieHellman.DiffieHellman(alice_number, bob_number)
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


class PK():
    def __init__(self,p: int, q: int):
        self.p = p 
        self.q = q
    
    def computePublicKey(self):
        self.n = (self.p) * (self.q)
        self.e = 65537
        return (self.n, self.e)
    
    
    def ComputePhi(self):
        self.phi = (self.p-1) * (self.q-1)
        return self.phi
    
    def computePrivateKey(self):
        self.PrivKey = pow(self.e, -1, self.phi)
        return self.PrivKey


    
    

class Encryption():
    
    def __init__(self, plainText : str, publicKey: tuple):
        self.plainText = plainText
        self.publicKey = publicKey
    
    def Transform(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.transform = ''
        for letter in self.plainText:
            index = alphabet.find(letter)
            index = str(index)
            self.transform += index 
        self.transform = int(self.transform)
        print('transform', self.transform)
        return self.transform
            
    def Encrypt(self):
        print('PublicKey:', self.publicKey)
        self.cipherText = (self.transform**self.publicKey[1]) % self.publicKey[0]
        print('hi')
        return self.cipherText
    
    
class Decryption():
    def __init__(self, cipherText: int, privateKey: int, publicKey: tuple):
        self.cipherText = cipherText
        self.privateKey = privateKey
        self.publicKey = publicKey
    
    def Decrypt(self):
        print("beginning Decryption")
        self.plainText = pow(self.cipherText,self.privateKey, self.publicKey[0])
        return self.plainText
    




p = generateRandomPrimes(1000*10**5,1000*10**20)#should be 512 bits or 1024 bits
q = generateRandomPrimes(1000*10**5, 1000*10**20)#Should be 512 or 1024 bits
print("p and q:", p, q)
print('n is:', p*q)
print('Plain Text is:', 78)
K = PK(p, q)
PublicKey = K.computePublicKey()#Gives the secure parameter ex: RSA-1024
phi = K.ComputePhi()
PrivateKey = K.computePrivateKey()
print('Private Key:', PrivateKey)
print('phi:', phi)
cipherTextObject = Encryption("hi", PublicKey)
cipherText = cipherTextObject.Transform()
cipherText = cipherTextObject.Encrypt()
print('Cipher Text is:', cipherText)
plainTextObject = Decryption(cipherText, PrivateKey, PublicKey)
plainText = plainTextObject.Decrypt()
print('Decrypted Plain Text is:', plainText)
    

        
