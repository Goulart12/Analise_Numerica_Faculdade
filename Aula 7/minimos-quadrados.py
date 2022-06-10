import numpy as np
import matplotlib.pyplot as plt

xi = np.array([1, 1.5, 2])

yi = np.array([1.2,1.3,2.3])

V = np.array([xi**1,xi**0]).transpose();V

a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi);a

xx = np.linspace(0.5,2.5)

plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')

plt.grid();

plt.show()