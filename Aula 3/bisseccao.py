from __future__ import division

def funcao(x0): return x0**3-9*x0 + 3

def biss(a, b, TOL, N):
    f0 = funcao(a)
    f1 = funcao(b)
    i = 1

    while ((abs(funcao(a)) > TOL) and (abs(funcao(b)) > TOL) and (i<= N)):
        if (abs (a-b) < TOL):
            raiz = (a + b)/2
            media = (a + b)/2

            f2 = funcao(media)

        if (f0*f2 < 0):
            b = media

            f1 = funcao(media)

        else:
            a = media

            f0 = funcao(media)

            i = i + 1

        if (i > N):

            print ('Nao houve convergencia') 

        if (abs(funcao(a)) < TOL):
            raiz = a

        else:
            raiz = b