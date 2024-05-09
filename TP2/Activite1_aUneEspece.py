import numpy as np
import matplotlib.pyplot as plt
import fonctions_auxiliares as aux
r = 0.1

def variationExpoODE(t, N, r):
    '''Calcule la dérivée de la fonction exponentielle en un point N, avec un taux de croissance r'''
    return r * N

def populationExpoFonction(t, N0, r):
    '''Calcule la population en fonction du temps t, avec un taux de croissance r et une population initiale N0'''
    return N0 * np.exp(r * t)

def logistiqueODE(t, N, r, K):
    '''Calcule la dérivée de la fonction logistique en un point N, avec un taux de croissance r et une capacité de charge K'''
    return r * N * (1 - N / K)

def logistiquePopulation(t, N0, r, K):
    '''Calcule la population en fonction du temps t, avec un taux de croissance r, une capacité de charge K et une population initiale N0'''
    return K * N0 / (N0 + (K - N0) * np.exp(-r * t))

# Set some default values
t = np.linspace(0, 75, 100)
r = 0.1
k = 10000
N0 = 25
N1 = 6 # for the exponential

# Les curves (exponentielle)
popuExpo0 = populationExpoFonction(t, 0, r)
popuExpo1 = populationExpoFonction(t, N1, r) # TODO Appendix 1 Cambiar el 6 por "N1" para simular el que tienen todos el mismo comienzo 
popuExpo2 = populationExpoFonction(t, 10, (-1 * r))
popuExpo3 = populationExpoFonction(t, 10, 0)

# Les curves (logistique)
popuLogi0 = logistiquePopulation(t, 0, r, k)
popuLogi1 = logistiquePopulation(t, N0, r, 2000)
popuLogi2 = logistiquePopulation(t, N0, r, k)
popuLogi3 = logistiquePopulation(t, N0, (-1 * r), k)
popuLogi4 = logistiquePopulation(t, N0, 0, k)

# Les plots 

# Plot 1 || Expo vs Logis, Population over Time
plt.plot(t, popuExpo0, label='Exp0Starter')
plt.plot(t, popuLogi0, label='Logis0Starter')
plt.plot(t, popuExpo1, label='ExpNormal')
plt.plot(t, popuLogi1, label='LogisLowCap')
plt.plot(t, popuLogi2, label='LogisNormal')
plt.plot(t, popuExpo2, label='ExpNegGrowth')
plt.plot(t, popuLogi3, label='LogisNegGrowth')
plt.plot(t, popuExpo3, label='ExpNoGrowth')
plt.plot(t, popuLogi4, label='LogisNoGrowth')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Over Time')
plt.legend()
plt.show()

# Plot 2 || Population Variation Over Population
plt.plot(popuExpo1, variationExpoODE(t, popuExpo1, r), label='ExpNormal')
plt.plot(popuLogi1, logistiqueODE(t, popuLogi1, r, 1500), label='LogisLowCap')
plt.plot(popuLogi2, logistiqueODE(t, popuLogi2, r, k), label='LogisNormal')
plt.plot(popuExpo2, variationExpoODE(t, popuExpo2, (-1 * r)), label='ExpNegGrowth')
plt.plot(popuLogi3, logistiqueODE(t, popuLogi3, (-1 * r), k), label='LogisNegGrowth')
# TODO: Descomentar estos para el grafico de esos casos triviales, Appendix 2
# plt.plot(popuExpo0, variationExpoODE(r, popuExpo0), label='Exp0Starter')
# plt.plot(popuLogi0, logistiqueODE(r, popuLogi0, k), label='Logis0Starter')
# plt.plot(popuExpo3, variationExpoODE(0, popuExpo3), label='ExpNoGrowth')
# plt.plot(popuLogi4, logistiqueODE(0, popuLogi4, k), label='LogisNoGrowth')
plt.xlabel('Population')
plt.ylabel('Variation')
plt.title('Population Variation Over Population')
plt.legend()
plt.show()













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

# Example usage
initial_population = 10  # Initial population
growth_rate = 0.1  # Growth rate
t0 = 0  # Initial time
tf = 50  # Final time
num_steps = 100  # Number of steps for Euler method

# Compare exact solution with Euler method approximation
t_exact = np.linspace(t0, tf, 100)  # Time points for exact solution
N_exact = populationExpoFonction(t_exact, initial_population, growth_rate)


# Perform Euler integration
t_values, N_values = euler_method(variationExpoODE, initial_population, t0, tf, num_steps, growth_rate)

# Plot the results
import matplotlib.pyplot as plt

# Plot both exact solution and Euler method approximation
plt.plot(t_values, N_values, label='Euler Method Approximation')
plt.plot(t_exact, N_exact, label='Exact Solution', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Growth: Euler Method vs Exact Solution')
plt.legend()
plt.grid(True)
plt.show()

# Plot 3 || Population Time (Exponential, Euler Approximation, Runge-Kutta Approximation)



# Plot 4 || Population Over Time (Exponential, Euler Approximation, Runge-Kutta Approximation)



