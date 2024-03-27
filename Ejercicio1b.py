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
x1_plot = np.linspace(-1, 1, 100)
x2_plot = np.linspace(-1, 1, 100)
x1_plot, x2_plot = np.meshgrid(x1_plot, x2_plot)
y_original = funcion1b(x1_plot, x2_plot)
y_interpolada = spi.griddata(points, values, (x1_plot, x2_plot), method='cubic') #splines

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1_plot, x2_plot, y_interpolada, cmap = plt.cm.plasma, alpha=0.9)
ax.plot_wireframe(x1_plot, x2_plot, y_original, color="black", alpha=0.4)
plt.title('Interpolación de la función 1b usando Splines Cubicos')
plt.show()

#Paso 4: Calcular y graficar el error relativo promedio para cada cantidad de nodos utilizada
n_values = range(6, 71)  # range of node quantities to test
avg_relative_errors = []

for n in n_values:
    x1, x2 = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n))
    x1_flat = x1.reshape(-1)
    x2_flat = x2.reshape(-1)
    points = list(zip(x1_flat, x2_flat))
    values = funcionesTP1.eval_points_lister_R2(points, funcion1b)
    y_interpolada = spi.griddata(points, values, (x1_plot, x2_plot), method='cubic')  # splines
    relative_error = np.abs((y_original - y_interpolada) / y_original)
    avg_relative_error = np.nanmean(relative_error)  
    avg_relative_errors.append(avg_relative_error)

plt.figure()
plt.semilogy(n_values, avg_relative_errors, marker='o')
plt.title('Error promedio en funcion a cantidad de puntos usando Spline Cubico', pad=20) 
plt.xlabel('Cantidad de puntos')
plt.ylabel('Error relativo promedio')
plt.xticks(np.arange(min(n_values), max(n_values)+1, 3)) 
plt.grid(True, which='both', linestyle='--', linewidth=0.6) 

for i, (x, y) in enumerate(zip(n_values, avg_relative_errors)):
    if i % 4 == 0:  # Only label every 4th point
        y_int = int(y)
        if len(str(y_int)) > 5:
            label = "{:.2e}".format(y)  # Use scientific notation
        else:
            label = "{:.0f}".format(y)
        plt.annotate(label, 
                     (x, y),  
                     textcoords="offset points",
                     xytext=(0,10),  
                     ha='center')  
plt.show()