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

# Les curves (exponentielle)
popuExpo0 = populationExpoFonction(0.1, 100, 4000)
popuExpo1 = populationExpoFonction(0.1, 100, 4000)
popuExpo2 = populationExpoFonction(0.1, 100, 4000)
popuExpo3 = populationExpoFonction(0.1, 100, 4000)
popuExpo4 = populationExpoFonction(0.1, 100, 4000)
popuExpo5 = populationExpoFonction(0.1, 100, 4000)
popuExpo6 = populationExpoFonction(0.1, 100, 4000)
popuExpo7 = populationExpoFonction(0.1, 100, 4000)

# Les curves (logistique)
popuLogi0 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi1 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi2 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi3 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi4 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi5 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi6 = logistiquePopulation(0.1, 100, 4000, t)
popuLogi7 = logistiquePopulation(0.1, 100, 4000, t)

# Les plots 
# Plot 1 || 
plt.plot(t, popuExpo0, label='Exp.')
plt.plot(t, popuLogi0, label='Logis')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Over Time')
plt.legend()
plt.show()

# Plot 2 || 