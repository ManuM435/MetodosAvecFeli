import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import fonctions_auxiliares as aux

# Definimos las ecuaciones diferenciales
def lotkaVolterra(y, r1, r2, K1, K2, alpha12, alpha21):
    N1, N2 = y
    dN1dt = r1 * N1 * (1 - N1 / K1 - alpha12 * N2 / K1)
    dN2dt = r2 * N2 * (1 - N2 / K2 - alpha21 * N1 / K2)
    return [dN1dt, dN2dt]

# Definimos los valores iniciales
# TODO: Ajustar bien estos numeros
y0, y1, y2, y3, y4, y5, y6, y7 = [10, 10], [10, 10], [10, 10], [10, 10], [10, 10], [10, 10], [10, 10], [10, 10]

# Definimos el tiempo
t = np.linspace(0, 100, 1000)

# Resolvemos las ecuaciones diferenciales con runge kutta
rkCase0 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y0, t)
rkCase1 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y1, t)
rkCase2 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y2, t)
rkCase3 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y3, t)
rkCase4 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y4, t)
rkCase5 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y5, t)
rkCase6 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y6, t)
rkCase7 = aux.runge_kutta_4(lambda t, y: lotkaVolterra(y, 0.1, 0.1, 1000, 1000, 0.01, 0.01), y7, t)

# Graficamos las soluciones
plt.plot(t, rkCase0[:, 0], label='Especies 1')
plt.plot(t, rkCase0[:, 1], label='Especies 2')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Over Time')
plt.legend()
plt.show()

# Graficamos el campo de vectores
r1 = 0.1
r2 = 0.1
K1 = 1000
K2 = 1000
alpha12 = 0.01
alpha21 = 0.01

N1 = np.linspace(0, 1000, 20)
N2 = np.linspace(0, 1000, 20)
N1, N2 = np.meshgrid(N1, N2)
dN1dt = r1 * N1 * (1 - N1 / K1 - alpha12 * N2 / K1)
dN2dt = r2 * N2 * (1 - N2 / K2 - alpha21 * N1 / K2)
plt.quiver(N1, N2, dN1dt, dN2dt)
plt.xlabel('N1')
plt.ylabel('N2')
plt.title('Population Vector Field')
plt.show()

# Puntos de equilibrio
N1_eq = K1 * (1 - alpha21 * K2 / (r2 * K2))
N2_eq = K2 * (1 - alpha12 * K1 / (r1 * K1))
print(f'Puntos de equilibrio: ({N1_eq}, {N2_eq})')

