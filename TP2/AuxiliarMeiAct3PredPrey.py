# #Ejercicio 3
# import fonctions_auxiliares as aux
# import numpy as np
# import matplotlib.pyplot as plt

# def PredatorPreyLotVol(t, n, p, r, a, b, q):
#     dNdt = r * n - a * n * p
#     dPdt = b * n * p - q * p
#     return [dNdt, dPdt]

# def LotkaVolterraExtODE(t, n, p, r, a, b, q, k):
#     dNdT = r * n * (1 - n / k) - a * n * p
#     dPdt = b * n * p - q * p
#     return [dNdT, dPdt]

# # Probar con estas 2 funciones de RK, despues se pasan a las auxiliares, primero probarlas aca
# def rungeKuttaPredatorPrey(ode, n, p, r, a, b, q, dt, t_end):
#     t = 0
#     n_values = [n]
#     p_values = [p]
#     while t < t_end:
#         k1 = ode(t, n, p, r, a, b, q)
#         k2 = ode(t + 0.5 * dt, n + 0.5 * dt * k1[0], p + 0.5 * dt * k1[1], r, a, b, q)
#         k3 = ode(t + 0.5 * dt, n + 0.5 * dt * k2[0], p + 0.5 * dt * k2[1], r, a, b, q)
#         k4 = ode(t + dt, n + dt * k3[0], p + dt * k3[1], r, a, b, q)
        
#         n += (dt / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
#         p += (dt / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        
#         n_values.append(n)
#         p_values.append(p)
#         t += dt
#     return n_values, p_values

# def rungeKuttaLotVolExt(ode, n, p, r, a, b, q, k, dt, t_end):
#     t = 0
#     n_values = [n]
#     p_values = [p]
#     while t < t_end:
#         k1 = ode(t, n, p, r, a, b, q, k)
#         k2 = ode(t + 0.5 * dt, n + 0.5 * dt * k1[0], p + 0.5 * dt * k1[1], r, a, b, q, k)
#         k3 = ode(t + 0.5 * dt, n + 0.5 * dt * k2[0], p + 0.5 * dt * k2[1], r, a, b, q, k)
#         k4 = ode(t + dt, n + dt * k3[0], p + dt * k3[1], r, a, b, q, k)
        
#         n += (dt / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
#         p += (dt / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        
#         n_values.append(n)
#         p_values.append(p)
#         t += dt
#     return n_values, p_values


# # Runge Kutta Approximations
# Pandas0 = 120  # initial population of prey species
# Leopards0 = 30  # initial population of predator species
# dt = 0.25 # time step size
# t_end = 100 # end time

# # Approximate Predator-Prey with Runge Kutta
# d1 = [0.2, 0.02, 0.004, 0.2] # Normal Values
# d2 = [0.2, 0.005, 0.004, 0.2] # Lower Predation Rate aka Lower a
# d3 = [0.8, 0.02, 0.004, 0.2] # Higher Panda Growth Rate aka Higher r
# d4 = [0.2, 0.02, 0.024, 0.2] # Lower Predator Efficiency Rate aka Lower b
# d5 = [0.2, 0.02, 0.004, 0.6] # Higher Predator Death Rate aka Higher q

# pandas1, leopards1 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d1[0], d1[1], d1[2], d1[3], dt, t_end)
# pandas2, leopards2 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d2[0], d2[1], d2[2], d2[3], dt, t_end)
# pandas3, leopards3 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d3[0], d3[1], d3[2], d3[3], dt, t_end)
# pandas4, leopards4 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d4[0], d4[1], d4[2], d4[3], dt, t_end)
# pandas5, leopards5 = rungeKuttaPredatorPrey(PredatorPreyLotVol, Pandas0, Leopards0, d5[0], d5[1], d5[2], d5[3], dt, t_end)

# fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# # Subplot 1
# axs[0, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[0, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[0, 0].plot(pandas2, color='blue', label='Pandas (Lower a)')
# axs[0, 0].plot(leopards2, color='red', label='Leopards2 (Lower a)')
# axs[0, 0].set_title('Population dynamics with a Lower Predation Rate')
# axs[0, 0].legend(loc='upper right')

# # Subplot 2
# axs[0, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[0, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[0, 1].plot(pandas3, color='blue', label='Pandas (Higher r)')
# axs[0, 1].plot(leopards3, color='red', label='Leopards (Higher r)')
# axs[0, 1].set_title('Population dynamics with a Higher Panda Growth Rate')
# axs[0, 1].legend(loc='upper right')

# # Subplot 3
# axs[1, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[1, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[1, 0].plot(pandas4, color='blue', label='Pandas (Lower B)')
# axs[1, 0].plot(leopards4, color='red', label='Leopards (Lower B)')
# axs[1, 0].set_title('Population dynamics with a Lower Predator Efficiency Rate')
# axs[1, 0].legend(loc='upper right')

# # Subplot 4
# axs[1, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[1, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[1, 1].plot(pandas5, color='blue', label='Pandas (Higher q)')
# axs[1, 1].plot(leopards5, color='red', label='Leopards (Higher q)')
# axs[1, 1].set_title('Population dynamics with a Higher Predator Death Rate')
# axs[1, 1].legend(loc='upper right')

# plt.tight_layout()
# plt.show()

# # Approximate Lotka Volterra Extended with Runge Kutta
# d1 = [0.2, 0.02, 0.004, 0.2, 200] # Normal Values
# d2 = [0.2, 0.005, 0.004, 0.2, 200] # Lower Predation Rate aka Lower a
# d3 = [0.8, 0.02, 0.004, 0.2, 200] # Higher Panda Growth Rate aka Higher r
# d4 = [0.2, 0.02, 0.004, 0.2, 800] # Higher Carrying Capacity aka Higher K
# d5 = [0.2, 0.02, 0.004, 0.2, 120] # Lower Carrying Capacity aka Lower K

# pandas1, leopards1 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d1[0], d1[1], d1[2], d1[3], d1[4], dt, t_end)
# pandas2, leopards2 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d2[0], d2[1], d2[2], d2[3], d2[4], dt, t_end)
# pandas3, leopards3 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d3[0], d3[1], d3[2], d3[3], d3[4], dt, t_end)
# pandas4, leopards4 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d4[0], d4[1], d4[2], d4[3], d4[4], dt, t_end)
# pandas5, leopards5 = rungeKuttaLotVolExt(LotkaVolterraExtODE, Pandas0, Leopards0, d5[0], d5[1], d5[2], d5[3], d5[4], dt, t_end)

# fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# # Subplot 1
# axs[0, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[0, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[0, 0].plot(pandas2, color='blue', label='Pandas (Lower a)')
# axs[0, 0].plot(leopards2, color='red', label='Leopards2 (Lower a)')
# axs[0, 0].set_title('Population dynamics with a Lower Predation Rate')
# axs[0, 0].legend(loc='upper right')

# # Subplot 2
# axs[0, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[0, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[0, 1].plot(pandas3, color='blue', label='Pandas (Higher r)')
# axs[0, 1].plot(leopards3, color='red', label='Leopards (Higher r)')
# axs[0, 1].set_title('Population dynamics with a Higher Panda Growth Rate')
# axs[0, 1].legend(loc='upper right')

# # Subplot 3
# axs[1, 0].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[1, 0].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[1, 0].plot(pandas4, color='blue', label='Pandas (Higher K)')
# axs[1, 0].plot(leopards4, color='red', label='Leopards (Higher K)')
# axs[1, 0].set_title('Population dynamics with a Higher Panda Carrying Capacity')
# axs[1, 0].legend(loc='upper right')

# # Subplot 4
# axs[1, 1].plot(pandas1, color='grey', linestyle=':', alpha=0.7, label='Pandas "Normal"')
# axs[1, 1].plot(leopards1, color='black', linestyle=':', alpha=0.7, label='Leopards "Normal"')
# axs[1, 1].plot(pandas5, color='blue', label='Pandas (Lower K)')
# axs[1, 1].plot(leopards5, color='red', label='Leopards (Lower K)')
# axs[1, 1].set_title('Population dynamics with a Lower Panda Carrying Capacity')
# axs[1, 1].legend(loc='upper right')

# plt.tight_layout()
# plt.show()

