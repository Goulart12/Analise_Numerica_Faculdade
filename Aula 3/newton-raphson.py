from __future__ import division

def nr(x0, TOL, N):
    x1 = x0 - funcao(x0)/derivada(x0)
    i = 1

    while ((abs(funcao(x1)) > TOL) and (i<= N)):
        x0 = x1
        x1 = x0 - funcao(x0)/derivada(x0)
        i = i+1

    if (i > N):
        print ('Nao houve convergencia!');

    if (abs(funcao(x1)) < TOL):
        return x1

    return raiz

def funcao(x0): return x0**3 - 9*x0 + 3

def derivada(x0): return 3*x0**2 - 9