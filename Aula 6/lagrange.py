from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import numpy as np

x = np.array([0, 1, 2])
y = x**3

poly = lagrange(x, y)

Polynomial(poly).coef

#array([ 3., -2., 0.])