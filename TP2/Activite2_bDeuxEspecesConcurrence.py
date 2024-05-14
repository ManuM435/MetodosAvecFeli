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

# Data for Graph Part 1 
# TODO Convertirlos en una figura con 2 subplots
d1 = [60, 60, 0.1, 0.1, 500, 500, 3, 1, 0.1, 250] # aP > aT
d2 = [100, 60, 0.1, 0.1, 500, 500, 1, 1, 0.1, 250] # N0P > N0T

# Data for Graph Part 2
# TODO COnvertirlos en una figura con 2 subplots
d3 = [60, 60, 0.1, 0.5, 500, 500, 1, 1, 0.1, 250] # rP > rT
d4 = [60, 60, 0.1, 0.1, 200, 800, 1, 1, 0.1, 250] # KP > KT


# Graphing all the Curves
pandas1, turtles1 = rkSolver(lotkaVolterra, d1[0], d1[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7], d1[8], d1[9])
pandas2, turtles2 = rkSolver(lotkaVolterra, d2[0], d2[1], d2[2], d2[3], d2[4], d2[5], d2[6], d2[7], d2[8], d2[9])

pandas3, turtles3 = rkSolver(lotkaVolterra, d3[0], d3[1], d3[2], d3[3], d3[4], d3[5], d3[6], d3[7], d3[8], d3[9])
pandas4, turtles4 = rkSolver(lotkaVolterra, d4[0], d4[1], d4[2], d4[3], d4[4], d4[5], d4[6], d4[7], d4[8], d4[9])

# Plotting the results Part 1
#TODO descomentar
# plt.plot(pandas1, color = 'blue', label='Pandas (a1 > a2)')
# plt.plot(turtles1, color = 'blue', label='Turtles (a1 > a2)')
# plt.plot(pandas2, color = 'red', label='Pandas (N0P > N0T)')
# plt.plot(turtles2, color = 'red', label='Turtles (N0P > N0T)')
# plt.xlabel('Time')
# plt.ylabel('Population')
# plt.title('Population dynamics of two species')
# plt.legend()
# plt.show()

# Plotting the results Part 2









# # Isoclinas Cero
r1 = 0.1
r2 = 0.1

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

#vectores
N1_values = np.linspace(0, 100, num=18)
N2_values = np.linspace(0, 200, num=18)

N1, N2 = np.meshgrid(N1_values, N2_values)

def dN1_values(N1, N2):
    return r1 * N1 * ((K1a - N1 - alpha12a * N2) / K1a)

def dN2_values(N1, N2):
    return r2 * N2 * ((K2a - N2 - alpha21a * N1) / K2a)

dN1_values = dN1_values(N1, N2)
dN2_values = dN2_values(N1, N2)

# Normaliza el campo vectorial para que todos los vectores tengan la misma longitud
magnitude = np.sqrt(dN1_values**2 + dN2_values**2)
dN1_values /= magnitude
dN2_values /= magnitude

# Graficar Part 1
plt.plot(N1a, isoclineN1a, label='Isocline of N1', color = 'crimson')
plt.plot(isoclineN2a, N2a, label='Isocline of N2', color = 'limegreen')
plt.xlabel('N1')
plt.ylabel('N2')
plt.quiver(N1_values, N2_values, dN1_values, dN2_values, angles='xy')
plt.xlim(0, K1a)
plt.ylim(0, K2a)
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

#vectores
N1_valuesb = np.linspace(0, 100, num=18)
N2_valuesb = np.linspace(0, 200, num=18)

N1b, N2b = np.meshgrid(N1_valuesb, N2_valuesb)

def dN1_valuesb(N1, N2):
    return r1 * N1 * ((K1b - N1 - alpha12b * N2) / K1b)

def dN2_valuesb(N1, N2):
    return r2 * N2 * ((K2b - N2 - alpha21b * N1) / K2b)

dN1_valuesb = dN1_valuesb(N1b, N2b)
dN2_valuesb = dN2_valuesb(N1b, N2b)

# Normaliza el campo vectorial para que todos los vectores tengan la misma longitud
magnitude = np.sqrt(dN1_valuesb**2 + dN2_valuesb**2)
dN1_valuesb /= magnitude
dN2_valuesb /= magnitude

# Graficar Part 2
#TODO desocmentar
plt.plot(N1b, isoclineN1b, label='Isocline of N1', color = 'indigo')
plt.plot(isoclineN2b, N2b, label='Isocline of N2', color = 'limegreen')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.quiver(N1_valuesb, N2_valuesb, dN1_valuesb, dN2_valuesb, angles='xy')
plt.show()

# # Parametros Part 3
# N1c = np.linspace(0, 50, 100)
# N2c = np.linspace(0, 50, 100)
# K1c = 100
# K2c = 100
# alpha12c = 2
# alpha21c = 2

# # Isoclinas Part 3
# isoclineN1c = K1c - alpha12c * N2c
# isoclineN2c = K2c - alpha21c * N1c
# EquiPointC = [K1c/(1+alpha12c), K2c/(1+alpha21c)]

# # Vectores
# x3 = np.linspace(0, 100, num=20)
# y3 = np.linspace(0, 100, num=20)

# X3, Y3 = np.meshgrid(x3, y3)

# selected_points3 = np.vstack([X3.ravel(), Y3.ravel()]).T
# vector_dN1dt3 = []
# vector_dN2dt3 = []

# for point in selected_points3:
#     dN1dt3, dN2dt3 = lotkaVolterra(point[0], point[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7])
#     vector_dN1dt3.append(dN1dt3)
#     vector_dN2dt3.append(dN2dt3)

# # Normalizar los vectores para que tengan longitud unitaria
# norm_vector_dN1dt3 = np.array(vector_dN1dt3) / np.sqrt(np.array(vector_dN1dt3)**2 + np.array(vector_dN2dt3)**2)
# norm_vector_dN2dt3 = np.array(vector_dN2dt3) / np.sqrt(np.array(vector_dN1dt3)**2 + np.array(vector_dN2dt3)**2)

# # Graficar Part 3
# plt.plot(N1c, isoclineN1c, label='Isocline of N1')
# plt.plot(isoclineN2c, N2c, label='Isocline of N2')
# plt.scatter(EquiPointC[0], EquiPointC[1], color='red', label='Intersection Point')
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.legend()
# plt.quiver(selected_points3[:,0], selected_points3[:,1], norm_vector_dN1dt3, norm_vector_dN2dt3, color='black', scale=30, width=0.0025)
# plt.show()
# # Con alfas > 1
# # Arrancan con N1 mayor, luego N2 mayor 

# # Parametros Part 4
# N1e = np.linspace(0, 150, 100)
# N2e = np.linspace(0, 150, 100)
# K1e = 100
# K2e = 100
# alpha12e = 2/3
# alpha21e = 2/3

# # Isoclinas Part 4
# isoclineN1e = K1e - alpha12e * N2e
# isoclineN2e = K2e - alpha21e * N1e
# EquiPointE = [K1e/(1+alpha12e), K2e/(1+alpha21e)]

# #vectores
# x4 = np.linspace(0, 150, num=20)
# y4 = np.linspace(0, 150, num=20)

# X4, Y4 = np.meshgrid(x4, y4)

# selected_points4 = np.vstack([X4.ravel(), Y4.ravel()]).T
# vector_dN1dt4 = []
# vector_dN2dt4 = []
# for point in selected_points4:
#     dN1dt4, dN2dt4 = lotkaVolterra(point[0], point[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7])
#     vector_dN1dt4.append(dN1dt4)
#     vector_dN2dt4.append(dN2dt4)

# # Normalizar los vectores para que tengan longitud unitaria
# norm_vector_dN1dt4 = np.array(vector_dN1dt4) / np.sqrt(np.array(vector_dN1dt4)**2 + np.array(vector_dN2dt4)**2)
# norm_vector_dN2dt4 = np.array(vector_dN2dt4) / np.sqrt(np.array(vector_dN1dt4)**2 + np.array(vector_dN2dt4)**2)

# # Graficar Part 4
# plt.plot(N1e, isoclineN1e, label='Isocline of N1', color = 'indigo')
# plt.plot(isoclineN2e, N2e, label='Isocline of N2', color = 'limegreen')
# plt.scatter(EquiPointE[0], EquiPointE[1], color='red', label='Intersection Point')
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.quiver(selected_points4[:,0], selected_points4[:,1], norm_vector_dN1dt4, norm_vector_dN2dt4, color='black', scale=30, width=0.0025)
# plt.legend()
# plt.show()
# Con alfas < 1
# Empiezan al reves, y terminan al reves