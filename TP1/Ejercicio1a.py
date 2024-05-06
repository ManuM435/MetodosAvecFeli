import TP1.funcionesTP1 as funcionesTP1
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Redefinir en este archivo para evitar problemas de importaciones circulares, y ahorrar espacio de codigo en el futuro del archivo
def funcion1a(x):
    return funcionesTP1.functionFormula1a(x)

# Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_lag = np.linspace(-4, 4, 8) 
equi_points_spl = np.linspace(-4, 4, 20)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_lag = funcionesTP1.eval_points_lister(equi_points_lag, funcion1a)
eval_points_spl = funcionesTP1.eval_points_lister(equi_points_spl, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, equi_points_lag, eval_points_lag)

#Paso 4: Creamos lista de puntos para graficar
x = np.linspace(-4, 4, 1000)

# Paso 5: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar con CubicSpline
cubic_spline = CubicSpline(equi_points_spl, eval_points_spl)

# Paso 6: Evaluamos la función de cubic spline en los puntos x
y_cubic_spline = cubic_spline(x)

# Paso 7: Graficamos la función original y la interpolada
y_original = [funcion1a(xi) for xi in x]
y_interpolada = [funcionInterpol1aLagrange(xi) for xi in x]
plt.plot(x, y_original, label='Función original')
plt.plot(x, y_interpolada, label='Función interpolada con Lagrange')
plt.plot(x, y_cubic_spline, label='Función interpolada con Cubic Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación con Lagrange y Cubic Spline en Puntos Equiespaciados')
plt.legend()
plt.show()

# Paso 1: creamos lista de puntos de Chebyshev para usar como "ground truth"
cheby_points_lag = funcionesTP1.Chebyshev(20)
cheby_points_spl = funcionesTP1.Chebyshev(20)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_cheby_lag = funcionesTP1.eval_points_lister(cheby_points_lag, funcion1a)
eval_points_cheby_spl = funcionesTP1.eval_points_lister(cheby_points_spl, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aChebyLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, cheby_points_lag, eval_points_cheby_lag)

# Paso 5: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar con CubicSpline
cubic_spline_cheby = CubicSpline(cheby_points_spl, eval_points_cheby_spl)

# Paso 6: Evaluamos la función de cubic spline en los puntos x
y_cubic_spline_cheby = cubic_spline_cheby(x)

# Paso 7: Graficamos la función original y la interpolada
y_interpolada_cheby = [funcionInterpol1aChebyLagrange(xi) for xi in x]
plt.plot(x, y_original, label='Función original')
plt.plot(x, y_interpolada_cheby, label='Función interpolada con Lagrange')
plt.plot(x, y_cubic_spline_cheby, label='Función interpolada con Cubic Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación con Lagrange y Cubic Spline en nodos de Chebyshev')
plt.legend()
plt.show()


# Definir una función para calcular el error relativo promedio
def average_relative_error(original_values, interpolated_values):
    return np.mean(np.abs((original_values - interpolated_values) / original_values))

# Definir un rango para el número de puntos
num_points_range = range(6, 61)

# Inicializar una lista para almacenar los errores relativos promedio
average_errors = []

# Bucle sobre el número de puntos
for num_points in num_points_range:
    # Crear puntos equidistantes
    equi_points = np.linspace(-4, 4, num_points)
    
    # Evaluar la función en estos puntos
    eval_points = funcionesTP1.eval_points_lister(equi_points, funcion1a)
    
    # Crear una interpolación de spline cúbica
    cubic_spline = CubicSpline(equi_points, eval_points)
    
    # Evaluar el spline cúbico en los puntos x
    y_cubic_spline = cubic_spline(x)
    
    # Calcular el error relativo promedio y añadirlo a la lista
    average_errors.append(average_relative_error(y_original, y_cubic_spline))

plt.clf()
# Initialize lists to store the average errors for equidistant points and Chebyshev nodes
average_errors_equi = []
average_errors_cheby = []

# Loop over the number of points
for num_points in num_points_range:
    # Create equidistant points and Chebyshev nodes
    equi_points = np.linspace(-4, 4, num_points)
    cheby_points = funcionesTP1.Chebyshev(num_points)

    # Evaluate the function at these points
    eval_points_equi = funcionesTP1.eval_points_lister(equi_points, funcion1a)
    eval_points_cheby = funcionesTP1.eval_points_lister(cheby_points, funcion1a)

    # Create cubic spline interpolations
    cubic_spline_equi = CubicSpline(equi_points, eval_points_equi)
    cubic_spline_cheby = CubicSpline(cheby_points, eval_points_cheby)

    # Evaluate the cubic spline interpolations at the points x
    y_cubic_spline_equi = cubic_spline_equi(x)
    y_cubic_spline_cheby = cubic_spline_cheby(x)

    # Calculate the average relative errors and add them to the lists
    average_errors_equi.append(average_relative_error(y_original, y_cubic_spline_equi))
    average_errors_cheby.append(average_relative_error(y_original, y_cubic_spline_cheby))

# Plot the average relative errors
plt.semilogy(num_points_range, average_errors_equi, label='Puntos Equidistantes')
plt.semilogy(num_points_range, average_errors_cheby, label='Nodos de Chebyshev')
plt.xlabel('Numero de Puntos')
plt.ylabel('Error Relativo')
plt.title('Error Relativo en base a cantidad de puntos con Splines Cubicos')
plt.xticks(np.arange(min(num_points_range), max(num_points_range)+1, 3))
plt.legend()
plt.xticks(np.arange(min(num_points_range), max(num_points_range)+1, 3))
for i, txt in enumerate(average_errors):
    if i % 5 == 0: 
        plt.annotate(f"{txt:.4f}", (num_points_range[i], average_errors[i]))
plt.show()





