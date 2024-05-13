import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import fonctions_auxiliares as aux

# Definimos las ecuaciones diferenciales
def lotkaVolterra(N1, N2, r1, r2, K1, K2, alpha12, alpha21):
    dN1dt = r1 * N1 * ((K1 - N1 - alpha12 * N2) / K1)
    dN2dt = r2 * N2 * ((K2 - N2 - alpha21 * N1) / K2)
    return [dN1dt, dN2dt]

def rkSolver(ode, N1, N2, r1, r2, K1, K2, alpha12, alpha21, dt, t_end):
    return aux.rungeKutta4TwoSpecies(ode, N1, N2, r1, r2, K1, K2, alpha12, alpha21, dt, t_end)

def EquilibriumPoint(r1, r2, K1, K2, alpha12, alpha21):
    '''Calcula el punto de equilibrio del sistema de ecuaciones diferenciales'''
    N1 = K1 - alpha12 * (K2 - alpha21 * K1) / (1 - alpha12 * alpha21)
    N2 = (K2 - alpha21 * K1) / (1 - alpha12 * alpha21)
    return [N1, N2]

# Data for The Multiple Curves
d1 = [60, 60, 0.1, 0.1, 500, 500, 3, 1, 0.1, 250] # a1>a2
d2 = [60, 60, 0.1, 0.1, 500, 500, -2, 1, 0.1, 250] # a1<a2
d3 = [60, 120, 0.1, 0.1, 500, 500, 1, 1, 0.1, 250] # N01 < N02
d4 = [60, 60, 0.1, 0.1, 500, 500, 1, 1, 0.1, 250] # N01 > N02


# Graphing all the Curves
N1_values, N2_values = rkSolver(lotkaVolterra, d1[0], d1[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7], d1[8], d1[9])
N1_valuesb, N2_valuesb = rkSolver(lotkaVolterra, d2[0], d2[1], d2[2], d2[3], d2[4], d2[5], d2[6], d2[7], d2[8], d2[9])
N1_valuesc, N2_valuesc = rkSolver(lotkaVolterra, d3[0], d3[1], d3[2], d3[3], d3[4], d3[5], d3[6], d3[7], d3[8], d3[9])

# TODO: Maybe replace "N1_values" and "N2_values" with "Pandas" and "Tigers" 
# Maybe!!

# Plotting the results
#TODO descomentar
# plt.plot(N1_values, color = 'blue', label='Species 1 (a1 > a2)')
# plt.plot(N2_values, color = 'blue', label='Species 2 (a1 > a2)')
# plt.plot(N1_valuesb, color = 'red', label='Species 1 (a1 < a2)')
# plt.plot(N2_valuesb, color = 'red', label='Species 2 (a1 < a2)')
# plt.plot(N1_valuesc, color = 'green', label='Species 1 (N01 < N02)')
# plt.plot(N2_valuesc, color = 'green', label='Species 2 (N01 < N02)')
# plt.xlabel('Time')
# plt.ylabel('Population')
# plt.title('Population dynamics of two species')
# plt.legend()
# plt.show()


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

equia = EquilibriumPoint(0.1, 0.1, K1a, K2a, alpha12a, alpha21a)

# Isoclinas Part 1
isoclineN1a = K1a - alpha12a * N2a
isoclineN2a = K2a - alpha21a * N1a

#Vectores
selected_points = np.random.uniform(0, 200, size=(50, 2))

vector_dN1dt = []
vector_dN2dt = []
for point in selected_points:
    dN1dt, dN2dt = lotkaVolterra(point[0], point[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7])
    vector_dN1dt.append(dN1dt)
    vector_dN2dt.append(dN2dt)

# Normalizar los vectores para que tengan longitud unitaria
norm_vector_dN1dt = np.array(vector_dN1dt) / np.sqrt(np.array(vector_dN1dt)**2 + np.array(vector_dN2dt)**2)
norm_vector_dN2dt = np.array(vector_dN2dt) / np.sqrt(np.array(vector_dN1dt)**2 + np.array(vector_dN2dt)**2)

# Dibujar los vectores en el gráfico de isoclinas

# Graficar Part 1
plt.plot(N1a, isoclineN1a, label='Isocline of N1')
plt.plot(isoclineN2a, N2a, label='Isocline of N2')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.quiver(selected_points[:,0], selected_points[:,1], norm_vector_dN1dt, norm_vector_dN2dt, color='black', scale=30)

plt.show()

# # Parametros Part 2
# N1b = np.linspace(0, 200, 100)
# N2b = np.linspace(0, 100, 100)
# K1b = 200
# K2b = 100
# alpha12b = 2
# alpha21b = 1/2
# # Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# # Si K1 > K2, entonces [isoclina de N1 > isoclina de N2]

# # Isoclinas Part 2
# isoclineN1b = K1b - alpha12b * N2b
# isoclineN2b = K2b - alpha21b * N1b

# # Graficar Part 2
# plt.plot(N1b, isoclineN1b, label='Isocline of N1')
# plt.plot(isoclineN2b, N2b, label='Isocline of N2')
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.legend()
# plt.show()

# # Parametros Part 3
# N1c = np.linspace(0, 100, 100)
# N2c = np.linspace(0, 180, 100)
# K1c = 360
# K2c = 300
# alpha12c = 2
# alpha21c = 3

# # Isoclinas Part 3
# isoclineN1c = K1c - alpha12c * N2c
# isoclineN2c = K2c - alpha21c * N1c

# # Graficar Part 3
# plt.plot(N1c, isoclineN1c, label='Isocline of N1')
# plt.plot(isoclineN2c, N2c, label='Isocline of N2')
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.legend()
# plt.show()
# # Con alfas > 1
# # Arrancan con N1 mayor, luego N2 mayor 


# # Parametros Part 4
# N1e = np.linspace(0, 100, 100)
# N2e = np.linspace(0, 180, 100)
# K1e = 60
# K2e = 50
# alpha12e = 1/3
# alpha21e = 1/2

# # Isoclinas Part 4
# isoclineN1e = K1e - alpha12e * N2e
# isoclineN2e = K2e - alpha21e * N1e

# # Graficar Part 4
# plt.plot(N1e, isoclineN1e, label='Isocline of N1')
# plt.plot(isoclineN2e, N2e, label='Isocline of N2')
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.legend()
# plt.show()
# # Con alfas < 1
# # Empiezan al reves, y terminan al reves



# # #TODO Para el Appendix, saber que cuando ambos alfas son positivos, estas decrecen, pero si algun alfa es positivo 

# # # # Parametros Part 5
# # # N1d = np.linspace(0, 100, 100)
# # # N2d = np.linspace(0, 100, 100)
# # # K1d = 0
# # # K2d = 200
# # # alpha12d = -2
# # # alpha21d = 2

# # # # Isoclinas Part 5
# # # isoclineN1d = K1d - alpha12d * N2d
# # # isoclineN2d = K2d - alpha21d * N1d

# # # # Graficar Part 5
# # # plt.plot(N1d, isoclineN1d, label='Isocline of N1')
# # # plt.plot(isoclineN2d, N2d, label='Isocline of N2')
# # # plt.xlabel('N1')
# # # plt.ylabel('N2')
# # # plt.legend()
# # # plt.show()


