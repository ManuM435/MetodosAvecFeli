import numpy as np
import matplotlib.pyplot as plt
import fonctions_auxiliares as aux
r = 0.1

def variationExpoODE(r, N):
    '''Calcule la dérivée de la fonction exponentielle en un point N, avec un taux de croissance r'''
    return r * N

def populationExpoFonction(r, N0, t):
    '''Calcule la population en fonction du temps t, avec un taux de croissance r et une population initiale N0'''
    return N0 * np.exp(r * t)

def logistiqueODE(r, N, K):
    '''Calcule la dérivée de la fonction logistique en un point N, avec un taux de croissance r et une capacité de charge K'''
    return r * N * (1 - N / K)

def logistiquePopulation(r, N0, t, K):
    '''Calcule la population en fonction du temps t, avec un taux de croissance r, une capacité de charge K et une population initiale N0'''
    return K * N0 / (N0 + (K - N0) * np.exp(-r * t))

# Set some default values
t = np.linspace(0, 75, 100)
r = 0.1
k = 10000
N0 = 25
N1 = 6 # for the exponential

# Les curves (exponentielle)
popuExpo0 = populationExpoFonction(r, 0, t)
popuExpo1 = populationExpoFonction(r, N1, t) # TODO Appendix 1 Cambiar el 6 por "N1" para simular el que tienen todos el mismo comienzo 
popuExpo2 = populationExpoFonction((-1 * r), 10, t)
popuExpo3 = populationExpoFonction(0, 10, t)

# Les curves (logistique)
popuLogi0 = logistiquePopulation(r, 0, t, k)
popuLogi1 = logistiquePopulation(r, N0, t, 2000)
popuLogi2 = logistiquePopulation(r, N0, t, k)
popuLogi3 = logistiquePopulation((-1 * r), N0, t, k)
popuLogi4 = logistiquePopulation(0, N0, t, k)

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
plt.plot(popuExpo1, variationExpoODE(r, popuExpo1), label='ExpNormal')
plt.plot(popuLogi1, logistiqueODE(r, popuLogi1, 1500), label='LogisLowCap')
plt.plot(popuLogi2, logistiqueODE(r, popuLogi2, k), label='LogisNormal')
plt.plot(popuExpo2, variationExpoODE((-1 * r), popuExpo2), label='ExpNegGrowth')
plt.plot(popuLogi3, logistiqueODE((-1 * r), popuLogi3, k), label='LogisNegGrowth')
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

# Values for the Approximation
Nz = 10
rz = 0.1
Kz = 100
h = 0.1



# Plot 3 || Population Over Time (Exponential, Euler Approximation, Runge-Kutta Approximation)
plt.plot(t, popuExpoZ, label='Exponential')
plt.plot(t, euler_approx, label='Euler Approximation')
plt.plot(t, runge_kutta_approx, label='Runge-Kutta Approximation')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Over Time (Exponential, Euler Approximation, Runge-Kutta Approximation)')
plt.legend()
plt.show()




