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

# aca hacer todo lo demas del ejercicio, los datos y todo
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


# Isoclinas Cero

# Parametros Part 1
N1a = np.linspace(0, 100, 100)
N2a = np.linspace(0, 200, 100)
K1a = 100
K2a = 200
alpha12a = 1/2
alpha21a = 2
# Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# Si K2 > K1, entonces [isoclina de N2 > isoclina de N1]

# Isoclinas Part 1
isoclineN1a = K1a - alpha12a * N2a
isoclineN2a = K2a - alpha21a * N1a

# Graficar Part 1
plt.plot(N1a, isoclineN1a, label='Isocline of N1')
plt.plot(isoclineN2a, N2a, label='Isocline of N2')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.show()

# Parametros Part 2
N1b = np.linspace(0, 200, 100)
N2b = np.linspace(0, 100, 100)
K1b = 200
K2b = 100
alpha12b = 2
alpha21b = 1/2
# Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# Si K1 > K2, entonces [isoclina de N1 > isoclina de N2]

# Isoclinas Part 2
isoclineN1b = K1b - alpha12b * N2b
isoclineN2b = K2b - alpha21b * N1b

# Graficar Part 2
plt.plot(N1b, isoclineN1b, label='Isocline of N1')
plt.plot(isoclineN2b, N2b, label='Isocline of N2')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.show()

# Parametros Part 3
N1c = np.linspace(0, 200, 100)
N2c = np.linspace(0, 100, 100)
K1c = 400
K2c = 400
alpha12c = 4
alpha21c = 2

# Isoclinas Part 3
isoclineN1c = K1c - alpha12c * N2c
isoclineN2c = K2c - alpha21c * N1c

# Graficar Part 3
plt.plot(N1c, isoclineN1c, label='Isocline of N1')
plt.plot(isoclineN2c, N2c, label='Isocline of N2')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.show()


#TODO: Arreglar esta ultima

# Parametros Part 4
N1d = np.linspace(0, 100, 100)
N2d = np.linspace(0, 200, 100)
K1d = 400
K2d = 400
alpha12d = 2
alpha21d = 4

# Isoclinas Part 4
isoclineN2d = K1d - alpha12d * N2d
isoclineN1d = K2d - alpha21d * N1d

# Graficar Part 4
plt.plot(N1d, isoclineN1d, label='Isocline of N1')
plt.plot(isoclineN2d, N2d, label='Isocline of N2')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.show()


