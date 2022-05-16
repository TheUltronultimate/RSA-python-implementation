 #Decryption module --> Decryption Object
class Decryption():
    def __init__(self, cipherText: int, privateKey: int, publicKey: tuple):
        self.cipherText = cipherText
        self.privateKey = privateKey
        self.publicKey = publicKey
    
    def Decrypt(self) -> int:
        self.plainText = pow(self.cipherText,self.privateKey, self.publicKey[0])
        return self.plainText
    