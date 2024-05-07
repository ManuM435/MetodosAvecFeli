#Funciones auxiliares utilizadas en el TP2
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def runge_kutta_4(ode, y0, t, h):
    '''Implementa el método de Runge-Kutta de orden 4 para resolver ecuaciones diferenciales'''
    k1 = h * np.array(ode(y0, t))
    k2 = h * np.array(ode(y0 + k1 / 2, t + h / 2))
    k3 = h * np.array(ode(y0 + k2 / 2, t + h / 2))
    k4 = h * np.array(ode(y0 + k3, t + h))
    return y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6

