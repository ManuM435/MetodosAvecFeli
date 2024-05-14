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


# PREDATOR PREY RUNGE KUTTA (1 graph, 10 curves, 5 data sets)

# Approximate Predator-Prey with Runge Kutta
Pandas0 = 120  # initial population of prey species
Leopards0 = 30  # initial population of predator species
dt = 0.1 # time step size
t_end = 10 # end time

d1 = [0.2, 0.02, 0.004, 0.2] # Normal Values
d2 = [0.2, 0.005, 0.004, 0.2] # Lower Predation aka Lower a
d3 = [0.8, 0.02, 0.004, 0.2] # Highr Panda Growth Rate aka Lower r
d4 = [0.2, 0.02, 0.024, 0.2] # Higher Predator Efficiency Rate aka Lower b
d5 = [0.2, 0.02, 0.004, 0.6] # Higher Predator Death Rate aka Higher q

pandas1, leopards1 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d1[0], d1[1], d1[2], d1[3], dt, t_end)


fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(pandas1, label='Pandas Normal')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Population')
axs[0, 0].legend()

axs[0, 1].plot(leopards1, label='Predator Normal')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Population')
axs[0, 1].legend()

# Add code for the other two subplots here

plt.tight_layout()
plt.show()

# LOTKA VOLTERRA EXTENDED RUNGE KUTTA (1 graph with 10 curves, 5 data sets)
# Jugar un poco con el k y K, pero un poco menos enfasis en jugar con la de predadores que ya jugaste en el grafico anterior





# GRAPHING BOTH DIFFERENTIAL EQUATIONS (no approximations, just the 2 differential equations)
# TODO PREGUNTAR SI ES DN/DT OVER T OR OVER N(T)

#Isoclinas Cero

#Parámetros part 1
Na = np.linspace(0, 100, 100)
Pa = np.linspace(0, 200, 100)
alphaa = 10
betaa = 10
ra = 0.1
qa = 0.1
alphaa = 0.1
betaa = 0.1

#Isoclinas predador-presa
# isocline_Na = qa/betaa
# isocline_Pa = ra/alphaa
isocline_Na = np.full_like(Na, qa/betaa)
isocline_Pa = np.full_like(Pa, ra/alphaa)

#Graficar las isoclinas
plt.plot(Na, isocline_Na, label='Isocline of N', color = 'indigo')
plt.plot(isocline_Pa, Pa, label='Isocline of P', color = 'limegreen')
plt.xlabel('N')
plt.ylabel('P')
plt.legend()
plt.show()

#Parametros part2 LVE
Nb = np.linspace(0, 10, 10)
Pb = np.linspace(0, 10, 10)
rb = 0.1
qb = 0.1
alphab = 0.1
betab = 0.1
k = 10

#Isoclinas LVE
isocline_Nlve = np.full_like(Nb, alphab/betab)
isocline_Plve = np.full_like(Pb, 1 - (alphab/(betab*k)) - alphab/rb)

#Graficar las isoclinas
plt.plot(Nb, isocline_Nlve, label='Isocline of N', color = 'indigo')
plt.plot(isocline_Plve, Pb, label='Isocline of P', color = 'limegreen')
plt.xlabel('N')
plt.ylabel('P')
plt.legend()
plt.show()
