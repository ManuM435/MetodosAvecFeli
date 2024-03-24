import numpy as np
import matplotlib.pyplot as plt
import math
import funcionesTP1

def funcion1b(x1,x2):
    return 0.75*math.exp(-((10*x1 - 2)**2/(4))  ((9*x2 - 2)**2/(4))) + 0.65*math.exp(-((9*x1 + 1)**2/(9)) - ((10*x2 + 1)**2/(2))) + 0.55*math.exp(-((9*x1 - 6)**2/(4)) - ((9*x2 - 3)**2/(4))) - 0.01*math.exp(((9*x1 - 7)**2/(4)) - ((9*x2 - 3)**2/(4)))

#Ejercicio 1 punto b
#PUNTOS EQUIESPACIADOS
#Lagrange

#Paso 1: Crear los puntos equiespaciados