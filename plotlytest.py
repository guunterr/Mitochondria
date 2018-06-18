import random
import numpy as np
import matplotlib.pyplot as py
import math
def test():
    x = np.arange(100)
    y = random.randint(0,100)
    data = []
    for i in range(0,100):
        y = y + random.randint(-20,20)/10
        data.append(y)

    print(data)
    print(x)
    py.show(py.plot(x, data))

def Charge(C,R,V,t):
    Q = C*V*(1-np.exp(-t/R*C))
    return Q

def dbydt(Q, C, R, V, t):
    h = 0.00001
    dQ = np.abs((Q(C,R,V,t - h) - Q(C,R,V,t + h))/2*h)
    return dQ

def chargerate(C, R, V, Vt):
    x = np.arange(0,10, 0.1)
    data = []
    derivatives = []
    for i in x:
        Q = Charge(C,R,V,i)
        dQ = dbydt(Charge, C,R,V,i)
        Vc = Q/C
        
        data.append(Vc)
        derivatives.append(dQ)

    py.plot(x,data, 'r', x, derivatives, "g")
    py.show()


    
