import numpy as np
import matplotlib.pyplot as plt
import math
import funcionesTP1

# def funcion1b(x1,x2):
#     return 0.75*math.exp(-((10*x1 - 2)**2/(4)) - ((9*x2 - 2)**2/(4))) + 0.65*math.exp(-((9*x1 + 1)**2/(9)) - ((10*x2 + 1)**2/(2))) + 0.55*math.exp(-((9*x1 - 6)**2/(4)) - ((9*x2 - 3)**2/(4))) - 0.01*math.exp(((9*x1 - 7)**2/(4)) - ((9*x2 - 3)**2/(4)))

def funcion1b(x1, x2):
    return 0.75*np.exp(-(((10*x1 - 2)**2)/(4)) - (((9*x2 - 2)**2)/(4))) + \
           0.65*np.exp(-(((9*x1 + 1)**2)/(9)) - (((10*x2 + 1)**2)/(2))) + \
           0.55*np.exp(-(((9*x1 - 6)**2)/(4)) - (((9*x2 - 3)**2)/(4))) - \
           0.01*np.exp((((9*x1 - 7)**2)/(4)) - (((9*x2 - 3)**2)/(4)))

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
# print(values)

#Paso 3: Creamos una función matemática en base a nuestro ground truth para interpolar con las reglas de Lagrange
def funcionInterpol1bLagrange(x1, x2):
    return funcionesTP1.interpolador_lagrange_R2(x1, x2, points, values)

#Paso 4: Graficamos la función original y la interpolada
x1_plot = np.linspace(-1, 1, 10)
x2_plot = np.linspace(-1, 1, 10)
x1_plot, x2_plot = np.meshgrid(x1_plot, x2_plot)
y_original = np.array([[funcion1b(xi, yi) for xi, yi in zip(x1_row, x2_row)] for x1_row, x2_row in zip(x1_plot, x2_plot)])
y_interpolada = np.array([[funcionInterpol1bLagrange(xi, yi) for xi, yi in zip(x1_row, x2_row)] for x1_row, x2_row in zip(x1_plot, x2_plot)])


#graficar en 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1_plot, x2_plot, y_original, alpha=0.5)
ax.plot_surface(x1_plot, x2_plot, y_interpolada, alpha=0.5)
plt.show()

