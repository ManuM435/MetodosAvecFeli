#Funciones a utilizar en Ejercicio 1
import numpy as np
import matplotlib.pyplot as plt
import math


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

#Función que reciba un par de puntos y crea una función cúbica que los una y que cumpla las condiciones de splines
def spline_cubico(x0, x1, y0, y1, m0, m1):
    h = x1 - x0
    a = y0
    b = m0
    c = (3*(y1 - y0)/h**2) - ((m1 + 2*m0)/h)
    d = (2*(y0 - y1)/h**3) + ((m1 + m0)/h**2)
    return lambda x: a + b*(x-x0) + c*(x-x0)**2 + d*(x-x0)**3

# #Función que recibe una lista de puntos y una lista de valores de la función en esos puntos y devuelve una lista de funciones cúbicas que unen los puntos y cumplen las condiciones de splines
def spline_interpolation(x, list_x, list_y):
    n = len(list_x)
    h = [list_x[i+1] - list_x[i] for i in range(n-1)]
    alpha = [(3*(list_y[i+1] - list_y[i])/h[i]) - (3*(list_y[i] - list_y[i-1])/h[i-1]) for i in range(1, n-1)]
    l = [1] * (n-1)
    mu = [0] * (n-1)
    z = [0] * (n-1)
    
    for i in range(1, n-1):
        l[i] = 2*(list_x[i+1] - list_x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i-1] - h[i-1]*z[i-1])/l[i]
    
    l.append(1)
    z.append(0)
    c = [0] * n
    b = [0] * n
    d = [0] * n
    
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (list_y[j+1] - list_y[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j])/(3*h[j])
    
    splines = []
    for i in range(n-1):
        splines.append(spline_cubico(list_x[i], list_x[i+1], list_y[i], list_y[i+1], b[i], b[i+1]))
        
    for i in range(n-1):
        if x >= list_x[i] and x <= list_x[i+1]:
            return splines[i](x)
    
    return 0

#Función que crea una lista de nodos de Chebyshev para una interpolación
def chebyshev_nodes(a, b, n):
    return [(a + b)/2 + ((b - a)/2)*math.cos((2*i + 1)*math.pi/(2*n)) for i in range(n)]

#______________________________________________________________________________________________________
#Ejercicio 2
def eval_points_lister_R2(list, function):
    eval_list = []
    for i in list:
        eval_list.append(function(i[0], i[1]))
    return eval_list
