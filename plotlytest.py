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

def chargerate(Q, C, R, Vb, Vt):
    x = np.arange(0,10, 0.1)
    data = []
    for i in range(len(x)):
        y = C*V*(1-np.exp(-x[i]/R*C))
        data.append(y)

    py.show(py.plot(x,data))
