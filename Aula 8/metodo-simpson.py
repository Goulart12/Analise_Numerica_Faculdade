import numpy as np
import math

f = lambda x: x**2
a = 2; b = 3; N = 10
x = np.linspace(a,b,N+1)
y = f(x)
dx = (b-a)/N
soma_Simpson = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])

print("Integral:",soma_Simpson)