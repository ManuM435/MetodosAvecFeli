import numpy as np
import matplotlib.pyplot as plt
import csv
import funcionesTP1
import scipy.interpolate as spi
from scipy.interpolate import interp1d
from scipy.optimize import newton
from scipy.optimize import fsolve

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

#Paso 2.2: Crear las funciones que representan el recorrido de los vehículos
x_tractor = spi.CubicSpline(t_mediciones, x_mediciones)
y_tractor = spi.CubicSpline(t_mediciones, y_mediciones)
x_vehiculo2 = spi.CubicSpline(t_mediciones_vehiculo2, x_mediciones_vehiculo2)
y_vehiculo2 = spi.CubicSpline(t_mediciones_vehiculo2, y_mediciones_vehiculo2)

#Paso 3: Encontrar el punto de intersección con el método de Newton-Rhapson
def interseccionVehiculos(tiempo1, tiempo2):
    return (x_tractor(tiempo1) - x_vehiculo2(tiempo2), y_tractor(tiempo1) - y_vehiculo2(tiempo2))
    # return (spi.CubicSpline(t, x_interpol)(tiempo1) - spi.CubicSpline(t, x_interpol_vehiculo2)(tiempo2), spi.CubicSpline(t, y_interpol)(tiempo1) - spi.CubicSpline(t, y_interpol_vehiculo2)(tiempo2))

def jac(t):
    t1=t[0]
    t2=t[1]
    return np.array([[x_tractor(t1, 1), -x_vehiculo2(t2, 1)], [y_tractor(t1, 1), -y_vehiculo2(t2, 1)]])

def newtonRhapsonInterseccionVehiculos(f, t1, t2, tol=1e-5, max_iter=1000):
    t = [t1, t2]
    for i in range(max_iter):
        f1, f2 = f(t[0], t[1])  # Unpack the tuple returned by f
        delta = np.linalg.solve(jac(t), np.array([-f1, -f2]))
        t[0] += delta[0]  # Update t1
        t[1] += delta[1]
        if np.linalg.norm(f(t[0], t[1])) < tol:
            return t
    return t

t_interseccion = newtonRhapsonInterseccionVehiculos(interseccionVehiculos, 8.0, 4)

# encontrame las coordenadas
x_interseccion = spi.CubicSpline(t, x_interpol)(t_interseccion[0])
y_interseccion = spi.CubicSpline(t, y_interpol)(t_interseccion[0])
print(f'Las coordenadas de la intersección son: ({x_interseccion}, {y_interseccion})')

#Paso 4: Graficar
plt.plot(x_interpol, y_interpol, label='Interpolación vehículo 1', color = "red")
plt.plot(x_ground_truth, y_ground_truth, label='Ground truth', color = "violet")
plt.plot(x_interpol_vehiculo2, y_interpol_vehiculo2, label='Interpolación vehículo 2', color = "blue")
plt.plot(x_interseccion, y_interseccion, 'ro', label='Intersección')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones')
plt.show()

#LAGRANGE
#Ahora interpolamos el recorido del tractor con lagrange
x_interpol_lagrange = spi.lagrange(t_mediciones, x_mediciones)
y_interpol_lagrange = spi.lagrange(t_mediciones, y_mediciones)

x_interpol_lagrange = x_interpol_lagrange(t)
y_interpol_lagrange = y_interpol_lagrange(t)

#Paso 2.1: Graficar
plt.plot(x_interpol_lagrange, y_interpol_lagrange, label='Interpolación Lagrange', color = "green")
plt.plot(x_ground_truth, y_ground_truth, label='Ground truth', color = "violet")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones')
plt.show()

#interpolo el vehiculo 2 con lagrange
x_interpol_vehiculo2_lagrange = spi.lagrange(t_mediciones_vehiculo2, x_mediciones_vehiculo2)
y_interpol_vehiculo2_lagrange = spi.lagrange(t_mediciones_vehiculo2, y_mediciones_vehiculo2)

x_interpol_vehiculo2_lagrange = x_interpol_vehiculo2_lagrange(t)
y_interpol_vehiculo2_lagrange = y_interpol_vehiculo2_lagrange(t)

#Paso 2.1: Graficar intersección
plt.plot(x_interpol_lagrange, y_interpol_lagrange, label='Interpolación vehículo 1', color = "green")
plt.plot(x_ground_truth, y_ground_truth, label='Ground truth', color = "violet")
plt.plot(x_interpol_vehiculo2_lagrange, y_interpol_vehiculo2_lagrange, label='Interpolación vehículo 2', color = "blue")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones')
plt.show()
