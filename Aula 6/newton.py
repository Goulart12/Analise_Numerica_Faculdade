from scipy.interpolate import interpolate
from numpy.polynomial.polynomial import Polynomial
import numpy as np

x = np.array([0, 1, 2])
y = x**3

f = interpolate.BarycentricInterpolator(x, y)
yn = f(xn)