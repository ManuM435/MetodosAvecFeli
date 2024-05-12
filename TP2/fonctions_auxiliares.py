#Funciones auxiliares utilizadas en el TP2
import numpy as np
import matplotlib.pyplot as plt

def euler_method(func, initial_condition, t0, tf, num_steps, *args):
    h = (tf - t0) / num_steps  # Step size
    t_values = [t0]
    y_values = [initial_condition]

    t = t0
    y = initial_condition

    for _ in range(num_steps):
        y += h * func(t, y, *args)
        t += h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


def runge_kutta_4(func, initial_condition, t0, tf, num_steps, *args):
    h = (tf - t0) / num_steps
    t_values = [t0]
    y_values = [initial_condition]

    t = t0
    y = initial_condition

    for _ in range(num_steps):
        k1 = h * func(t, y, *args)
        k2 = h * func(t + 0.5 * h, y + 0.5 * k1, *args)
        k3 = h * func(t + 0.5 * h, y + 0.5 * k2, *args)
        k4 = h * func(t + h, y + k3, *args)

        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t += h

        t_values.append(t)
        y_values.append(y)

    return [t_values, y_values]


def rungeKutta4TwoSpecies(ode, N1, N2, r1, r2, K1, K2, alpha12, alpha21, dt, t_end):
    t = 0
    N1_values = [N1]
    N2_values = [N2]
    while t < t_end:
        k1 = ode(N1, N2, r1, r2, K1, K2, alpha12, alpha21)
        k2 = ode(N1 + 0.5 * dt * k1[0], N2 + 0.5 * dt * k1[1], r1, r2, K1, K2, alpha12, alpha21)
        k3 = ode(N1 + 0.5 * dt * k2[0], N2 + 0.5 * dt * k2[1], r1, r2, K1, K2, alpha12, alpha21)
        k4 = ode(N1 + dt * k3[0], N2 + dt * k3[1], r1, r2, K1, K2, alpha12, alpha21)
        
        N1 += (dt / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        N2 += (dt / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        
        N1_values.append(N1)
        N2_values.append(N2)
        t += dt
    
    return N1_values, N2_values