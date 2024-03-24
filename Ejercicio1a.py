#Ejercicio 1a
#INTERPOLACIÓN CON PUNTOS EQUIESPACIADOS
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
def funcionInterpol1aLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, equi_points_1a, eval_points_1a)

# Paso 4: Graficamos la función original y la interpolada
x = np.linspace(-4, 4, 1000)  # Más puntos para una mejor visualización
y_original = [funcion1a(xi) for xi in x]
y_interpolada = [funcionInterpol1aLagrange(xi) for xi in x]

# TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, y_original, label='Función original')
# plt.plot(x, y_interpolada, label='Función interpolada')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interpolación Lagrange')
# plt.show()

#Paso 5: Calculamos el error absoluto
error_absoluto_lagrange = [abs(funcion1a(xi) - funcionInterpol1aLagrange(xi)) for xi in x]

# TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, error_absoluto_lagrange)
# plt.xlabel('x')
# plt.ylabel('Error absoluto')
# plt.title('Error absoluto en interpolación Lagrange')
# plt.show()

#Paso 6: Calculamos el error relativo
error_relativo = [abs(funcion1a(xi) - funcionInterpol1aLagrange(xi)) / abs(funcion1a(xi)) for xi in x]

# TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, error_relativo)
# plt.xlabel('x')
# plt.ylabel('Error relativo')
# plt.title('Error relativo en interpolación Lagrange')
# plt.show()

#Paso 7: Hacemos una función para calcular el error dependiendo de la cantidad de puntos que elegimos para interpolar y graficamos
def error_vs_cantidad_puntos(funcion, x, cantidad_puntos):
    error = []
    for n in cantidad_puntos:
        equi_points = np.linspace(-4, 4, n)
        eval_points = funcionesTP1.eval_points_lister(equi_points, funcion)
        interpol = lambda x: funcionesTP1.lagrange_interpolation(x, equi_points, eval_points)
        error.append(sum([abs(funcion(xi) - interpol(xi)) for xi in x]))
    return error

cantidad_puntos = range(2, 17)
error = error_vs_cantidad_puntos(funcion1a, x, cantidad_puntos)
# plt.plot(cantidad_puntos, error)
# for i, txt in enumerate(error):
#     plt.annotate(f'{int(txt)}', (cantidad_puntos[i], error[i]))
#     plt.plot([cantidad_puntos[i], cantidad_puntos[i]], [0, error[i]], 'k--')  # Add pointed lines
# plt.xticks(cantidad_puntos)
# plt.xlabel('Cantidad de puntos')
# plt.ylabel('Error')
# plt.title('Error en interpolación Lagrange en función de la cantidad de puntos')
# plt.show()

#AHORA LO MISMO PERO CON SPLINES
#Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_1a = np.linspace(-4,4,16)
# print(equi_points_1a)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a = funcionesTP1.eval_points_lister(equi_points_1a, funcion1a)

# Paso 3: Definimos una función que cree funciones cúbicas entre los puntos que cumplas las condiciones de splines
def funcionInterpol1aSplines(x):
    return funcionesTP1.spline_interpolation(x, equi_points_1a, eval_points_1a)

# Paso 4: Graficamos la función original y la interpolada
x = np.linspace(-4, 4, 1000)  # Más puntos para una mejor visualización
y_originalSplines = [funcion1a(xi) for xi in x]
y_interpoladaSplines = [funcionInterpol1aSplines(xi) for xi in x]
# TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, y_originalSplines, label='Función original')
# plt.plot(x, y_interpoladaSplines, label='Función interpolada')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interpolación Splines')
# plt.show()

#Paso 5: Calculamos el error absoluto
error_absoluto_splines = [abs(funcion1a(xi) - funcionInterpol1aSplines(xi)) for xi in x]
#TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, error_absoluto_splines)
# plt.xlabel('x')
# plt.ylabel('Error absoluto')
# plt.title('Error absoluto en interpolación Splines')
# plt.show()

#Paso 6: Calculamos el error relativo
error_relativo_splines = [abs(funcion1a(xi) - funcionInterpol1aSplines(xi)) / abs(funcion1a(xi)) for xi in x]

#TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, error_relativo_splines)
# plt.xlabel('x')
# plt.ylabel('Error relativo')
# plt.title('Error relativo en interpolación Splines')
# plt.show()

#Paso 7: Hacemos una función para calcular el error dependiendo de la cantidad de puntos que elegimos para interpolar y graficamos
def error_vs_cantidad_puntos_splines(funcion, x, cantidad_puntos):
    error = []
    for n in cantidad_puntos:
        equi_points = np.linspace(-4, 4, n)
        eval_points = funcionesTP1.eval_points_lister(equi_points, funcion)
        interpol = lambda x: funcionesTP1.spline_interpolation(x, equi_points, eval_points)
        error.append(sum([abs(funcion(xi) - interpol(xi)) for xi in x]))
    return error

cantidad_puntos = range(2, 30)
error = error_vs_cantidad_puntos_splines(funcion1a, x, cantidad_puntos)
# plt.plot(cantidad_puntos, error)
# for i, txt in enumerate(error):
#     plt.annotate(f'{int(txt)}', (cantidad_puntos[i], error[i]))
#     plt.plot([cantidad_puntos[i], cantidad_puntos[i]], [0, error[i]], 'k--')  # Add pointed lines
# plt.xticks(cantidad_puntos)
# plt.xlabel('Cantidad de puntos')
# plt.ylabel('Error')
# plt.title('Error en interpolación Splines en función de la cantidad de puntos')
# plt.show()
