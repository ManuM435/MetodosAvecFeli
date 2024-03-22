#Ejercicio 1a
#Interpolación lagrange
import funcionesTP1
import numpy as np
import matplotlib.pyplot as plt
import math

def funcion1a(x):
    return (0.3**(abs(x)) * math.sin(4*x)) - math.tanh(2*x) + 2

#Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_1a = np.linspace(-4,4,9)
# print(equi_points_1a)

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
# plt.show()

#Paso 5: Calculamos el error absoluto
error_absoluto = [abs(funcion1a(xi) - funcionInterpol1a(xi)) for xi in x]
plt.plot(x, error_absoluto)
plt.xlabel('x')
plt.ylabel('Error absoluto')
plt.title('Error absoluto en interpolación Lagrange')
# plt.show()

#Paso 6: Calculamos el error relativo
error_relativo = [abs(funcion1a(xi) - funcionInterpol1a(xi)) / abs(funcion1a(xi)) for xi in x]
plt.plot(x, error_relativo)
plt.xlabel('x')
plt.ylabel('Error relativo')
plt.title('Error relativo en interpolación Lagrange')
# plt.show()

#Paso 7: Hacemos una función para calcular el error dependiendo de la cantidad de puntos que elegimos para interpolar y graficamos
def error_vs_cantidad_puntos(funcion, funcionInterpol, x, cantidad_puntos):
    error = []
    for n in cantidad_puntos:
        equi_points = np.linspace(-4, 4, n)
        eval_points = funcionesTP1.eval_points_lister(equi_points, funcion)
        interpol = lambda x: funcionesTP1.lagrange_interpolation(x, equi_points, eval_points)
        error.append(sum([abs(funcion(xi) - interpol(xi)) for xi in x]))
    return error

cantidad_puntos = range(2, 20)
error = error_vs_cantidad_puntos(funcion1a, funcionInterpol1a, x, cantidad_puntos)
plt.plot(cantidad_puntos, error)
plt.xlabel('Cantidad de puntos')
plt.ylabel('Error')
plt.title('Error en interpolación Lagrange en función de la cantidad de puntos')
plt.show()
