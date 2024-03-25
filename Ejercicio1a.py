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
equi_points_1a_lagrange = np.linspace(-4,4,9)
# print(equi_points_1a)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a_lagrange = funcionesTP1.eval_points_lister(equi_points_1a_lagrange, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, equi_points_1a_lagrange, eval_points_1a_lagrange)

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
# TODO REHACER SPLINES CON EQUIESPACIADOS USANDO NUEVAS FUNCIONES

#Paso 5: Calculamos el error absoluto
#error_absoluto_splines = 
#TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, error_absoluto_splines)
# plt.xlabel('x')
# plt.ylabel('Error absoluto')
# plt.title('Error absoluto en interpolación Splines')
# plt.show()

#Paso 6: Calculamos el error relativo
# error_relativo_splines =

#TODO: Descomentar para visualizar (y borrar esta linea)
# plt.plot(x, error_relativo_splines)
# plt.xlabel('x')
# plt.ylabel('Error relativo')
# plt.title('Error relativo en interpolación Splines')
# plt.show()

#Paso 7: Hacemos una función para calcular el error dependiendo de la cantidad de puntos que elegimos para interpolar y graficamos
# def error_vs_cantidad_puntos_splines(funcion, x, cantidad_puntos):
#     error = []
#     for n in cantidad_puntos:
#         equi_points = np.linspace(-4, 4, n)
#         eval_points = funcionesTP1.eval_points_lister(equi_points, funcion)
#         interpol = lambda x: funcionesTP1.spline_interpolation(x, equi_points, eval_points)
#         error.append(sum([abs(funcion(xi) - interpol(xi)) for xi in x]))
#     return error

# cantidad_puntos = range(2, 30)
# error = error_vs_cantidad_puntos_splines(funcion1a, x, cantidad_puntos)
# plt.plot(cantidad_puntos, error)
# for i, txt in enumerate(error):
#     plt.annotate(f'{int(txt)}', (cantidad_puntos[i], error[i]))
#     plt.plot([cantidad_puntos[i], cantidad_puntos[i]], [0, error[i]], 'k--')  # Add pointed lines
# plt.xticks(cantidad_puntos)
# plt.xlabel('Cantidad de puntos')
# plt.ylabel('Error')
# plt.title('Error en interpolación Splines en función de la cantidad de puntos')
# plt.show()

#AHORA CON PUNTOS NO EQUIESPACIADOS

#Lagrange
#Paso 1: creamos lista de puntos no equiespaciados para usar como "ground truth" usando los nodos de Chebyshev
cheb_points_1a_lagrange = funcionesTP1.Chebyshev(15)
# print(cheb_points_1a)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a_lagrange_cheb = funcionesTP1.eval_points_lister(cheb_points_1a_lagrange, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aLagrangeNoEquiespaciados(x):
    return funcionesTP1.lagrange_interpolation(x, cheb_points_1a_lagrange, eval_points_1a_lagrange_cheb)

# Paso 4: Graficamos la función original y la interpolada
x = np.linspace(-4, 4, 1000)  # Más puntos para una mejor visualización
y_original_lagrange_Chebyshev = [funcion1a(xi) for xi in x]
y_interpolada_Chebyshev_lagrange = [funcionInterpol1aLagrangeNoEquiespaciados(xi) for xi in x]
# graficar
# plt.plot(x, y_original_lagrange_Chebyshev, label='Función original')
# plt.plot(x, y_interpolada_Chebyshev_lagrange, label='Función interpolada')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interpolación Lagrange con nodos de Chebyshev')
# plt.show()

#Paso 5: Calculamos el error absoluto
error_absoluto_lagrange_Chebyshev = [abs(funcion1a(xi) - funcionInterpol1aLagrangeNoEquiespaciados(xi)) for xi in x]
#graficar
# plt.plot(x, error_absoluto_lagrange_Chebyshev)
# plt.xlabel('x')
# plt.ylabel('Error absoluto')
# plt.title('Error absoluto en interpolación Lagrange con nodos de Chebyshev')
# plt.show()

#Paso 6: Calculamos el error relativo
error_relativo_Chebyshev = [abs(funcion1a(xi) - funcionInterpol1aLagrangeNoEquiespaciados(xi)) / abs(funcion1a(xi)) for xi in x]
#graficar
# plt.plot(x, error_relativo_Chebyshev)
# plt.xlabel('x')
# plt.ylabel('Error relativo')
# plt.title('Error relativo en interpolación Lagrange con nodos de Chebyshev')
# plt.show()

#Paso 7: Hacemos una función para calcular el error dependiendo de la cantidad de puntos que elegimos para interpolar y graficamos
def error_vs_cantidad_puntos_no_equiespaciados(funcion, x, cantidad_puntos):
    error = []
    for n in cantidad_puntos:
        cheb_points = funcionesTP1.Chebyshev(n)
        eval_points = funcionesTP1.eval_points_lister(cheb_points, funcion)
        interpol = lambda x: funcionesTP1.lagrange_interpolation(x, cheb_points, eval_points)
        error.append(sum([abs(funcion(xi) - interpol(xi)) for xi in x]))
    return error

cantidad_puntos = range(2, 17)
error = error_vs_cantidad_puntos_no_equiespaciados(funcion1a, x, cantidad_puntos)
# plt.plot(cantidad_puntos, error)
# for i, txt in enumerate(error):
#     plt.annotate(f'{int(txt)}', (cantidad_puntos[i], error[i]))
#     plt.plot([cantidad_puntos[i], cantidad_puntos[i]], [0, error[i]], 'k--')  # Add pointed lines
# plt.xticks(cantidad_puntos)
# plt.xlabel('Cantidad de puntos')
# plt.ylabel('Error')
# plt.title('Error en interpolación Lagrange con nodos de Chebyshev en función de la cantidad de puntos')
# plt.show()


# No Equiespaciados con Splines

# Establecer parametros para la interpolación
x = funcionesTP1.Chebyshev(30)
y = np.array([funcion1a(xi) for xi in x])
splines = funcionesTP1.Cubic_Splines(x, y)

# Plotear la funcion y la interpolacion
x_plot = np.linspace(-4, 4, 1000)
y_plot = np.array([funcion1a(xi) for xi in x_plot])
plt.plot(x_plot, y_plot, label='Original function')

for i in range(len(splines)):
    xi = np.linspace(x[i], x[i+1], 100)
    y_spline = np.array([funcionesTP1.spline_interpolation(xi, splines, x) for xi in x_plot])
plt.plot(x_plot, y_spline, label='Cubic spline interpolation')

plt.legend()
plt.show()






