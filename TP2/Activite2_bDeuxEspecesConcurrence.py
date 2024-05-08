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

# el time y su'estep
t = np.linspace(0, 100, 1000)
h = 0.1

''' datos = (N1, N2, r1, r2, K1, K2, alpha12, alpha21) '''
# Son para el lotkaVolterra
datos0 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
#TODO CAMBIAR ESTOS DATOS, PROBAR MODELOS, FIJARSE ESO DE '4 TIPOS DE GRAFICO' EN BASE A SUS VALORES DE NO SE QUE Y LAS ISOCLINAS??
datos1 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
datos2 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
datos3 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
datos4 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
datos5 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
datos6 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)
datos7 = (10, 10, 0.1, 0.5, 100, 80, 0.01, 0.66)


r1 = 0.1
r2 = 0.5
K1 = 100
K2 = 80
alpha12 = 0.01
alpha21 = 0.66

# Condiciones iniciales
y00, y01, y02, y03, y04, y05, y06, y07 = [10, 10], [10, 10], [10, 10], [10, 10], [10, 10], [10, 10], [10, 10], [10, 10]

# Resolvemos el sistema de ecuaciones diferenciales con nuestro runge kutta
y = np.array([y00])
for i in range(len(t) - 1):
    y0 = rkSolve(lambda y, t: lotkaVolterra(y[0], y[1], r1, r2, K1, K2, alpha12, alpha21), y00, t[i], h)
    y = np.append(y, [y0], axis=0)

# # Graficamos
# plt.plot(t, y[:, 0], label='N1')
# plt.plot(t, y[:, 1], label='N2')
# plt.xlabel('Time')
# plt.ylabel('Population')
# plt.title('Population Over Time')
# plt.legend()
# plt.show()

def EquilibriumPoint(r1, r2, K1, K2, alpha12, alpha21):
    '''Calcula el punto de equilibrio del sistema de ecuaciones diferenciales'''
    N1 = - ((K1 - K2) / (alpha21 + 1/alpha12))
    N2 = (K1 - N1) / alpha12
    return [N1, N2]

auxi = (EquilibriumPoint(r1, r2, K1, K2, alpha12, alpha21))

print(auxi)

equi1 = auxi[0]
equi2 = auxi[1]
print(equi2)

print(lotkaVolterra(equi1, equi2, r1, r2, K1, K2, alpha12, alpha21))
