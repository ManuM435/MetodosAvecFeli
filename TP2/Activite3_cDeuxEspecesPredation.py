#Ejercicio 3
import fonctions_auxiliares as aux
import numpy as np
import matplotlib.pyplot as plt

def ODE(n, p, r, a, b, q):
    dNdt = r * n - a * n * p
    dPdt = b * n * p - q * p
    return [dNdt, dPdt]

def LVE(n, p, r, a, b, q, k):
    dNdT = r * n * (1 - n / k) - a * n * p
    dPdt = b * n * p - q * p
    return [dNdT, dPdt]

def rkSolver(ode, a, b, q, r, n0, p0, dt, t_end):
    return aux.rungeKutta4TwoSpecies(ode, n0, p0, r, a, b, q, dt, t_end)

def equilibrium


