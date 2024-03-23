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
