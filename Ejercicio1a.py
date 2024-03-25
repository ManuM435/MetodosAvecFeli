#Ejercicio 1a
#INTERPOLACIÓN CON PUNTOS EQUIESPACIADOS
#Interpolación lagrange
import funcionesTP1
import numpy as np
import matplotlib.pyplot as plt
import math

# Redefinir en este archivo para evitar problemas de importaciones circulares, y ahorrar espacio de codigo en el futuro del archivo
def funcion1a(x):
    return funcionesTP1.functionFormula1a(x)

# Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_1a_lagrange = np.linspace(-4, 4, 9) 
# KNOTE0 || Se toman 9 puntos equiespaciados para la interpolacion porque se determino que es el punto donde el error es minimo
# Esto se determino con el grafico de error relativo en funcion de la cantidad de puntos

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a_lagrange = funcionesTP1.eval_points_lister(equi_points_1a_lagrange, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, equi_points_1a_lagrange, eval_points_1a_lagrange)

#Paso 4: Creamos lista de puntos para graficar
x = np.linspace(-4, 4, 1000)

# Paso 5: Graficamos la función original y la interpolada
funcionesTP1.equiespPlotFor1a(x, funcionInterpol1aLagrange, 'Interpolación Lagrange')

# # KNOTE1 || Para el Apendice, error absoluto por punto en Lagrange Equiespaciado
# # Paso 6: Calculamos y Graficamos el error absoluto
# error_absoluto_lagrange = [abs(funcion1a(xi) - funcionInterpol1aLagrange(xi)) for xi in x]
# funcionesTP1.errorPlotter(x, error_absoluto_lagrange, 'Error Absoluto', 'Error absoluto en interpolación Lagrange con pts equiespaciados')

# # KNOTE2 || Para el Apendice, error relativo por punto en Lagrange Equiespaciado
# # Paso 7: Calculamos y graficamos el error relativo
# error_relativo = []
# for xi in x:
#     if funcion1a(xi) != 0:
#         error_relativo.append(abs(funcion1a(xi) - funcionInterpol1aLagrange(xi)) / abs(funcion1a(xi)))
#     else: # Caso excepcion si se divide por 0
#         error_relativo.append(-1)
# funcionesTP1.errorPlotter(x, error_relativo, 'Error Relativo', 'Error relativo en interpolación Lagrange con pts equiespaciados')

#Paso 8: Calculamos y Graficamos los distintos valores de error en cada cantidad de puntos tomados en Lagrange
# Esto sirve para ver que cantidad n de puntos da menos error (determinamos que n=8 da el menor error posible)
funcionesTP1.errorPointsPlotter(range(2, 15), funcionesTP1.lagrangeErrorPerPoint(funcion1a, x, range(2, 15), 'equiespaciados'), 'Error', 'Error en interpolación Lagrange en función de la cantidad de puntos')

# Ahora equiespaciados pero con Splines
errorRelativoEqui = []
funcionesTP1.funcionSplines1a(30, 'equiespaciados')
plt.show()

for a in range(6, 31):
    errorRelativoEqui.append(funcionesTP1.funcionSplines1a(a, 'equiespaciados'))
plt.clf()

plt.plot(range(6, 31), errorRelativoEqui)
for i, error in enumerate(errorRelativoEqui):
    plt.annotate(f'{error:.2f}', (i+6, error))
    plt.plot([i+6, i+6], [0, error], 'k--')  # Para lineitas punteadas
plt.xticks(range(6, 31))
plt.xlabel('x')
plt.ylabel('Error Relativo')
plt.title('Error relativo en interpolación Splines con puntos equiespaciados')
plt.show()

# # KNOTE3 || EL ERROR (relativo) POR PUNTO ES SIEMPRE EL MISMO EN SPLINES, POR LO QUE ES REDUNDANTE HACER UN GRAFICO DE ERROR POR PUNTO
# # O eso creo, y podriamos hablar de eso

# # KNOTE4 || Para el Apendice, grafico mostrando que con range menor a 6 puntos, se va todo muy lejos y distorsiona la vision del grafico
# # for a in range(3, 31):
# #     errorRelativoPuntos.append(funcionesTP1.funcionSplines1a(a, 'equiespaciados'))
# # plt.clf()
# # Para el Apendice, grafico mostrando que con range menor a 9 puntos, se va todo muy lejos y distorsiona la vision del grafico
# # plt.plot(range(3, 31), errorRelativoPuntos)
# # plt.xlabel('Cantidad de puntos')
# # plt.ylabel('Error Relativo')
# # plt.title('Error relativo en interpolación Splines con nodos de Chebyshev en función de la cantidad de puntos')
# # plt.show()

# Ahora puntos no-equiespaciados

#Lagrange
#Paso 1: creamos lista de puntos no equiespaciados para usar como "ground truth" usando los nodos de Chebyshev
cheb_points_1a_lagrange = funcionesTP1.Chebyshev(23)
# KNOTE5 || Se toman 23 puntos no equiespaciados para la interpolacion porque se determino que es el punto donde el error es minimo
# Esto se determino con el grafico de error relativo en funcion de la cantidad de puntos

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a_lagrange_cheb = funcionesTP1.eval_points_lister(cheb_points_1a_lagrange, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aLagrangeNoEquiespaciados(x):
    return funcionesTP1.lagrange_interpolation(x, cheb_points_1a_lagrange, eval_points_1a_lagrange_cheb)

# Paso 4: Graficamos la función original y la interpolada
funcionesTP1.chevyPlotFor1a(1000, funcionInterpol1aLagrangeNoEquiespaciados, 'Interpolación Lagrange con nodos de Chebyshev')

# # KNOTE6 || Para el Apendice, error absoluto por punto en Lagrange No-Equiespaciado
# # Paso 5: Calculamos y Graficamos el error absoluto
# error_absoluto_lagrange_Chebyshev = [abs(funcion1a(xi) - funcionInterpol1aLagrangeNoEquiespaciados(xi)) for xi in x]
# funcionesTP1.errorPlotter(x, error_absoluto_lagrange_Chebyshev, 'Error Absoluto', 'Error absoluto en interpolación Lagrange con nodos de Chebyshev')

# # KNOTE7 || Para el Apendice, error relativo por punto en Lagrange No-Equiespaciado
# # Paso 6: Calculamos y Graficamos el error relativo
# error_relativo_Chebyshev = [abs(funcion1a(xi) - funcionInterpol1aLagrangeNoEquiespaciados(xi)) / abs(funcion1a(xi)) for xi in x]
# funcionesTP1.errorPlotter(x, error_relativo_Chebyshev, 'Error Relativo', 'Error relativo en interpolación Lagrange con nodos de Chebyshev')

#Paso 7:Calculamos el error dependiendo de la cantidad de puntos que elegimos para interpolar y graficamos
funcionesTP1.errorPointsPlotter(range(2, 25), funcionesTP1.lagrangeErrorPerPoint(funcion1a, x, range(2, 25), 'no_equiespaciados'), 'Error', 'Error en interpolación Lagrange con nodos de Chebyshev en función de la cantidad de puntos')

# No Equiespaciados con Splines

# La funcion Splines1a agrega todos los puntos al plot, y a la vez devuelve el error relativo de la interpolacion con splines cubicos
# Se combinan estas funciones para ahorrar grandes cantidades de codigo y de tiempo de ejecucion

errorRelativoPuntos = []
funcionesTP1.funcionSplines1a(30, 'chebyshev')
plt.show()

for a in range(9, 31):
    errorRelativoPuntos.append(funcionesTP1.funcionSplines1a(a, 'chebyshev'))
plt.clf()
plt.plot(range(9, 31), errorRelativoPuntos)
for i, error in enumerate(errorRelativoPuntos):
    plt.annotate(f'{error:.2f}', (i+9, error))
    plt.plot([i+9, i+9], [0, error], 'k--') # Para lineitas punteadas
plt.xticks(range(9, 31))
plt.xlabel('x')
plt.ylabel('Error Relativo')
plt.title('Error relativo en interpolación Splines con nodos de Chebyshev')
plt.show()

# # KNOTE8 || Para el Apendice, grafico mostrando que con range menor a 9 puntos, se va todo muy lejos y distorsiona la vision del grafico
# # for a in range(3, 31):
# #     errorRelativoPuntos.append(funcionesTP1.funcionSplines1a(a, chebyshev))
# # plt.clf()
# # plt.plot(range(3, 31), errorRelativoPuntos)
# # plt.xlabel('Cantidad de puntos')
# # plt.ylabel('Error Relativo')
# # plt.title('Error relativo en interpolación Splines con nodos de Chebyshev en función de la cantidad de puntos')
# # plt.show()

print("Todo ok")

