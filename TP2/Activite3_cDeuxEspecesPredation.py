#Ejercicio 3
import fonctions_auxiliares as aux
import numpy as np
import matplotlib.pyplot as plt

def PredatorPreyLotVol(t, n, p, r, a, b, q):
    dNdt = r * n - a * n * p
    dPdt = b * n * p - q * p
    return [dNdt, dPdt]

def LotkaVolterraExtODE(t, n, p, r, a, b, q, k):
    dNdT = r * n * (1 - n / k) - a * n * p
    dPdt = b * n * p - q * p
    return [dNdT, dPdt]

# Probar con estas 2 funciones de RK, despues se pasan a las auxiliares, primero probarlas aca
def rungeKuttaPredatorPrey(ode, n, p, r, a, b, q, dt, t_end):
    t = 0
    n_values = [n]
    p_values = [p]
    while t < t_end:
        k1 = ode(t, n, p, r, a, b, q)
        k2 = ode(t + 0.5 * dt, n + 0.5 * dt * k1[0], p + 0.5 * dt * k1[1], r, a, b, q)
        k3 = ode(t + 0.5 * dt, n + 0.5 * dt * k2[0], p + 0.5 * dt * k2[1], r, a, b, q)
        k4 = ode(t + dt, n + dt * k3[0], p + dt * k3[1], r, a, b, q)
        
        n += (dt / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        p += (dt / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        
        n_values.append(n)
        p_values.append(p)
        t += dt
    return n_values, p_values

def rungeKuttaLotVolExt(ode, n, p, r, a, b, q, k, dt, t_end):
    t = 0
    n_values = [n]
    p_values = [p]
    while t < t_end:
        k1 = ode(t, n, p, r, a, b, q, k)
        k2 = ode(t + 0.5 * dt, n + 0.5 * dt * k1[0], p + 0.5 * dt * k1[1], r, a, b, q, k)
        k3 = ode(t + 0.5 * dt, n + 0.5 * dt * k2[0], p + 0.5 * dt * k2[1], r, a, b, q, k)
        k4 = ode(t + dt, n + dt * k3[0], p + dt * k3[1], r, a, b, q, k)
        
        n += (dt / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        p += (dt / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        
        n_values.append(n)
        p_values.append(p)
        t += dt
    return n_values, p_values

# Runge Kutta Approximations
Pandas0 = 120  # initial population of prey species
Leopards0 = 30  # initial population of predator species
dt = 0.25 # time step size
t_end = 200 # end time

# Approximate Predator-Prey with Runge Kutta
d1 = [0.2, 0.02, 0.004, 0.2] # Normal Values
d2 = [0.2, 0.005, 0.004, 0.2] # Lower Predation Rate aka Lower a
d3 = [0.8, 0.02, 0.004, 0.2] # Higher Panda Growth Rate aka Higher r
d4 = [0.2, 0.02, 0.024, 0.2] # Lower Predator Efficiency Rate aka Lower b
d5 = [0.2, 0.02, 0.004, 0.6] # Higher Predator Death Rate aka Higher q

pandas1, leopards1 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d1[0], d1[1], d1[2], d1[3], dt, t_end)
pandas2, leopards2 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d2[0], d2[1], d2[2], d2[3], dt, t_end)
pandas3, leopards3 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d3[0], d3[1], d3[2], d3[3], dt, t_end)
pandas4, leopards4 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d4[0], d4[1], d4[2], d4[3], dt, t_end)
pandas5, leopards5 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d5[0], d5[1], d5[2], d5[3], dt, t_end)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Subplot 1
axs[0, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[0, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[0, 0].plot(pandas2, color='blue', label='Pandas (Lower a)')
axs[0, 0].plot(leopards2, color='red', label='Leopards2 (Lower a)')
axs[0, 0].set_title('Population dynamics with a Lower Predation Rate')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Population')
axs[0, 0].legend(loc='upper right')

# Subplot 2
axs[0, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[0, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[0, 1].plot(pandas3, color='blue', label='Pandas (Higher r)')
axs[0, 1].plot(leopards3, color='red', label='Leopards (Higher r)')
axs[0, 1].set_title('Population dynamics with a Higher Panda Growth Rate')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Population')
axs[0, 1].legend(loc='upper right')

# Subplot 3
axs[1, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[1, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[1, 0].plot(pandas4, color='blue', label='Pandas (Lower B)')
axs[1, 0].plot(leopards4, color='red', label='Leopards (Lower B)')
axs[1, 0].set_title('Population dynamics with a Lower Predator Efficiency Rate')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Population')
axs[1, 0].legend(loc='upper right')

# Subplot 4
axs[1, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[1, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[1, 1].plot(pandas5, color='blue', label='Pandas (Higher q)')
axs[1, 1].plot(leopards5, color='red', label='Leopards (Higher q)')
axs[1, 1].set_title('Population dynamics with a Higher Predator Death Rate')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('Population')
axs[1, 1].legend(loc='upper right')

plt.tight_layout()
plt.show()

# Approximate Lotka Volterra Extended with Runge Kutta
d1 = [0.2, 0.02, 0.004, 0.2, 200] # Normal Values
d2 = [0.2, 0.005, 0.004, 0.2, 200] # Lower Predation Rate aka Lower a
d3 = [0.8, 0.02, 0.004, 0.2, 200] # Higher Panda Growth Rate aka Higher r
d4 = [0.2, 0.02, 0.004, 0.2, 800] # Higher Carrying Capacity aka Higher K
d5 = [0.2, 0.02, 0.004, 0.2, 120] # Lower Carrying Capacity aka Lower K

pandas1, leopards1 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d1[0], d1[1], d1[2], d1[3], d1[4], dt, t_end)
pandas2, leopards2 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d2[0], d2[1], d2[2], d2[3], d2[4], dt, t_end)
pandas3, leopards3 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d3[0], d3[1], d3[2], d3[3], d3[4], dt, t_end)
pandas4, leopards4 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d4[0], d4[1], d4[2], d4[3], d4[4], dt, t_end)
pandas5, leopards5 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d5[0], d5[1], d5[2], d5[3], d5[4], dt, t_end)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Subplot 1
axs[0, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[0, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[0, 0].plot(pandas2, color='blue', label='Pandas (Lower a)')
axs[0, 0].plot(leopards2, color='red', label='Leopards2 (Lower a)')
axs[0, 0].set_title('Population dynamics with a Lower Predation Rate')
axs[0, 0].legend(loc='upper right')

# Subplot 2
axs[0, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[0, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[0, 1].plot(pandas3, color='blue', label='Pandas (Higher r)')
axs[0, 1].plot(leopards3, color='red', label='Leopards (Higher r)')
axs[0, 1].set_title('Population dynamics with a Higher Panda Growth Rate')
axs[0, 1].legend(loc='upper right')

# Subplot 3
axs[1, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[1, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[1, 0].plot(pandas4, color='blue', label='Pandas (Higher K)')
axs[1, 0].plot(leopards4, color='red', label='Leopards (Higher K)')
axs[1, 0].set_title('Population dynamics with a Higher Panda Carrying Capacity')
axs[1, 0].legend(loc='upper right')

# Subplot 4
axs[1, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
axs[1, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
axs[1, 1].plot(pandas5, color='blue', label='Pandas (Lower K)')
axs[1, 1].plot(leopards5, color='red', label='Leopards (Lower K)')
axs[1, 1].set_title('Population dynamics with a Lower Panda Carrying Capacity')
axs[1, 1].legend(loc='upper right')

plt.tight_layout()
plt.show()












#Isoclinas Cero

#Parámetros part 1
Na = np.linspace(0, 10, 10)
Pa = np.linspace(0, 10, 10)
alphaa = 10
betaa = 10
ra = 0.1
qa = 0.1
alphaa = 0.1
betaa = 0.1

#Isoclinas predador-presa
isocline_Na = np.full_like(Na, qa/betaa)
isocline_Pa = np.full_like(Pa, ra/alphaa)

# ENcontrar pnuto de equilibrio
equiPointA = aux.findEquilibriumPredatorPrey(alphaa, betaa, ra, qa)
eq1, eq1b = equiPointA[0], equiPointA[1]

#campo de vectores
vN = np.linspace(0, 10, 40)
vP = np.linspace(0, 10, 40)
VN, VP = np.meshgrid(vN, vP)

dN = ra * VN - alphaa * VN * VP
dP = alphaa * VN * VP - qa * VP

#Trayectoria con runge kutta
Na_values_1, Pa_values_1 = rungeKuttaPredatorPrey(PredatorPreyLotVol, 5, 1, ra, alphaa, betaa, qa, 0.1, 1000)
Na_values_2, Pa_values_2 = rungeKuttaPredatorPrey(PredatorPreyLotVol, 1.5, 1.5, ra, alphaa, betaa, qa, 0.1, 1000)
Na_values_3, Pa_values_3 = rungeKuttaPredatorPrey(PredatorPreyLotVol, 8, 0.6, ra, alphaa, betaa, qa, 0.1, 1000)

#Graficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))  # Crear una figura con 2 gráficos uno al lado del otro

# Primer gráfico en ax1
ax1.plot(Na, isocline_Na, label='Isocline of Pandas', color='indigo', linewidth=2, linestyle='--')
ax1.plot(isocline_Pa, Pa, label='Isocline of Leopardos', color='limegreen', linewidth=2, linestyle='--')
ax1.set_xlabel('P')
ax1.set_ylabel('L')
ax1.plot(Na_values_1, Pa_values_1, color='deeppink', label='Trayectoria 1')
ax1.plot(Na_values_2, Pa_values_2, color='hotpink', label='Trayectoria 2')
ax1.plot(Na_values_3, Pa_values_3, color='mediumvioletred', label='Trayectoria 3')
ax1.set_title('Isoclines of Depredador y Presa')
ax1.scatter(eq1, eq1b, color='red', label='Punto de Equilibrio', s=100, zorder=10)
ax1.streamplot(vN, vP, dN, dP, color='gray', density=1, arrowstyle='->', linewidth=0.7)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.legend()

# Segundo gráfico en ax2
ax2.plot(Na_values_1, label='P- Trayectoria 1', color='orangered')
ax2.plot(Na_values_3, label='P - Trayectoria 3', color='gold')
ax2.plot(Pa_values_1, label='L - Trayectoria 1', color='coral')
ax2.plot(Pa_values_3, label='L - Trayectoria 3', color='khaki')
ax2.set_xlabel('Time')
ax2.set_ylabel('N')
ax2.set_title('Trajectories of Predator-Prey')
ax2.legend()

# Mostrar ambos gráficos
plt.tight_layout()
plt.show()

#Parametros part2 LVE
#Caso 1
Nb = np.linspace(0, 10, 10)
Pb = np.linspace(0, 10, 10)
rb = 0.5
qb = 0.5
alphab = 0.3
betab = 0.3
k = 10

#Isoclinas LVE
isocline_Nlve = np.full_like(Nb, qb/betab)
isocline_Plve = (rb/alphab) * (1 - Nb/k)

# Calculate the equilibrium point
eq2xAxis = qb / betab
eq2yAxis = (rb / alphab) * (1 - eq2xAxis / k)

#campo de vectores
vN = np.linspace(0, 10, 40)
vP = np.linspace(0, 10, 40)
VN, VP = np.meshgrid(vN, vP)

dN = rb * VN * (1 - VN/k) - alphab * VN * VP
dP = alphab * VN * VP - qb * VP

#Trayectoria con runge kutta
Nb_values_1, Pb_values_1 = rungeKuttaLotVolExt(LotkaVolterraExtODE, 5, 5, rb, alphab, betab, qb, k, 0.1, 150)

#Graficar las isoclinas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Primer gráfico (Isoclinas)
ax1.plot(isocline_Nlve, Nb, label='Isoclina de Pandas', color = 'indigo', linestyle='--', linewidth=2)
ax1.plot(Nb, isocline_Plve, label='Isoclina de Leopardos', color = 'limegreen', linestyle='--', linewidth=2)
ax1.set_xlabel('P')
ax1.set_ylabel('L')
ax1.set_title('Isoclinas de Lotka-Volterra Extendido')
ax1.plot(Nb_values_1, Pb_values_1, color = 'violet', label='Trajectoria')
ax1.scatter(eq2xAxis, eq2yAxis, color='red', label='Punto de Equilibrio', s=100, zorder=10)
ax1.streamplot(vN, vP, dN, dP, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.legend(loc='upper right')

Segundo gráfico (Trayectorias)
ax2.plot(Nb_values_1, label='P - Trayectoria 1', color = 'violet')
ax2.plot(Pb_values_1, label='L - Trayectoria 1', color = 'darkviolet')
# TODO agregar otra trayectoria
ax2.set_xlabel('Time')
ax2.set_ylabel('N')
ax2.set_title('Trajectories of Lotka-Volterra Extended')
ax2.legend()

Ajustar el diseño
plt.tight_layout()
plt.show()







# 


#Graficar las ODE a través del tiempo
#Primero graficamos dNdt

#parámetros1
r1 = 0.1
alpha1 = 10
beta1 = 10
q1 = 0.1
N = 5
P = 1

#graficar dNdt a traves del tiempo
t = np.linspace(0, 100, 100)
# N = np.linspace(0, 10, 10)
# P = np.linspace(0, 10, 10)

dNdt = r1 * N - alpha1 * N * P

plt.plot(t, dNdt)
plt.xlabel('Time')
plt.ylabel('dN/dt')
plt.title('dN/dt over time')


# Parameters
r1 = 0.1
alpha1 = 10
beta1 = 10
q1 = 0.1
N = 5
P = 1

# Time array
t = np.linspace(0, 100, 100)

# Function to calculate dNdt
def calculate_dNdt(N, P, r1, alpha1):
    return r1 * N - alpha1 * N * P

# Calculate dNdt over time
dNdt = np.array([calculate_dNdt(N, P, r1, alpha1) for _ in t])

# Plotting
plt.plot(t, dNdt)
plt.xlabel('Time')
plt.ylabel('dN/dt')
plt.title('dN/dt over time')
plt.show()
