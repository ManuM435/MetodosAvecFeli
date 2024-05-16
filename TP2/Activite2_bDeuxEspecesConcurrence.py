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

# Data for Graphs
h = 0.1
# el sexto es turtles over pandas, el septimo es pandas over turtles
t = 250
d0 = [100, 60, 0.2, 0.1, 550, 500, 2, 1] # Normal
d1 = [100, 60, 0.2, 0.1, 550, 500, 2, 2.5] # aP > aT
d2 = [300, 60, 0.2, 0.1, 550, 500, 2, 1] # N0T > N0P
d3 = [100, 60, 0.6, 0.1, 550, 500, 2, 1] # rT > rP
d4 = [100, 60, 0.2, 0.1, 750, 500, 2, 1] # KP > KT

# Creating the Curves
pandas0, turtles0 = rkSolver(lotkaVolterra, d0[0], d0[1], d0[2], d0[3], d0[4], d0[5], d0[6], d0[7], h, t) # Normal
pandas1, turtles1 = rkSolver(lotkaVolterra, d1[0], d1[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7], h, t) # aP > aT
pandas2, turtles2 = rkSolver(lotkaVolterra, d2[0], d2[1], d2[2], d2[3], d2[4], d2[5], d2[6], d2[7], h, t) # N0P > N0T
pandas3, turtles3 = rkSolver(lotkaVolterra, d3[0], d3[1], d3[2], d3[3], d3[4], d3[5], d3[6], d3[7], h, t) # rP > rT
pandas4, turtles4 = rkSolver(lotkaVolterra, d4[0], d4[1], d4[2], d4[3], d4[4], d4[5], d4[6], d4[7], h, t) # KP > KT

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Subplot 1
axs[0, 0].plot(pandas0, color='indigo', linestyle=':', alpha=0.7, label='Pandas (Default)')
axs[0, 0].plot(turtles0, color='darkred', linestyle=':', alpha=0.7, label='Turtles (Defualt)')
axs[0, 0].plot(pandas1, color='navy', label='Pandas (Higher aP)')
axs[0, 0].plot(turtles1, color='orangered', label='Turtles (Higher aP)')
axs[0, 0].set_title('Pop. Dynamics with higher Panda Competition')
axs[0, 0].legend(loc='upper right')

# Subplot 2
axs[0, 1].plot(pandas0, color='indigo', linestyle=':', alpha=0.7, label='Pandas (Default)')
axs[0, 1].plot(turtles0, color='darkred', linestyle=':', alpha=0.7, label='Turtles (Defualt)')
axs[0, 1].plot(pandas2, color='navy', label='Pandas (Higher N0P)')
axs[0, 1].plot(turtles2, color='orangered', label='Turtles (Higher N0P)')
axs[0, 1].set_title('Pop. Dynamics with even higher Panda Init. Population')
axs[0, 1].legend(loc='upper right')

# Subplot 3
axs[1, 0].plot(pandas0, color='indigo', linestyle=':', alpha=0.7, label='Pandas (Default)')
axs[1, 0].plot(turtles0, color='darkred', linestyle=':', alpha=0.7, label='Turtles (Defualt)')
axs[1, 0].plot(pandas3, color='navy', label='Pandas (Higher rP)')
axs[1, 0].plot(turtles3, color='orangered', label='Turtles (Higher rP)')
axs[1, 0].set_title('Pop. Dynamics with Even Higher Panda Growth Rate')
axs[1, 0].legend(loc='upper right')

# Subplot 4
axs[1, 1].plot(pandas0, color='indigo', linestyle=':', alpha=0.7, label='Pandas (Default)')
axs[1, 1].plot(turtles0, color='darkred', linestyle=':', alpha=0.7, label='Turtles (Defualt)')
axs[1, 1].plot(pandas4, color='navy', label='Pandas (Higher KP)')
axs[1, 1].plot(turtles4, color='orangered', label='Turtles (Lower KT)')
axs[1, 1].set_title('Pop. Dynamics with even Higher Panda Carrying Capacity')
axs[1, 1].legend(loc='upper right')

plt.tight_layout()
plt.show()



# # Isoclinas Cero
# r1 = 0.1
# r2 = 0.1

# # Parametros Part 1
# N1a = np.linspace(0, 100, 100)
# N2a = np.linspace(0, 200, 100)
# K1a = 30
# K2a = 50
# alpha12a = 3/2
# alpha21a = 1

# # Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# # Si K2 > K1, entonces [isoclina de N2 > isoclina de N1]

# # Isoclinas Part 1
# isoclineN1a = K1a/alpha12a - 1/alpha12a * N1a
# isoclineN2a = K2a - alpha21a * N1a
# EquiPointA = [0, K2a]

# #vectores
# vn1 = np.linspace(0, 100, 40)
# vn2 = np.linspace(0, 100, 40)
# VN1, VN2 = np.meshgrid(vn1, vn2)

# dN1 = r1 * VN1 * (K1a - VN1 - alpha12a * VN2) / K1a
# dN2 = r2 * VN2 * (K2a - VN2 - alpha21a * VN1) / K2a

# #Trayectoria con runge kutta 
# #def rkSolver(ode, N1, N2, r1, r2, K1, K2, alpha12, alpha21, dt, t_end):
# N1a_values_1, N2a_values_1 = rkSolver(lotkaVolterra, 80, 80, r1, r2, K1a, K2a, alpha12a, alpha21a, 0.1, 200)
# N1a_values_2, N2a_values_2 = rkSolver(lotkaVolterra, 2, 2, r1, r2, K1a, K2a, alpha12a, alpha21a, 0.1, 200)
# N1a_values_3, N2a_values_3 = rkSolver(lotkaVolterra, 40, 5, r1, r2, K1a, K2a, alpha12a, alpha21a, 0.1, 200)

# # Graficar Part 1
# plt.plot(N1a, isoclineN1a, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
# plt.plot(N1a, isoclineN2a, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
# plt.scatter(EquiPointA[0], EquiPointA[1], color='red', label='Punto De Equilibrio (Estable)', zorder=10)
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.title('Isoclinas (Caso Pandas Dominante)')
# plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
# plt.plot(N1a_values_1, N2a_values_1, color = 'darksalmon', label='Trayectoria 1')
# plt.plot(N1a_values_2, N2a_values_2, color = 'coral', label='Trayectoria 2')
# plt.plot(N1a_values_3, N2a_values_3, color = 'orangered', label='Trayectoria 3')
# plt.legend(loc='upper right')
# plt.xlim(0,80)
# plt.ylim(0,80)
# plt.show()

# # # Parametros Part 2
# N1b = np.linspace(0, 200, 100)
# N2b = np.linspace(0, 100, 100)
# K1b = 50
# K2b = 30
# alpha12b = 1
# alpha21b = 3/2
# # Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# # Si K1 > K2, entonces [isoclina de N1 > isoclina de N2]

# # Isoclinas Part 2
# # isoclineN1a = K1a/alpha12a - 1/alpha12a * N1a
# isoclineN1b = K1b/alpha12b - 1/alpha12b * N1b
# isoclineN2b = K2b - alpha21b * N1b
# EquiPointB = [K1b, 0]

# #vectores
# vn1 = np.linspace(0, 100, 40)
# vn2 = np.linspace(0, 100, 40)
# VN1, VN2 = np.meshgrid(vn1, vn2)

# dN1 = r1 * VN1 * (K1b - VN1 - alpha12b * VN2) / K1b
# dN2 = r2 * VN2 * (K2b - VN2 - alpha21b * VN1) / K2b

# #Trayectoria con runge kutta
# N1b_values_1, N2b_values_1 = rkSolver(lotkaVolterra, 77, 77, r1, r2, K1b, K2b, alpha12b, alpha21b, 0.1, 200)
# N1b_values_2, N2b_values_2 = rkSolver(lotkaVolterra, 2, 2, r1, r2, K1b, K2b, alpha12b, alpha21b, 0.1, 200)
# N1b_values_3, N2b_values_3 = rkSolver(lotkaVolterra, 2, 40, r1, r2, K1b, K2b, alpha12b, alpha21b, 0.1, 200)

# # Graficar Part 2
# plt.plot(N1b, isoclineN1b, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
# plt.plot(N1b, isoclineN2b, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
# plt.scatter(EquiPointB[0], EquiPointB[1], color='red', label='Punto De Equilibrio (Estable)', zorder=10)
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.title('Isoclinas (Caso Tortugas Dominante)')
# plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
# plt.plot(N1b_values_1, N2b_values_1, color = 'orchid', label='Trayectoria 1')
# plt.plot(N1b_values_2, N2b_values_2, color = 'mediumorchid', label='Trayectoria 2')
# plt.plot(N1b_values_3, N2b_values_3, color = 'darkorchid', label='Trayectoria 3')
# plt.legend(loc='upper right')
# plt.xlim(0,80)
# plt.ylim(0,80)
# plt.show()

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
# EquiPointC1 = [0, K2c]
# EquiPointC2 = [K1c, 0]
# EquiPointC3 = [K1c/(1+alpha12c), K2c/(1+alpha21c)]

# # Vectores
# vn1 = np.linspace(0, 120, 20)
# vn2 = np.linspace(0, 120, 20)
# VN1, VN2 = np.meshgrid(vn1, vn2)

# dN1 = r1 * VN1 * (K1c - VN1 - alpha12c * VN2) / K1c
# dN2 = r2 * VN2 * (K2c - VN2 - alpha21c * VN1) / K2c

# # Trayectoria con runge kutta
# N1c_values_1, N2c_values_1 = rkSolver(lotkaVolterra, 80, 118, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 200)
# N1c_values_2, N2c_values_2 = rkSolver(lotkaVolterra, 20, 5, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 200)
# N1c_values_3, N2c_values_3 = rkSolver(lotkaVolterra, 2, 20, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 200)
# N1c_values_4, N2c_values_4 = rkSolver(lotkaVolterra, 115, 60, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 200)

# # Graficar Part 3
# plt.plot(N1c, isoclineN1c, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
# plt.plot(isoclineN2c, N2c, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
# plt.scatter(EquiPointC1[0], EquiPointC1[1], color='red', label='Punto De Equilibrio 1 (Estable)', zorder=10)
# plt.scatter(EquiPointC2[0], EquiPointC2[1], color='red', label='Punto De Equilibrio 2 (Estable)', zorder=10)
# plt.scatter(EquiPointC3[0], EquiPointC3[1], color='maroon', label='Punto De Equilibrio 3 (Inestable)', zorder=10)
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.title('Isoclinas (Caso Interseccion Inestable)')
# plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
# plt.plot(N1c_values_1, N2c_values_1, color = 'hotpink', label='Trayectoria 1')
# plt.plot(N1c_values_2, N2c_values_2, color = 'deeppink', label='Trayectoria 2')
# plt.plot(N1c_values_3, N2c_values_3, color = 'mediumvioletred', label='Trayectoria 3')
# plt.plot(N1c_values_4, N2c_values_4, color = 'darkmagenta', label='Trayectoria 4')
# plt.legend(loc='upper right')
# plt.xlim(0,120)
# plt.ylim(0,120)
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
# vn1 = np.linspace(0, 200, 40)
# vn2 = np.linspace(0, 200, 40)
# VN1, VN2 = np.meshgrid(vn1, vn2)

# dN1 = r1 * VN1 * (K1e - VN1 - alpha12e * VN2) / K1e
# dN2 = r2 * VN2 * (K2e - VN2 - alpha21e * VN1) / K2e

# # Trayectoria con runge kutta
# N1e_values_1, N2e_values_1 = rkSolver(lotkaVolterra, 75, 198, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 200)
# N1e_values_2, N2e_values_2 = rkSolver(lotkaVolterra, 3, 20, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 200)
# N1e_values_3, N2e_values_3 = rkSolver(lotkaVolterra, 125, 3, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 200)
# N1e_values_4, N2e_values_4 = rkSolver(lotkaVolterra, 198, 50, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 200)

# # Graficar Part 4
# plt.plot(N1e, isoclineN1e, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
# plt.plot(isoclineN2e, N2e, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
# plt.scatter(EquiPointE[0], EquiPointE[1], color='red', label='Punto de Equilibrio (Estable)', zorder=10)
# plt.xlabel('N1')
# plt.ylabel('N2')
# plt.title('Isoclinas (Caso Interseccion Estable)')
# plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
# plt.plot(N1e_values_1, N2e_values_1, color = 'lightsteelblue', label='Trayectoria 1')
# plt.plot(N1e_values_2, N2e_values_2, color = 'cornflowerblue', label='Trayectoria 2')
# plt.plot(N1e_values_3, N2e_values_3, color = 'royalblue', label='Trayectoria 3')
# plt.plot(N1e_values_4, N2e_values_4, color = 'steelblue', label='Trayectoria 4')
# plt.legend(loc='upper right')
# plt.xlim(0,200)
# plt.ylim(0,200)
# plt.show()
# # # Con alfas < 1
# # Empiezan al reves, y terminan al reves


