import numpy as np;

A = ([[2,3,1],[0,2,2],[0,0,3]]);
b = ([2,1,3]);

x = np.zeros(3)

x[2] = b[2]/A[2][2]

n = 3

for i in np.arange(n-2,-1,-1):
    SOMA = 0

for j in np.arange(i+1,n):
    SOMA = SOMA + A[i][j]*x[j]

x[i] = (b[i] - SOMA)/A[i][i]

print(x)