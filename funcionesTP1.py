#Funciones a utilizar en Ejercicio 1
import numpy as np
import matplotlib.pyplot as plt
import math

# Funcion 1a
def functionFormula1a(x):
    return (0.3**(abs(x)) * math.sin(4*x)) - math.tanh(2*x) + 2

#Función que evalúa una función en una lista de puntos
def eval_points_lister(list, function):
    eval_list = []
    for i in list:
        eval_list.append(function(i))
    return eval_list


#Función que interpola un punto con el método de Lagrange
def lagrange_interpolation(x, list_x, list_y):
    n = len(list_x)
    result = 0
    for i in range(n):
        term = list_y[i]
        for j in range(n):
            if j != i:
                term *= (x - list_x[j]) / (list_x[i] - list_x[j])
        result += term
    return result

def equiespPlotFor1a(points: list, InterpolFunction, InterpolMethod: str):
    y_original = [functionFormula1a(xi) for xi in points]
    y_interpolada = [InterpolFunction(xi) for xi in points]
    plt.plot(points, y_original, label='Función original')
    plt.plot(points, y_interpolada, label='Función interpolada')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(InterpolMethod)
    plt.show()

def chevyPlotFor1a(n, InterpolFunction, InterpolMethod: str):
    points = Chebyshev(n)
    y_original = [functionFormula1a(xi) for xi in points]
    y_interpolada = [InterpolFunction(xi) for xi in points]
    plt.plot(points, y_original, label='Función original')
    plt.plot(points, y_interpolada, label='Función interpolada')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(InterpolMethod)
    plt.show()

def lagrangeErrorPerPoint(funcion, x, cantidad_puntos, pointType: str):
    error = []
    for n in cantidad_puntos:
        points = np.linspace(-4, 4, n) if pointType == 'equiespaciados' else Chebyshev(n)
        eval_points = eval_points_lister(points, funcion)
        interpol = lambda x: lagrange_interpolation(x, points, eval_points)
        error.append(sum([abs((funcion(xi) - interpol(xi)) / funcion(xi)) for xi in x]))
    return error

def errorPlotter(x, error, errorType, errorTitle):
    plt.plot(x, error)
    plt.xlabel('x')
    plt.ylabel(errorType)
    plt.title(errorTitle)
    plt.show()

def errorPointsPlotter(points, error, errorType, errorTitle):
    plt.plot(points, error)
    for i, txt in enumerate(error):
        plt.annotate(f'{int(txt)}', (points[i], error[i]))
        plt.plot([points[i], points[i]], [0, error[i]], 'k--')  # Para lineitas punteadas
    plt.xticks(points)
    plt.xlabel('Cantidad de puntos')
    plt.ylabel(errorType)
    plt.title(errorTitle)
    plt.xticks(points[::3])
    plt.show()

#Función que crea una lista de nodos de Chebyshev para una interpolación
def Chebyshev(x):
    x = np.cos(np.linspace(0, np.pi, x))
    x = 4 * x  # Multiplicar por 4 para extender de [-1, 1] a [-4, 4].
    x = np.sort(x)
    return x

#______________________________________________________________________________________________________
#Ejercicio 1b
def eval_points_lister_R2(list, function):
    eval_list = []
    for i in list:
        eval_list.append(function(i[0], i[1]))
    return eval_list

#Función que interpola con el método de lagrange en R2 usando las funciones ya creadas de interpolador lagrange
def interpolador_lagrange_R2(x1, x2, points, values):
    result = 0
    n = len(points)
    for i in range(n):
        term = values[i]
        for j in range(n):
            if j != i:                
                term *= (x1 - points[j][0]) / (points[i][0] - points[j][0])
                term *= (x2 - points[j][1]) / (points[i][1] - points[j][1])
        result += term
    return result

#Función que encuentra raíz usando el método de Newton-Rhapson
def newtonRaphson(p0,funcion,derivada, error):
    iteracionesMax = 1000
    p = p0
    for i in range(0,iteracionesMax):
        pAnterior = p
        p = pAnterior - funcion(pAnterior)/derivada(pAnterior)
        if abs(p-pAnterior) < error:
            print("El valor de p es: ", p, "\nEn la iteración: ", i)
            return p, i+1

    print("El método no converge")
    return None