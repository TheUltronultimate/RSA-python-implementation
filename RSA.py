import primeGenerator
from Encrypt import *
from Decrypt import *
from Keys import *

import random
import primeList


def generateRandomPrimes(min, max) -> int:
    '''generates a random prime number,
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
    """primality test using 6k+-1 optimization."""
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



class KeyObject():
    #Object for Generating all Keys in the implementation
    def __init__(self,p: int, q: int):
        self.p = p 
        self.q = q
    
    def computePublicKey(self) -> int:
        '''Computes RSA public Key:
                                    --> e : 65537
                                    --> n : p*q  '''
        self.n = (self.p) * (self.q)
        self.e = 65537
        return (self.n, self.e)
    
    
    def ComputePhi(self):
        self.phi = (self.p-1) * (self.q-1)
        return self.phi
    
    def computePrivateKey(self):
        self.PrivKey = pow(self.e, -1, self.phi) # modular exponentiation to maximise efficency <=> e ^-1 modulo phi
        return self.PrivKey


    

class Encryption():
    
    def __init__(self, plainText : int, publicKey: tuple):
        self.plainText = plainText
        self.publicKey = publicKey
    
    def Transform(self) -> int:
        '''Transforms Plain Text to base 10'''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.transform = ''
        for letter in self.plainText:
            index = alphabet.find(letter)
            index = str(index)
            self.transform += index 
        self.transform = int(self.transform)
        return self.transform
            
    def Encrypt(self) -> int:
        '''Encrypts via modular exponentiation'''
        self.cipherText = pow(self.plainText, self.publicKey[1], self.publicKey[0])
        return self.cipherText
    
    
     
class Decryption():
    def __init__(self, cipherText: int, privateKey: int, publicKey: tuple):
        '''Constructor'''
        self.cipherText = cipherText
        self.privateKey = privateKey
        self.publicKey = publicKey
    
    def Decrypt(self) -> int:
        '''Decrypts Cipher Text via modular exponentiation'''
        self.plainText = pow(self.cipherText,self.privateKey, self.publicKey[0])
        return self.plainText
    






p = primeGenerator.generateRandomPrimes(1000*10**10,1000*10**12)#should be 512 bits or 1024 bits
q = primeGenerator.generateRandomPrimes(1000*10**10, 1000*10**12)#Should be 512 or 1024 bits
print("p : ", p)
print("q :", q)
print('n :', p*q)



K = KeyObject(p, q)
PublicKey = K.computePublicKey()#Gives the secure parameter ex: RSA-1024
phi = K.ComputePhi()
PrivateKey = K.computePrivateKey()


print('Private Key :', PrivateKey)
print('phi:', phi)



cipherTextObject = Encryption(31415926535897932384626, PublicKey)
#cipherText = cipherTextObject.Transform()
cipherText = cipherTextObject.Encrypt()


print('Cipher Text :', cipherText)


plainTextObject = Decryption(cipherText, PrivateKey, PublicKey)
plainText = plainTextObject.Decrypt()


print('Decrypted Plain Text :', plainText)
    

        
