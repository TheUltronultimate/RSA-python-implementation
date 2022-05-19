#Keys module --> Key Object

class KeyObject():
    def __init__(self,p: int, q: int):
        self.p = p 
        self.q = q
        #Calculates the totient
        self.phi = (p-1)*(q-1)
    
    def computePublicKey(self):
        self.n = (self.p) * (self.q)
        #e is standarised to 65537 in most RSA implementations
        self.e = 65537
        return (self.n, self.e)
    
    def computePrivateKey(self):
        # (e^-1) modulo phi
        self.PrivKey = pow(self.e, -1, self.phi)
        #print('Private key:', self.PrivKey)
        return self.PrivKey
