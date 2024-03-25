import numpy as np
import matplotlib.pyplot as plt
import math
import funcionesTP1

def funcion1b(x1,x2):
    return 0.75*math.exp(-((10*x1 - 2)**2/(4)) - ((9*x2 - 2)**2/(4))) + 0.65*math.exp(-((9*x1 + 1)**2/(9)) - ((10*x2 + 1)**2/(2))) + 0.55*math.exp(-((9*x1 - 6)**2/(4)) - ((9*x2 - 3)**2/(4))) - 0.01*math.exp(((9*x1 - 7)**2/(4)) - ((9*x2 - 3)**2/(4)))

#Ejercicio 1 punto b
#PUNTOS EQUIESPACIADOS
#Lagrange

#Paso 1: Crear los puntos equiespaciados, (deberían ser tuplas ya que es una runcion en R2), una lista de tuplas, en donde cada punto debería estar entre -1 y 1
x1, x2 = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))

x1 = np.clip(x1, -1, 1)
x2 = np.clip(x2, -1, 1)

x1_flat = x1.reshape(-1)
x2_flat = x2.reshape(-1)

points = list(zip(x1_flat, x2_flat))
# print(points)

#Paso 2: Evaluar la función en los puntos
values = funcionesTP1.eval_points_lister_R2(points, funcion1b)
print(values)
