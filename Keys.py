#Keys module --> Key Object

class KeyObject():
    def __init__(self,p: int, q: int):
        self.p = p 
        self.q = q
        self.phi = (p-1)*(q-1)
    
    def computePublicKey(self) -> tuple:
        self.n = (self.p) * (self.q)
        self.e = 65537
        return (self.n, self.e)
    
    def computePrivateKey(self) -> int:
        self.PrivKey = pow(self.e, -1, self.phi)
        return self.PrivKey
