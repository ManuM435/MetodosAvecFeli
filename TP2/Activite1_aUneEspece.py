import numpy as np
import matplotlib.pyplot as plt

def variationExpoODE(r, N):
    '''Calcule la dérivée de la fonction exponentielle en un point N, avec un taux de croissance r'''
    return r * N

def populationExpoFonction(r, N0, t):
    '''Calcule la population en fonction du temps t, avec un taux de croissance r et une population initiale N0'''
    return N0 * np.exp(r * t)

def logistiqueODE(r, N, K):
    '''Calcule la dérivée de la fonction logistique en un point N, avec un taux de croissance r et une capacité de charge K'''
    return r * N * (1 - N / K)

def logistiquePopulation(r, N0, K, t):
    '''Calcule la population en fonction du temps t, avec un taux de croissance r, une capacité de charge K et une population initiale N0'''
    return K * N0 / (N0 + (K - N0) * np.exp(-r * t))

# El del Time
t = np.linspace(0, 40, 100)

r = 0.1
N0 = 100
K = 4000

# Les plots 
# TODO: No definir valores r, N0, k. En su lugar, ir tipeando las funciones en el plot con los valores que vamos poniendo
plt.plot(t, populationExpoFonction(r, N0, t), label='Exponential')
plt.plot(t, logistiquePopulation(r, N0, K, t), label='Logistic')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Over Time')
plt.legend()
plt.show()