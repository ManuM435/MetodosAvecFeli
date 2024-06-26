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
dt = 0.1 # time step size
t_end = 150 # end time

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
axs[0, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Red Pandas (Default)')
axs[0, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[0, 0].plot(pandas2, color='blue', label='Red Pandas (Lower a)')
axs[0, 0].plot(leopards2, color='red', label='Leopards (Lower a)')
axs[0, 0].set_title('Population with Lower Predation Rate')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Population')
axs[0, 0].legend(loc='upper right')

# Subplot 2
axs[0, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas (Default)')
axs[0, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[0, 1].plot(pandas3, color='blue', label='Red Pandas (Higher r)')
axs[0, 1].plot(leopards3, color='red', label='Leopards (Higher r)')
axs[0, 1].set_title('Population with Higher Panda Growth Rate')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Population')
axs[0, 1].legend(loc='upper right')

# Subplot 3
axs[1, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Red Pandas (Default)')
axs[1, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[1, 0].plot(pandas4, color='blue', label='Red Pandas (Lower B)')
axs[1, 0].plot(leopards4, color='red', label='Leopards (Lower B)')
axs[1, 0].set_title('Population with Lower Leopard Efficiency Rate')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Population')
axs[1, 0].legend(loc='upper right')

# Subplot 4
axs[1, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Red Pandas (Default)')
axs[1, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[1, 1].plot(pandas5, color='blue', label='Pandas (Higher q)')
axs[1, 1].plot(leopards5, color='red', label='Leopards (Higher q)')
axs[1, 1].set_title('Population with Higher Leopard Death Rate')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('Population')
axs[1, 1].legend(loc='upper right')

# Show
plt.tight_layout()
plt.show()




dt2 = 0.1 # time step size
t_end2 = 250 # end time

# Approximate Lotka Volterra Extended with Runge Kutta
d1 = [0.2, 0.02, 0.004, 0.2, 200] # Normal Values
d2 = [0.2, 0.005, 0.004, 0.2, 200] # Lower Predation Rate aka Lower a
d2b = [0.2, 0.1, 0.004, 0.2, 200] # Higher Predation Rate aka Higher a
d3 = [0.1, 0.02, 0.004, 0.2, 200] # Lower Panda Growth Rate aka Higher r
d3b = [0.4, 0.02, 0.004, 0.2, 200] # Higher Panda Growth Rate aka Higher r
d4 = [0.2, 0.02, 0.004, 0.2, 120] # Lower Carrying Capacity aka Lower K
d4b = [0.2, 0.02, 0.004, 0.2, 800] # Higher Carrying Capacity aka High K
d5 = [0.2, 0.02, 0.0032, 0.2, 200] # Lower Predator Efficiency Rate aka Lower b
d5b = [0.2, 0.02, 0.012, 0.2, 200] # Higher Predator Efficiency Rate aka Higher b 
d6 = [0.2, 0.02, 0.004, 0.15, 200] # Lower Predator Death Rate aka Lower q
d6b = [0.2, 0.02, 0.004, 0.25, 200] # Higher Predator Death Rate aka Higher q


pandas1, leopards1 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d1[0], d1[1], d1[2], d1[3], d1[4], dt2, t_end2)
pandas2, leopards2 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d2[0], d2[1], d2[2], d2[3], d2[4], dt2, t_end2)
pandas2b, leopards2b = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d2b[0], d2b[1], d2b[2], d2b[3], d2b[4], dt2, t_end2)
pandas3, leopards3 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d3[0], d3[1], d3[2], d3[3], d3[4], dt2, t_end2)
pandas3b, leopards3b = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d3b[0], d3b[1], d3b[2], d3b[3], d3b[4], dt2, t_end2)
pandas4, leopards4 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d4[0], d4[1], d4[2], d4[3], d4[4], dt2, t_end2)
pandas4b, leopards4b = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d4b[0], d4b[1], d4b[2], d4b[3], d4b[4], dt2, t_end2)
pandas5, leopards5 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d5[0], d5[1], d5[2], d5[3], d5[4], dt2, t_end2)
pandas5b, leopards5b = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d5b[0], d5b[1], d5b[2], d5b[3], d5b[4], dt2, t_end2)
pandas6, leopards6 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d6[0], d6[1], d6[2], d6[3], d6[4], dt2, t_end2)
pandas6b, leopards6b = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d6b[0], d6b[1], d6b[2], d6b[3], d6b[4], dt2, t_end2)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Subplot 1
axs[0, 0].plot(pandas1, color='grey', linestyle=':', label='Red Pandas (Default)')
axs[0, 0].plot(leopards1, color='black', linestyle=':', label='Leopards (Default)')
axs[0, 0].plot(pandas2, color='blue', label='Red Pandas (Lower a)')
axs[0, 0].plot(leopards2, color='red', label='Leopards2 (Lower a)')
axs[0, 0].plot(pandas2b, color='darkblue', linestyle='--', label='Red Pandas (Higher a)')
axs[0, 0].plot(leopards2b, color='darkred', linestyle='--', label='Leopards (Higher a)')
axs[0, 0].plot(pandas4, color='aqua', label='Red Pandas (Lower K)')
axs[0, 0].plot(leopards4, color='firebrick', label='Leopards (Lower K)')
axs[0, 0].plot(pandas4b, color='mediumseagreen', linestyle='--', label='Red Pandas (Higher K)')
axs[0, 0].plot(leopards4b, color='chocolate', linestyle='--', label='Leopards (Higher K)')
axs[0, 0].set_title('Population with Varying Predation and Capacity')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Population')
axs[0, 0].legend(loc='upper right')

# Subplot 2
axs[0, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Red Pandas (Default)')
axs[0, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[0, 1].plot(pandas3, color='blue', label='Red Pandas (Lower r)')
axs[0, 1].plot(leopards3, color='red', label='Leopards (Lower r)')
axs[0, 1].plot(pandas3b, color='darkblue', linestyle='--', label='Red Pandas (Higher r)')
axs[0, 1].plot(leopards3b, color='darkred', linestyle='--', label='Leopards (Higher r)')
axs[0, 1].set_title('Population with Varying Red Panda Growth Rate')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Population')
axs[0, 1].legend(loc='upper right')

# Subplot 3
axs[1, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Red Pandas (Default)')
axs[1, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[1, 0].plot(pandas5, color='blue', label='Red Pandas (Lower b)')
axs[1, 0].plot(leopards5, color='red', label='Leopards (Lower b)')
axs[1, 0].plot(pandas5b, color='darkblue', linestyle='--', label='Red Pandas (Higher b)')
axs[1, 0].plot(leopards5b, color='darkred', linestyle='--', label='Leopards (Higher b)')
axs[1, 0].set_title('Population with Varying Predator Efficiency')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Population')
axs[1, 0].legend(loc='upper right')

# Subplot 4
axs[1, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Red Pandas (Default)')
axs[1, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards (Default)')
axs[1, 1].plot(pandas6, color='blue', label='Red Pandas (Lower q)')
axs[1, 1].plot(leopards6, color='red', label='Leopards (Lower q)')
axs[1, 1].plot(pandas6b, color='darkblue', linestyle='--', label='Red Pandas (Higher q)')
axs[1, 1].plot(leopards6b, color='darkred', linestyle='--', label='Leopards (Higher q)')
axs[1, 1].set_title('Population with Varying Red Panda Carrying Capacity')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('Population')
axs[1, 1].legend(loc='upper right')

# Show
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

# P'al Runge
tF = 150
hS = 0.1

#Trayectoria con runge kutta
Na_values_1, Pa_values_1 = rungeKuttaPredatorPrey(PredatorPreyLotVol, 5, 1, ra, alphaa, betaa, qa, hS, tF)
Na_values_2, Pa_values_2 = rungeKuttaPredatorPrey(PredatorPreyLotVol, 1.5, 1.5, ra, alphaa, betaa, qa, hS, tF)
Na_values_3, Pa_values_3 = rungeKuttaPredatorPrey(PredatorPreyLotVol, 8, 0.6, ra, alphaa, betaa, qa, hS, tF)

#Graficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))  # Crear una figura con 2 gráficos uno al lado del otro

# Primer gráfico en ax1
ax1.plot(Na, isocline_Na, label='Isoclina de Pandas Rojos', color='indigo', linewidth=2, linestyle='--')
ax1.plot(isocline_Pa, Pa, label='Isoclina de Leopardos', color='limegreen', linewidth=2, linestyle='--')
ax1.set_xlabel('Pandas Rojos')
ax1.set_ylabel('Leopardos')
ax1.plot(Na_values_1, Pa_values_1, color='deeppink', label='Trayectoria 1')
ax1.plot(Na_values_2, Pa_values_2, color='hotpink', label='Trayectoria 2')
ax1.plot(Na_values_3, Pa_values_3, color='mediumvioletred', label='Trayectoria 3')
ax1.set_title('Isoclinas de Depredador y Presa')
ax1.scatter(eq1, eq1b, color='red', label='Punto de Equilibrio', s=100, zorder=10)
ax1.streamplot(vN, vP, dN, dP, color='gray', density=1, arrowstyle='->', linewidth=0.7)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.legend()

# Segundo gráfico en ax2
ax2.plot(Na_values_1, label='P- Trayectoria 1', color='orangered')
ax2.plot(Na_values_3, label='P - Trayectoria 3', color='gold', linestyle='--')
ax2.plot(Pa_values_1, label='L - Trayectoria 1', color='coral')
ax2.plot(Pa_values_3, label='L - Trayectoria 3', color='khaki', linestyle='--')
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Poblacion')
ax2.set_title('Trayectorias de Depredador-Presa')
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

# P'al Runge
tFinal = 150
hStep = 0.1

#Trayectoria con runge kutta
Nb_values_1, Pb_values_1 = rungeKuttaLotVolExt(LotkaVolterraExtODE, 5, 5, rb, alphab, betab, qb, k, hStep, tFinal)
Nb_values_2, Pb_values_2 = rungeKuttaLotVolExt(LotkaVolterraExtODE, 3, 9, rb, alphab, betab, qb, k, hStep, tFinal)
Nb_values_3, Pb_values_3 = rungeKuttaLotVolExt(LotkaVolterraExtODE, 2, 0.5, rb, alphab, betab, qb, k, hStep, tFinal)

#Graficar las isoclinas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Primer gráfico (Isoclinas)
ax1.plot(isocline_Nlve, Nb, label='Isoclina de Pandas Rojos', color = 'indigo', linestyle='--', linewidth=2)
ax1.plot(Nb, isocline_Plve, label='Isoclina de Leopardos', color = 'limegreen', linestyle='--', linewidth=2)
ax1.set_xlabel('Pandas Rojos')
ax1.set_ylabel('Leopardos')
ax1.set_title('Isoclinas de Lotka-Volterra Extendido')
ax1.plot(Nb_values_1, Pb_values_1, color = 'violet', label='Trajectoria 1')
ax1.plot(Nb_values_2, Pb_values_2, color = 'purple', label='Trajectoria 2')
ax1.plot(Nb_values_3, Pb_values_3, color = 'darkviolet', label='Trajectoria 3')
ax1.scatter(eq2xAxis, eq2yAxis, color='red', label='Punto de Equilibrio', s=100, zorder=10)
ax1.streamplot(vN, vP, dN, dP, color = 'gray', density=1, arrowstyle='->', linewidth=0.7)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.legend(loc='upper right')

# Segundo gráfico (Trayectorias)
ax2.plot(Nb_values_1, label='P - Trayectoria 1', color = 'violet')
ax2.plot(Pb_values_1, label='L - Trayectoria 1', color = 'darkviolet')
# TODO agregar otra trayectoria
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Poblacion')
ax2.set_title('Trayectorias de Lotka-Volterra Extendido')
ax2.legend()

# Show
plt.tight_layout()
plt.show()


