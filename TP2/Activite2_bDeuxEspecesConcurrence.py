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
d1 = [60, 60, 0.1, 0.1, 500, 500, 3, 1, 0.1, 250] # aP > aT
d2 = [60, 60, 0.1, 0.1, 500, 500, 1, 1, 0.1, 250] # N0P > N0T

# Data for Graph Part 2

d3 = [60, 60, 0.1, 0.5, 500, 500, 1, 1, 0.1, 250] # rP > rT
d4 = [60, 60, 0.1, 0.1, 200, 800, 1, 1, 0.1, 250] # KP > KT


# Graphing all the Curves
pandas1, turtles1 = rkSolver(lotkaVolterra, d1[0], d1[1], d1[2], d1[3], d1[4], d1[5], d1[6], d1[7], d1[8], d1[9])
pandas2, turtles2 = rkSolver(lotkaVolterra, d2[0], d2[1], d2[2], d2[3], d2[4], d2[5], d2[6], d2[7], d2[8], d2[9])



# Plotting the results Part 1
plt.plot(pandas1, color = 'blue', label='Pandas (a1 > a2)')
plt.plot(turtles1, color = 'blue', label='Turtles (a1 > a2)')
plt.plot(pandas2, color = 'red', label='Pandas (N0P > N0T)')
plt.plot(turtles2, color = 'red', label='Turtles (N0P > N0T)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population dynamics of two species')
plt.legend()
plt.show()

# Plotting the results Part 2











# # Isoclinas Cero
r1 = 0.1
r2 = 0.1

# Parametros Part 1
N1a = np.linspace(0, 100, 100)
N2a = np.linspace(0, 200, 100)
K1a = 30
K2a = 50
alpha12a = 3/2
alpha21a = 1

# Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# Si K2 > K1, entonces [isoclina de N2 > isoclina de N1]

# Isoclinas Part 1
isoclineN1a = K1a/alpha12a - 1/alpha12a * N1a
isoclineN2a = K2a - alpha21a * N1a

#vectores
vn1 = np.linspace(0, 100, 40)
vn2 = np.linspace(0, 100, 40)
VN1, VN2 = np.meshgrid(vn1, vn2)

dN1 = r1 * VN1 * (K1a - VN1 - alpha12a * VN2) / K1a
dN2 = r2 * VN2 * (K2a - VN2 - alpha21a * VN1) / K2a

#Trayectoria con runge kutta 
#def rkSolver(ode, N1, N2, r1, r2, K1, K2, alpha12, alpha21, dt, t_end):
N1a_values_1, N2a_values_1 = rkSolver(lotkaVolterra, 80, 80, r1, r2, K1a, K2a, alpha12a, alpha21a, 0.1, 100)
N1a_values_2, N2a_values_2 = rkSolver(lotkaVolterra, 2, 2, r1, r2, K1a, K2a, alpha12a, alpha21a, 0.1, 100)
N1a_values_3, N2a_values_3 = rkSolver(lotkaVolterra, 40, 5, r1, r2, K1a, K2a, alpha12a, alpha21a, 0.1, 100)

# Graficar Part 1
plt.plot(N1a, isoclineN1a, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
plt.plot(N1a, isoclineN2a, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
plt.plot(N1a_values_1, N2a_values_1, color = 'red', label='Trajectory 1')
plt.plot(N1a_values_2, N2a_values_2, color = 'dodgerblue', label='Trajectory 2')
plt.plot(N1a_values_3, N2a_values_3, color = 'deeppink', label='Trajectory 3')
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()

# # Parametros Part 2
N1b = np.linspace(0, 200, 100)
N2b = np.linspace(0, 100, 100)
K1b = 50
K2b = 30
alpha12b = 1
alpha21b = 3/2
# Si los alpha son inversos, la pendiente es la misma (entonces el que tiene K mas grande va a ser siempre mas grande)
# Si K1 > K2, entonces [isoclina de N1 > isoclina de N2]

# Isoclinas Part 2
# isoclineN1a = K1a/alpha12a - 1/alpha12a * N1a
isoclineN1b = K1b/alpha12b - 1/alpha12b * N1b
isoclineN2b = K2b - alpha21b * N1b

#vectores
vn1 = np.linspace(0, 100, 40)
vn2 = np.linspace(0, 100, 40)
VN1, VN2 = np.meshgrid(vn1, vn2)

dN1 = r1 * VN1 * (K1b - VN1 - alpha12b * VN2) / K1b
dN2 = r2 * VN2 * (K2b - VN2 - alpha21b * VN1) / K2b

#Trayectoria con runge kutta
N1b_values_1, N2b_values_1 = rkSolver(lotkaVolterra, 77, 77, r1, r2, K1b, K2b, alpha12b, alpha21b, 0.1, 100)
N1b_values_2, N2b_values_2 = rkSolver(lotkaVolterra, 2, 2, r1, r2, K1b, K2b, alpha12b, alpha21b, 0.1, 100)
N1b_values_3, N2b_values_3 = rkSolver(lotkaVolterra, 2, 40, r1, r2, K1b, K2b, alpha12b, alpha21b, 0.1, 100)

# Graficar Part 2
plt.plot(N1b, isoclineN1b, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
plt.plot(N1b, isoclineN2b, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
plt.plot(N1b_values_1, N2b_values_1, color = 'red', label='Trajectory 1')
plt.plot(N1b_values_2, N2b_values_2, color = 'dodgerblue', label='Trajectory 2')
plt.plot(N1b_values_3, N2b_values_3, color = 'deeppink', label='Trajectory 3')
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()

# Parametros Part 3
N1c = np.linspace(0, 50, 100)
N2c = np.linspace(0, 50, 100)
K1c = 100
K2c = 100
alpha12c = 2
alpha21c = 2

# Isoclinas Part 3
isoclineN1c = K1c - alpha12c * N2c
isoclineN2c = K2c - alpha21c * N1c
EquiPointC = [K1c/(1+alpha12c), K2c/(1+alpha21c)]

# Vectores
vn1 = np.linspace(0, 120, 20)
vn2 = np.linspace(0, 120, 20)
VN1, VN2 = np.meshgrid(vn1, vn2)

dN1 = r1 * VN1 * (K1c - VN1 - alpha12c * VN2) / K1c
dN2 = r2 * VN2 * (K2c - VN2 - alpha21c * VN1) / K2c

# Trayectoria con runge kutta
N1c_values_1, N2c_values_1 = rkSolver(lotkaVolterra, 80, 118, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 100)
N1c_values_2, N2c_values_2 = rkSolver(lotkaVolterra, 20, 5, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 100)
N1c_values_3, N2c_values_3 = rkSolver(lotkaVolterra, 2, 20, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 100)
N1c_values_4, N2c_values_4 = rkSolver(lotkaVolterra, 115, 60, r1, r2, K1c, K2c, alpha12c, alpha21c, 0.1, 100)

# Graficar Part 3
plt.plot(N1c, isoclineN1c, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
plt.plot(isoclineN2c, N2c, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
plt.scatter(EquiPointC[0], EquiPointC[1], color='red', label='Punto De Equilibrio (Inestable)')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
plt.plot(N1c_values_1, N2c_values_1, color = 'red', label='Trajectory 1')
plt.plot(N1c_values_2, N2c_values_2, color = 'dodgerblue', label='Trajectory 2')
plt.plot(N1c_values_3, N2c_values_3, color = 'deeppink', label='Trajectory 3')
plt.plot(N1c_values_4, N2c_values_4, color = 'orange', label='Trajectory 4')
plt.xlim(0,120)
plt.ylim(0,120)
plt.show()
# Con alfas > 1
# Arrancan con N1 mayor, luego N2 mayor 

# Parametros Part 4
N1e = np.linspace(0, 150, 100)
N2e = np.linspace(0, 150, 100)
K1e = 100
K2e = 100
alpha12e = 2/3
alpha21e = 2/3

# Isoclinas Part 4
isoclineN1e = K1e - alpha12e * N2e
isoclineN2e = K2e - alpha21e * N1e
EquiPointE = [K1e/(1+alpha12e), K2e/(1+alpha21e)]

#vectores
vn1 = np.linspace(0, 200, 40)
vn2 = np.linspace(0, 200, 40)
VN1, VN2 = np.meshgrid(vn1, vn2)

dN1 = r1 * VN1 * (K1e - VN1 - alpha12e * VN2) / K1e
dN2 = r2 * VN2 * (K2e - VN2 - alpha21e * VN1) / K2e

# Trayectoria con runge kutta
N1e_values_1, N2e_values_1 = rkSolver(lotkaVolterra, 75, 198, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 100)
N1e_values_2, N2e_values_2 = rkSolver(lotkaVolterra, 3, 20, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 100)
N1e_values_3, N2e_values_3 = rkSolver(lotkaVolterra, 125, 3, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 100)
N1e_values_4, N2e_values_4 = rkSolver(lotkaVolterra, 198, 50, r1, r2, K1e, K2e, alpha12e, alpha21e, 0.1, 100)

# Graficar Part 4
plt.plot(N1e, isoclineN1e, label='Isocline of N1', color = 'indigo', linewidth=2.5, linestyle='--')
plt.plot(isoclineN2e, N2e, label='Isocline of N2', color = 'limegreen', linewidth=2.5, linestyle='--')
plt.scatter(EquiPointE[0], EquiPointE[1], color='red', label='Punto de Equilibrio (Estable)')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()
plt.streamplot(vn1, vn2, dN1, dN2, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
plt.plot(N1e_values_1, N2e_values_1, color = 'red', label='Trajectory 1')
plt.plot(N1e_values_2, N2e_values_2, color = 'dodgerblue', label='Trajectory 2')
plt.plot(N1e_values_3, N2e_values_3, color = 'deeppink', label='Trajectory 3')
plt.plot(N1e_values_4, N2e_values_4, color = 'orange', label='Trajectory 4')
plt.xlim(0,200)
plt.ylim(0,200)
plt.show()
# # Con alfas < 1
# Empiezan al reves, y terminan al reves


