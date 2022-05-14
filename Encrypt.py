    

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
    