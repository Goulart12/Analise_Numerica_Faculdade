from __future__ import division

def nr(x0, TOL, N):
    x2 = x1 - (x1 - x0)*funcao(x1)/(funcao(x1) - funcao(x0))
    i = 1

    while ((abs(funcao(x2)) > TOL) and (i<= N)):
        x0 = x1
        x1 = x2
        x2 = x1 - (x1 - x0)*funcao(x1)/(funcao(x1) - funcao(x0))
        i = i+1

    if (i > N):
        print ('Nao houve convergencia!');

    if (abs(funcao(x2)) < TOL):
        return x2

def funcao(x0): return x0**3 - 9*x0 + 3