from math import sqrt
from numpy import *
from scipy import integrate

import pylab as p

def rk4(funcaoy, funcaox, t_inicial, x, y, t1, n):
    vt = [0] * (n + 1)
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    
    h = (t1 - t_inicial) / float(n)
    
    vt[0] = t = t_inicial
    vx[0] = x
    vy[0] = y 
    
    for i in range(1, n + 1):
        k1 = h * funcaox(x, y)
        k2 = h * funcaox(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * funcaox(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * funcaox(x + h, y + k3)

        k1 = h * funcaoy(x, y)
        k2 = h * funcaoy(y + 0.5 * h, x + 0.5 * k1)
        k3 = h * funcaoy(y + 0.5 * h, x + 0.5 * k2)
        k4 = h * funcaoy(y + h, x + k3)
        
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        vx[i] = x = x + (k1 + k2 + k2 + k3 + k3 + k4) / 6

        vt[i] = t = t_inicial + i * h
    return vt, vy, vx

def funcaox(x, y):
    return -(398600.4418 * x) / (sqrt(x ** 2 + y ** 2) ** 3)

def funcaoy(x, y):
    return -(398600.4418 * y) / (sqrt(x ** 2 + y ** 2) ** 3)
 
vt, vy, vx = rk4(funcaoy, funcaox, 0, 1, 0, 10, 50)

for x, y, yy in list(zip(vt, vy, vx))[::10]:
    print("%s %s %s" % (x, y, yy))  # y - (4 + x * x) ** 2 / 16))

p.figure(1)
p.plot(vt, vx, 'r-', label='')
p.title('Orbita')
p.figure(2)
p.plot(vt, vy, 'r-', label='')
p.title('Orbita')
p.show()
