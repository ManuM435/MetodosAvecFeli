#Ejercicio 1a
#Interpolación lagrange
import FuncionesEj1 as funcionesTP1
import numpy as np
import matplotlib.pyplot as plt
import math

def funcion1a(x):
    return (0.3**(abs(x)) * math.sin(4*x)) - math.tanh(2*x) + 2

#Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_1a = np.linspace(-4,4,9)
print(equi_points_1a)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a = funcionesTP1.eval_points_lister(equi_points_1a, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1a(x):
    return funcionesTP1.lagrange_interpolation(x, equi_points_1a, eval_points_1a)

# Paso 4: Graficamos la función original y la interpolada
x = np.linspace(-4, 4, 1000)  # Más puntos para una mejor visualización
y_original = [funcion1a(xi) for xi in x]
y_interpolada = [funcionInterpol1a(xi) for xi in x]

plt.plot(x, y_original, label='Función original')
plt.plot(x, y_interpolada, label='Función interpolada')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Lagrange')
plt.show()