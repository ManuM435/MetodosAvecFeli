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
    plt.show()

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

def funcionSplines1a(n, key: str):
    if n < 3:
        return "-1 (Error al aplicar Splines Cubicos, la cantidad de puntos debe ser mayor a 2)"
    if key == 'equiespaciados':
        x = np.linspace(-4, 4, n)
    else:
        x = Chebyshev(n)
    y = np.array([functionFormula1a(xi) for xi in x])
    splines = Cubic_Splines(x, y)

    # Plotear la funcion y la interpolacion
    x_plot = np.linspace(-4, 4, 1000)
    y_plot = np.array([functionFormula1a(xi) for xi in x_plot])
    plt.plot(x_plot, y_plot, label='Original function')

    point_abs_error = []
    point_rel_error = []
    relative_error = 0

    for i in range(len(splines)):
        y_spline = []
        relative_sum = 0
        xi = np.linspace(x[i], x[i+1], 100)
        for xi in x_plot:
            y_spli = spline_interpolation(xi, splines, x)
            if y_spli is None:
                y_spli = functionFormula1a(xi)
            y_spline.append(y_spli)
            point_abs_error.append(abs(functionFormula1a(xi) - y_spli))
            if functionFormula1a(xi) != 0:
                point_rel_error.append(abs(functionFormula1a(xi) - y_spli) / abs(functionFormula1a(xi)))
            else:
                point_rel_error.append(-1)     
            relative_sum += abs(functionFormula1a(xi) - y_spli) / abs(functionFormula1a(xi))
        relative_error += relative_sum
    relative_error /= len(splines)

    plt.plot(x_plot, y_spline, label='Cubic spline interpolation')
    plt.legend()
    return relative_error


#______________________________________________________________________________________________________
#Ejercicio 1b
def eval_points_lister_R2(list, function):
    eval_list = []
    for i in list:
        eval_list.append(function(i[0], i[1]))
    return eval_list
