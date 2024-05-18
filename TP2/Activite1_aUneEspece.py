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
t = np.linspace(0, 50, 100)
r = 0.1
r2 = 0.01
k = 10000
N0 = 20
N1 = 4 # for the exponential

# Les curves (exponentielle)
popuExpo0 = populationExpoFonction(t, 0, r)
popuExpo1 = populationExpoFonction(t, N0, r) # TODO Appendix 1 Cambiar el 6 por "N1" para simular el que tienen todos el mismo comienzo 
popuExpo2 = populationExpoFonction(t, N1, (-1 * r))
popuExpo3 = populationExpoFonction(t, N1, 0)
popuExpo4 = populationExpoFonction(t, N1, r) # 4Starter

# Les curves (logistique)
popuLogi0 = logistiquePopulation(t, 0, r, k)
popuLogi1 = logistiquePopulation(t, N0, r, 1000)
popuLogi2 = logistiquePopulation(t, N0, r, k)
popuLogi3 = logistiquePopulation(t, N1, (-1 * r), k)
popuLogi4 = logistiquePopulation(t, N1, 0, k)
popuLogi5 = logistiquePopulation(t, N1, r, k) # 4Starter

expoLowGrowth = populationExpoFonction(t, N0, r2)
logiLowGrowth = logistiquePopulation(t, N0, r2, k)



# Les plots 

# Plot 1 || Expo vs Logis, Population over Time
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

# Subplot 1
axs[0].plot(t, popuExpo0, label='ExpZeroInitial')
axs[0].plot(t, popuLogi0, label='LogisZeroInitial')
axs[0].plot(t, popuExpo4, label='ExpLowInitial')
axs[0].plot(t, popuLogi5, label='LogisLowInitial')
axs[0].plot(t, popuExpo1, label='ExpHighInitial')
axs[0].plot(t, popuLogi2, label='LogisHighInitial')
axs[0].plot(t, popuLogi1, label='LogisHighInitialLowCap')

axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('Población')
axs[0].set_title('Pandas over time (Normal Growth)')
axs[0].legend()

# Subplot 2
axs[1].plot(t, popuExpo2, color='lavender',label='ExpNegGrowth', alpha=0.7)
axs[1].plot(t, popuLogi3, color='crimson',label='LogisNegGrowth', alpha=0.7)
axs[1].plot(t, popuExpo3, color='cadetblue',label='ExpNoGrowth', alpha=0.7)
axs[1].plot(t, popuLogi4, color='lime',label='LogisNoGrowth', alpha=0.7)
axs[1].plot(t, expoLowGrowth, linestyle=':', color='yellow', label='ExpLowGrowth')
axs[1].plot(t, logiLowGrowth, linestyle=':', color='black', label='LogisLowGrowth')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Población')
axs[1].set_title('Pandas over time (Varying Growth)')
axs[1].legend()

# Show
plt.tight_layout()
plt.show()




expoInitialPopOf1 = populationExpoFonction(t, 1, r)
logiInitialPopOf1 = logistiquePopulation(t, 1, r, k)

# Plot When Initial Pop is 1
plt.plot(t, expoInitialPopOf1, label='ExpInitialPop1')
plt.plot(t, logiInitialPopOf1, label='LogisInitialPop1')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Pandas over time (Initial Population of 1)')
plt.legend()
plt.show()




# Plot 2 || Population Variation Over Population
plt.plot(popuExpo1, variationExpoODE(t, popuExpo1, r), label='ExpNormal')
plt.plot(popuLogi2, logistiqueODE(t, popuLogi2, r, k), label='LogisNormal')
plt.plot(popuLogi1, logistiqueODE(t, popuLogi1, r, 1500), label='LogisHighGrowthLowCap')
plt.plot(expoLowGrowth, variationExpoODE(t, expoLowGrowth, r2), label='ExpLowGrowth')
plt.plot(logiLowGrowth, logistiqueODE(t, logiLowGrowth, r2, k), label='LogisLowGrowth')

# # TODO: Descomentar estos para el grafico de esos casos triviales, Appendix 2
# # plt.plot(popuExpo0, variationExpoODE(r, popuExpo0), label='Exp0Starter')
# # plt.plot(popuLogi0, logistiqueODE(r, popuLogi0, k), label='Logis0Starter')
# # plt.plot(popuExpo3, variationExpoODE(0, popuExpo3), label='ExpNoGrowth')
# # plt.plot(popuLogi4, logistiqueODE(0, popuLogi4, k), label='LogisNoGrowth')

plt.xlabel('Población')
plt.ylabel('Variacion')
plt.title('Variacion de Población en base a Población')
plt.legend()
plt.show()













# Valores Ejemplo para Aproximar
initial_population = 10  
growth_rate = 0.18  
t0 = 0  
tf = 50  
num_steps = 100
limit = 1000

# Exactas de Exponencial con los punticos
t_exact = np.linspace(t0, tf, num_steps) 
N_exact = populationExpoFonction(t_exact, initial_population, growth_rate)

# Aproximacion de Exponencial con Euler & RK
t_values_eu, N_values_eu = aux.euler_method(variationExpoODE, initial_population, t0, tf, num_steps, growth_rate)
t_values_rk4, N_values_rk4 = aux.runge_kutta_4(variationExpoODE, initial_population, t0, tf, num_steps, growth_rate)

# Exactas de Logistica con los punticos
t_logis_exact = np.linspace(t0, tf, num_steps)
N_logis_exact = logistiquePopulation(t_logis_exact, initial_population, growth_rate, limit)

# Aproximacion de Logistica con Euler & RK
t_logis_eu, N_logis_eu = aux.euler_method(logistiqueODE, initial_population, t0, tf, num_steps, growth_rate, limit)
t_logis_rk4, N_logis_rk4 = aux.runge_kutta_4(logistiqueODE, initial_population, t0, tf, num_steps, growth_rate, limit)



# Plot both exact solution and Euler method approximation for Exponential
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

# Subplot 1
axs[0].plot(t_values_eu, N_values_eu, label='Aproximacion Euler')
axs[0].plot(t_values_rk4, N_values_rk4, label='Aproximacion RK4')
axs[0].plot(t_exact, N_exact, label='Ground Truth', linestyle='--')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('Población')
axs[0].set_title('Pandas over time (Exponencial, Euler vs RK)')
axs[0].legend()
axs[0].grid(True)

# Subplot 2
axs[1].plot(t_logis_eu, N_logis_eu, label='Aproximacion Euler')
axs[1].plot(t_logis_rk4, N_logis_rk4, label='Aproximacion RK4')
axs[1].plot(t_logis_exact, N_logis_exact, label='Ground Truth', linestyle='--')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Población')
axs[1].set_title('Pandas over time (Logistica, Euler vs RK)')
axs[1].legend()
axs[1].grid(True)

# Show
plt.tight_layout()
plt.show()



# Calculate the average relative error for Euler approximation
euler_expo_error = np.abs(N_exact - N_values_eu[:-1]) / N_exact
euler_expo_avg_error = np.mean(euler_expo_error)

rk4_expo_error = np.abs(N_exact - N_values_rk4[:-1]) / N_exact
rk4_expo_avg_error = np.mean(rk4_expo_error)

print("Average Relative Error Euler (Exponential):", euler_expo_avg_error)
print("Average Relative Error Runge-Kutta (Exponential):", rk4_expo_avg_error)

# Calculate the average relative error for Euler approximation
euler_logis_error = np.abs(N_logis_exact - N_logis_eu[:-1]) / N_logis_exact
euler_logis_avg_error = np.mean(euler_logis_error)

rk4_logis_error = np.abs(N_logis_exact - N_logis_rk4[:-1]) / N_logis_exact
rk4_logis_avg_error = np.mean(rk4_logis_error)

print("Average Relative Error Euler (Logistique):", euler_logis_avg_error)
print("Average Relative Error Runge-Kutta (Logistique):", rk4_logis_avg_error)

#TODO (Maybe) Graph both their errors as less or more num_steps are used

