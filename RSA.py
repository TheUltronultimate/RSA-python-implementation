import primeGenerator
from Encrypt import *
from Decrypt import *
from Keys import *


p = primeGenerator.generateRandomPrimes(512)#should be 512 bits or 1024 bits
q = primeGenerator.generateRandomPrimes(512)#Should be 512 bits or 1024 bits
plainText = 31415926535897932384626# Message cannot be longer than p*q without adding a padding scheme
    
        
def RSA_Encrypt(p :int, q :int, plainText :int):
    '''Full process of Encryption and Decryption via RSA \n
         - input: \n
            - p --> (int) \n 
            - q --> (int) \n 
            - plainText --> (int) [unless using the optional Encrypt.Transform() method] \n
        
         - Output \n
            - tuple'''
    returned = [plainText]
    K = KeyObject(p, q)
    PublicKey = K.computePublicKey()#Length of the public key gives the security parameter (ex: RSA-1024)
    PrivateKey = K.computePrivateKey()
    cipherTextObject = Encryption(plainText, PublicKey)
    cipherText = cipherTextObject.Encrypt()
    returned.append(cipherText)
    plainTextObject = Decryption(cipherText, PrivateKey, PublicKey)
    plainText = plainTextObject.Decrypt()
    returned.append(plainText)
    return returned

total = RSA_Encrypt(p, q, plainText)
print('primes:', p,"\n", q)
print("Original Message:",total[0])
print("Encrypted Message:",total[1])
print("Decrypted Message:",total[2])


