class KeyObject():
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
