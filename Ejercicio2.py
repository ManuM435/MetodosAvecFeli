import numpy as np
import matplotlib.pyplot as plt
import csv
import funcionesTP1

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

#Paso 2: Crear una función que interpole los datos con lagrange
def funcionInterpolTractorLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, x_mediciones, y_mediciones)

#Paso 3: Crear una lista de puntos para graficar la función interpolada
x_plot = np.linspace(min(x_mediciones), max(x_mediciones), 100)
y_interpolada = [funcionInterpolTractorLagrange(xi) for xi in x_plot]

# #Paso 4: Graficar la función interpolada
plt.plot(x_plot, y_interpolada, label='Interpolación')
plt.scatter(x_mediciones, y_mediciones, label='Mediciones')
plt.legend()
plt.show()

#Paso 5: Cargar los datos del archivo de ground truth
data_list_ground_truth = []
with open('mnyo_ground_truth.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ')
    
    for row in csv_reader:
        row_float = [float(value) for value in row]
        data_list_ground_truth.append(row_float)

print(data_list_ground_truth)
