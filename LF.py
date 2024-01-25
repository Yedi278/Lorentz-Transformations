import numpy as np

c = 3e8

class transf():

    def __init__(self,v):
        self.v = v
        self.betha, self.gamma = self.gamma(self.v)
    
    def lorentz_fact(v):

        betha = v/c
        gamma = 1/np.sqrt(1-np.power(betha,2))

        return betha,gamma

    def trasf(self,x,t):

        x1 = (x - self.v*t) * self.gamma
        t1 = self.gamma * (t - (self.v*x/c**2))

        return x1,t1