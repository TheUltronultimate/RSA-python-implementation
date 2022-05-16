import primeGenerator
from Encrypt import *
from Decrypt import *
from Keys import *


p = primeGenerator.generateRandomPrimes(1000*10**5,1000*10**10)#should be 512 bits or 1024 bits
q = primeGenerator.generateRandomPrimes(1000*10**5,1000*10**10)#Should be 512 bits or 1024 bits
plainText = 31415926535897932384626# overflow mistakes ocurr (for longer messages) --> strangely this doesn't lead to a wrong decryption rather a wrong plaintext

    
        
def RSA_Encrypt(p, q, plainText):
    K = KeyObject(p, q)
    PublicKey = K.computePublicKey()#Gives the secure parameter ex: RSA-1024
    PrivateKey = K.computePrivateKey()
    cipherTextObject = Encryption(plainText, PublicKey)
    cipherText = cipherTextObject.Encrypt()
    plainTextObject = Decryption(cipherText, PrivateKey, PublicKey)
    plainText = plainTextObject.Decrypt()
    return plainText, cipherText, plainText

total = RSA_Encrypt(p, q, plainText)

print("Original Message:",total[0])
print("Encrypted Message:",total[1])
print("Decrypted Message:",total[2])


