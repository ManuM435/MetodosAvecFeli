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

# Approximate Predator-Prey with Runge Kutta

Pandas0 = 120  # initial population of prey species
Tigers0 = 30  # initial population of predator species
dt = 0.1 # time step size
t_end = 10 # end time

d1 = [0.2, 0.02, 0.004, 0.2] # Normal Values
d2 = [0.2, 0.005, 0.004, 0.2] # Lower Predation aka Lower a
d3 = [0.8, 0.02, 0.004, 0.2] # Highr Panda Growth Rate aka Lower r
d4 = [0.2, 0.02, 0.024, 0.2] # Higher Predator Efficiency Rate aka Lower b
d5 = [0.2, 0.02, 0.004, 0.6] # Higher Predator Death Rate aka Higher q

pandas1, tigers1 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Tigers0, d1[0], d1[1], d1[2], d1[3], dt, t_end)


plt.plot(pandas1, label='Pandas Normal')
plt.plot(tigers1, label='Predator Normal')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()