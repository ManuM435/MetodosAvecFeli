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

#Paso 1.3: Crear una lista que represente el tiempo con el mismo largo que las listas de x e y
t_mediciones = np.linspace(0, 100, len(x_mediciones))

#Paso 2: Crear una función matemática en base a las x mediciones (eje y) y t mediciones (eje x) interpolar usando lagrange
def funcionInterpol2LagrangeX(t):
    return funcionesTP1.lagrange_interpolation(t, t_mediciones, x_mediciones)

#Paso 3: Crear una función matemática en base a las y mediciones (eje y) y t mediciones (eje x) interpolar usando lagrange
def funcionInterpol2LagrangeY(t):
    return funcionesTP1.lagrange_interpolation(t, t_mediciones, y_mediciones)

#Paso 4: Graficar en el eje x lo que de funcionInterpol2LagrangeX(t) y en el eje y lo que de funcionInterpol2LagrangeY(t)
t = np.linspace(0, 100, 1000)
x_interpol = [funcionInterpol2LagrangeX(ti) for ti in t]
y_interpol = [funcionInterpol2LagrangeY(ti) for ti in t]

#Paso 4.1: Poner el groud truth en el mismo grafico
data_list_ground_truth = []
with open('mnyo_ground_truth.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ')
    
    for row in csv_reader:
        data_list_ground_truth.append(row)

x_ground_truth = [float(row[0]) for row in data_list_ground_truth]
y_ground_truth = [float(row[1]) for row in data_list_ground_truth]

plt.plot(x_interpol, y_interpol, label='Interpolación')
plt.plot(x_ground_truth, y_ground_truth, label='Ground Truth')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones de tractor')
plt.show()

#Paso 5: Calcular el error absoluto y relativo de la interpolación
error_absoluto_x = [abs(funcionInterpol2LagrangeX(ti) - xi) for ti, xi in zip(t, x_ground_truth)]
error_absoluto_y = [abs(funcionInterpol2LagrangeY(ti) - yi) for ti, yi in zip(t, y_ground_truth)]

error_relativo_x = [abs(funcionInterpol2LagrangeX(ti) - xi) / xi if xi != 0 else -1 for ti, xi in zip(t, x_ground_truth)]
error_relativo_y = [abs(funcionInterpol2LagrangeY(ti) - yi) / yi if yi != 0 else -1 for ti, yi in zip(t, y_ground_truth)]

#SEGUNDA PARTE --> interpolar el recorrido del otro vehículo y determinar si este pasó por algún lugar que haya pasado el tractor (va haber que usar métodos numéricos y búsqueda de raices de la intersección de las funciones)
#Paso 1: Cargar los datos del archivo de mediciones del otro vehículo
data_list_mediciones2 = []

with open('mnyo_mediciones2.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ')
    
    for row in csv_reader:
        data_list_mediciones2.append(row)

#Paso 1.2: Separar los datos en dos listas, una para x y otra para y
x_mediciones2 = [float(row[0]) for row in data_list_mediciones2]
y_mediciones2 = [float(row[1]) for row in data_list_mediciones2]

#Paso 1.3: Crear una lista que represente el tiempo con el mismo largo que las listas de x e y
t_mediciones2 = np.linspace(0, 100, len(x_mediciones2))

#Paso 2: Crear una función matemática en base a las x mediciones (eje y) y t mediciones (eje x) interpolar usando lagrange
def funcionInterpol2LagrangeX2(t):
    return funcionesTP1.lagrange_interpolation(t, t_mediciones2, x_mediciones2)

#Paso 3: Crear una función matemática en base a las y mediciones (eje y) y t mediciones (eje x) interpolar usando lagrange
def funcionInterpol2LagrangeY2(t):
    return funcionesTP1.lagrange_interpolation(t, t_mediciones2, y_mediciones2)

#Paso 4: Graficar en el eje x lo que de funcionInterpol2LagrangeX2(t) y en el eje y lo que de funcionInterpol2LagrangeY2(t), poner en el mismo gráfico el recorrido del tractor interpolado y el ground truth

x_interpol2 = [funcionInterpol2LagrangeX2(ti) for ti in t]
y_interpol2 = [funcionInterpol2LagrangeY2(ti) for ti in t]

plt.plot(x_interpol, y_interpol, label='Tractor Interpolado')
plt.plot(x_ground_truth, y_ground_truth, label='Tractor Ground Truth')
plt.plot(x_interpol2, y_interpol2, label='Vehículo 2 Interpolado')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de mediciones de tractor y vehículo 2')
plt.show()

#Paso 5: Determinar si el vehículo 2 pasó por algún lugar que haya pasado el tractor
#Paso 5.1: Crear función de intersección por eje
def funcionX(t):
    return funcionInterpol2LagrangeX(t) - funcionInterpol2LagrangeX2(t)

def funcionY(t):
    return funcionInterpol2LagrangeY(t) - funcionInterpol2LagrangeY2(t)

#Paso 5.2: Crear función que busque la intersección por el método de la bisección que me devuelva la cantidad de iteraciones
def biseccion(funcion, a, b, tol):
    if funcion(a) * funcion(b) > 0:
        return None
    count = 0
    while abs(b - a) > tol:
        m = (a + b) / 2
        if funcion(m) == 0:
            return m
        elif funcion(a) * funcion(m) < 0:
            b = m
        else:
            a = m
        count += 1
    return (a + b) / 2, count

#Paso 5.3: Buscar la intersección
interseccion_x = biseccion(funcionX, 0, 100, 0.0001)
interseccion_y = biseccion(funcionY, 0, 100, 0.0001)

print(f'El vehículo 2 pasó por el tractor en el punto ({interseccion_x[0]}, {interseccion_y[0]}) después de {max(interseccion_x[1], interseccion_y[1])} iteraciones')

