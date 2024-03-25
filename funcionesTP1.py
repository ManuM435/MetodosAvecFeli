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

#TODO
#Funcion para calcular el error absoluto


#Funcion para calcular el error relativo


# Funciones de Interpolacion de Splines Cúbicos
def Cubic_Splines(x, y):
    splines = []
    m_prev, c_prev = 0, 0

    for i in range(len(x) - 2):
        h = x[i+1] - x[i]
        h_next = x[i+2] - x[i+1]
        d = 6 * ((y[i+2] - y[i+1]) / h_next - (y[i+1] - y[i]) / h)
        a = h
        b = 2 * (h + h_next)
        c = h_next
        d_next = 6 * ((y[i+3] - y[i+2]) / (x[i+3] - x[i+2]) - (y[i+2] - y[i+1]) / h_next) if i < len(x) - 3 else 0
        m_next = (d - a * m_prev) / (b - a * c_prev) if i > 0 else d / b
        splines.append((y[i], (y[i+1] - y[i]) / h - h * (2 * m_prev + m_next) / 6, m_prev / 2, (m_next - m_prev) / (6 * h)))
        m_prev, c_prev = m_next, c

    return splines

def spline_interpolation(x, splines, x_values):
    for i in range(len(splines)):
        if x >= x_values[i] and x <= x_values[i+1]:
            return splines[i][0] + splines[i][1] * (x - x_values[i]) + splines[i][2] * (x - x_values[i]) ** 2 + splines[i][3] * (x - x_values[i]) ** 3
    return None

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