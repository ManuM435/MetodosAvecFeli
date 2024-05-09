import numpy as np
import matplotlib.pyplot as plt
import fonctions_auxiliares as aux

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
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Población en el tiempo')
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
plt.xlabel('Población')
plt.ylabel('Variacion')
plt.title('Variacion de Población en base a Población')
plt.legend()
plt.show()



# Valores Ejemplo para Aproximar
initial_population = 10  
growth_rate = 0.1  
t0 = 0  
tf = 50  
num_steps = 100  

# Exactas con los punticos
t_exact = np.linspace(t0, tf, num_steps) 
N_exact = populationExpoFonction(t_exact, initial_population, growth_rate)

# Euler & RK
t_values, N_values = aux.euler_method(variationExpoODE, initial_population, t0, tf, num_steps, growth_rate)
t_values_rk4, N_values_rk4 = aux.runge_kutta_4(variationExpoODE, initial_population, t0, tf, num_steps, growth_rate)

# Plot both exact solution and Euler method approximation
plt.plot(t_values, N_values, label='Aproximacion Euler')
plt.plot(t_values_rk4, N_values_rk4, label='Aproximacion RK4')
plt.plot(t_exact, N_exact, label='Exact Solution', linestyle='--')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Crecimiento de Población Exponencial (G-Truth vs Euler vs RK4)')
plt.legend()
plt.grid(True)
plt.show()


# Plot 4 || Population Over Time (Exponential, Euler Approximation, Runge-Kutta Approximation)



