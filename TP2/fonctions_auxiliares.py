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
