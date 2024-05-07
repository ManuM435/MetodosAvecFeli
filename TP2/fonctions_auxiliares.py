#Funciones auxiliares utilizadas en el TP2
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def runge_kutta_4(ecuaciones:list, y0, t):
    '''Implementa el método de Runge-Kutta de orden 4 para resolver ecuaciones diferenciales'''
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n-1):
        h = t[i+1] - t[i]
        k1 = h * ecuaciones(t[i], y[i])[0] and h*ecuaciones(t[i], y[i])[1]
        k2 = h * ecuaciones(t[i] + h/2, y[i] + k1/2)[0] and h*ecuaciones(t[i] + h/2, y[i] + k1/2)[1]
        k3 = h * ecuaciones(t[i] + h/2, y[i] + k2/2)[0] and h*ecuaciones(t[i] + h/2, y[i] + k2/2)[1]
        k4 = h * ecuaciones(t[i] + h, y[i] + k3)[0] and h*ecuaciones(t[i] + h, y[i] + k3)[1]
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return y
