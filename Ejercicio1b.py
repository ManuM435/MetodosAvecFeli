import numpy as np
import matplotlib.pyplot as plt
import math
import funcionesTP1
import scipy.interpolate as spi

def funcion1b(x, y):
    return 0.75 * np.exp(-((10 * x - 2) ** 2) / 4 - ((9 * y - 2) ** 2) / 4) + \
           0.65 * np.exp(-((9 * x + 1) ** 2) / 9 - ((10 * y + 1) ** 2) / 2) + \
           0.55 * np.exp(-((9 * x - 6) ** 2) / 4 - ((9 * y - 3) ** 2) / 4) - \
           0.01 * np.exp(-((9 * x - 7) ** 2) / 4 - ((9 * y - 3) ** 2) / 4)

#Ejercicio 1 punto b
#PUNTOS EQUIESPACIADOS
#Splines

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

#Paso 3: Graficamos la función original y la interpolada
x1_plot = np.linspace(-1, 1, 50)
x2_plot = np.linspace(-1, 1, 50)
x1_plot, x2_plot = np.meshgrid(x1_plot, x2_plot)
y_original = funcion1b(x1_plot, x2_plot)
y_interpolada = spi.griddata(points, values, (x1_plot, x2_plot), method='cubic') #splines

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1_plot, x2_plot, y_interpolada, cmap = plt.cm.plasma, alpha=0.9)
ax.plot_wireframe(x1_plot, x2_plot, y_original, color="black", alpha=0.4)
plt.title('Interpolación de la función 1b usando Splines Cubicos')
plt.show()

