from __future__ import division
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt


# Definição da equação diferencial ordinária de primeira ordem.
def dydx(x, y):
    return (2*y)

# Encontra o valor de y, dado x, utilizando um interval h
# Considera os valores iniciais como x0 e y0.

def rungeKutta(x0, y0, x, h):
    # Contagem do número de iterações utilizando o tamanho do passo
    # Representado pelo parâmetro h
    n = (int)((x - x0)/h)

    # Realização da iteração para um determinado número pré-determinado
    y = y0

    for i in range(1, n + 1):
        #Aplicação das formulas de Runge Kutta para encontrar o valor seguinte de y
        k1 = h * dydx(x0, y)

        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)

        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)

        k4 = h * dydx(x0 + h, y + k3)

    # Atualização do valor seguinte de y
    y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

    # Atualização do valor seguinte de x
    x0 = x0 + h
    return y

# Programa principal
x0 = 0
y = 1
x = 1
h = 0.2

print (rungeKutta(x0, y, x, h))