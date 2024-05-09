#Funciones auxiliares utilizadas en el TP2
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def euler_method(ode_func, r, r_values, initial_N, step_size):
    N_values = [initial_N]
    for _ in range(len(r_values) - 1):  # Iterate over the length of r_values - 1
        N_next = N_values[-1] + step_size * ode_func(r, N_values[-1])
        N_values.append(N_next)
    return N_values

def rk_4_A1(ode_func, r, N_values, step_size):
    new_N_values = [N_values[-1]]
    for _ in range(len(N_values) - 1):  # Iterate over the length of N_values - 1
        k1 = ode_func(r, new_N_values[-1])
        k2 = ode_func(r, new_N_values[-1] + step_size / 2 * k1)
        k3 = ode_func(r, new_N_values[-1] + step_size / 2 * k2)
        k4 = ode_func(r, new_N_values[-1] + step_size * k3)
        N_next = new_N_values[-1] + step_size / 6 * (k1 + 2*k2 + 2*k3 + k4)
        new_N_values.append(N_next)
    return new_N_values

