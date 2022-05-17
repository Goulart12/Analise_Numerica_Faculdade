import numpy as np
from numpy import random

A = np.random.random((3,4))

print(A)

A = np.array([[1,2],[2,1]]); 

print(A)

B = np.array([[2,1],[2,1]]); 

print(B)

print(A*B)

C = A.dot(B)

print(C)
