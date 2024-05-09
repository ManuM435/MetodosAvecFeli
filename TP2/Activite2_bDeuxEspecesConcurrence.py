import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import fonctions_auxiliares as aux

# Definimos las ecuaciones diferenciales
def lotkaVolterra(N1, N2, r1, r2, K1, K2, alpha12, alpha21):
    dN1dt = r1 * N1 * ((K1 - N1 - alpha12 * N2) / K1)
    dN2dt = r2 * N2 * ((K2 - N2 - alpha21 * N1) / K2)
    return [dN1dt, dN2dt]

def rkSolve(ode, y0, t, h):
    '''Resuelve el sistema de ecuaciones diferenciales con el método de Runge-Kutta'''
    return aux.runge_kutta_4(ode, y0, t, h)

def EquilibriumPoint(r1, r2, K1, K2, alpha12, alpha21):
    '''Calcula el punto de equilibrio del sistema de ecuaciones diferenciales'''
    N1 = K1 - alpha12 * (K2 - alpha21 * K1) / (1 - alpha12 * alpha21)
    N2 = (K2 - alpha21 * K1) / (1 - alpha12 * alpha21)
    return [N1, N2]

# el time y su'estep
t = np.linspace(0, 100, 1000)
h = 0.1

''' datos = (N1, N2, r1, r2, K1, K2, alpha12, alpha21) '''
# Son para el lotkaVolterra

pars0 = (0.1, 0.5, 100, 80, 0.01, 0.66)
#TODO CAMBIAR ESTOS DATOS, PROBAR MODELOS, FIJARSE ESO DE '4 TIPOS DE GRAFICO' EN BASE A SUS VALORES DE NO SE QUE Y LAS ISOCLINAS??
pars1 = (0.1, 0.5, 100, 80, 0.01, 0.66)
pars2 = (0.1, 0.5, 100, 80, 0.01, 0.66)
pars3 = (0.1, 0.5, 100, 80, 0.01, 0.66)
pars4 = (0.1, 0.5, 100, 80, 0.01, 0.66)
pars5 = (0.1, 0.5, 100, 80, 0.01, 0.66)
pars6 = (0.1, 0.5, 100, 80, 0.01, 0.66)
pars7 = (0.1, 0.5, 100, 80, 0.01, 0.66)

datos0 = (EquilibriumPoint(*pars0), pars0)
# Hay que ver de separar los datos y que no esten en listas maybe


r1 = 0.5
r2 = 0.75
K1 = 100
K2 = 80
alpha12 = 1
alpha21 = 10




TheseEquis = (EquilibriumPoint(r1, r2, K1, K2, alpha12, alpha21))
print(f"Los Puntos de Equilibrio son: {TheseEquis}")



