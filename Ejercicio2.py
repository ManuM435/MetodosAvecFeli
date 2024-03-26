import numpy as np
import matplotlib.pyplot as plt
import csv
import funcionesTP1
import scipy.interpolate as spi
from scipy.interpolate import interp1d


#Ejercicio 2
#Primer parte --> interpolar (aproximar) el recorrido del tractor con el archivo de mediciones, a esta función interpolada comparala con el camino real del tracto en ground truth

#Paso 1: Cargar los datos del archivo de mediciones
data_list_mediciones = []

with open('mnyo_mediciones.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ')
    
    for row in csv_reader:
        data_list_mediciones.append(row)

#Paso 1.2: Separar los datos en dos listas, una para x y otra para y
x_mediciones = [float(row[0]) for row in data_list_mediciones]
y_mediciones = [float(row[1]) for row in data_list_mediciones]

#Paso 1.3: Crear una lista que represente el tiempo con el mismo largo que las listas de x e y
t_mediciones = np.linspace(0, 100, len(x_mediciones))

#Paso 2: Graficar en el eje x lo que de xinterpo y en el eje y lo que de yinterpol
t = np.linspace(0, 100, 1000)
x_interpol = spi.CubicSpline(t_mediciones, x_mediciones)
y_interpol = spi.CubicSpline(t_mediciones, y_mediciones)

x_interpol = x_interpol(t)
y_interpol = y_interpol(t)

#Paso 2.1: Agregar el ground truth
data_list_ground_truth = []

with open('mnyo_ground_truth.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ')
    
    for row in csv_reader:
        data_list_ground_truth.append(row)

x_ground_truth = [float(row[0]) for row in data_list_ground_truth]
y_ground_truth = [float(row[1]) for row in data_list_ground_truth]

#Paso 2.2: Graficar
#TODO: descomentar
plt.plot(x_interpol, y_interpol, label='Interpolación', color = "red")
plt.plot(x_ground_truth, y_ground_truth, label='Ground truth', color = "violet")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones')
plt.show()

#Segunda parte --> buscar intersección con vehículo 2
#Paso 1: Cargar los datos del archivo de mediciones del vehículo 2
data_list_mediciones_vehiculo2 = []

with open('mnyo_mediciones2.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ')
    
    for row in csv_reader:
        data_list_mediciones_vehiculo2.append(row)

#Paso 1.2: Separar los datos en dos listas, una para x y otra para y
x_mediciones_vehiculo2 = [float(row[0]) for row in data_list_mediciones_vehiculo2]
y_mediciones_vehiculo2 = [float(row[1]) for row in data_list_mediciones_vehiculo2]

#Paso 1.3: Crear una lista que represente el tiempo con el mismo largo que las listas de x e y
t_mediciones_vehiculo2 = np.linspace(0, 100, len(x_mediciones_vehiculo2))

#Paso 2: Graficar en el eje x lo que de xinterpo y en el eje y lo que de yinterpol con el vehículo 1 y el ground truth
t = np.linspace(0, 100, 1000)
x_interpol_vehiculo2 = spi.CubicSpline(t_mediciones_vehiculo2, x_mediciones_vehiculo2)
y_interpol_vehiculo2 = spi.CubicSpline(t_mediciones_vehiculo2, y_mediciones_vehiculo2)

x_interpol_vehiculo2 = x_interpol_vehiculo2(t)
y_interpol_vehiculo2 = y_interpol_vehiculo2(t)

#Paso 2.1: Graficar
#TODO: descomentar
plt.plot(x_interpol, y_interpol, label='Interpolación vehículo 1', color = "red")
plt.plot(x_ground_truth, y_ground_truth, label='Ground truth', color = "violet")
plt.plot(x_interpol_vehiculo2, y_interpol_vehiculo2, label='Interpolación vehículo 2', color = "blue")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones')
plt.show()

#Paso 3: Encontrar el punto de intersección con el método de Newton-Rhapson
#Paso 3.1: Crear las funciones que representan a las rectas de los vehículos
def funcionVehiculo1(x):
    return spi.CubicSpline(t, x_interpol)(x) - spi.CubicSpline(t, y_interpol)(x)

def funcionVehiculo2(x):
    return spi.CubicSpline(t, x_interpol_vehiculo2)(x) - spi.CubicSpline(t, y_interpol_vehiculo2)(x)

#Paso 3.2: Crear la función que representa la intersección de las rectas
def interseccionVehiculos(x):
    return funcionVehiculo1(x) - funcionVehiculo2(x)

#Paso 3.3: Encontrar la derivada de la función de intersección
def derivadaInterseccionVehiculos(x):
    return spi.CubicSpline(t, x_interpol)(x) - spi.CubicSpline(t, x_interpol_vehiculo2)(x)

#Paso 3.4: Encontrar el punto de intersección
from scipy.optimize import newton
x_interseccion = newton(interseccionVehiculos, 0)
y_interseccion = spi.CubicSpline(t, x_interpol)(x_interseccion)

print(f'El punto de intersección es: ({x_interseccion}, {y_interseccion})')