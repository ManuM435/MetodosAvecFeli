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
#Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_1a_splines = np.linspace(-4,4,16)
# print(equi_points_1a)

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a_splines = funcionesTP1.eval_points_lister(equi_points_1a_splines, funcion1a)

# Paso 3: Definimos una función que cree funciones cúbicas entre los puntos que cumplas las condiciones de splines
def funcionInterpol1aSplines(x):
    return funcionesTP1.spline_interpolation(x, equi_points_1a_splines, eval_points_1a_splines)

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

#AHORA CON PUNTOS NO EQUIESPACIADOS
#Lagrange
#Paso 1: creamos lista de puntos no equiespaciados para usar como "ground truth" usando los nodos de Chebyshev
cheb_points_1a_lagrange = funcionesTP1.chebyshev_nodes(-4, 4, 15)
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
        cheb_points = funcionesTP1.chebyshev_nodes(-4, 4, n)
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


# Con Splines

# Define the number of points
n = 30  # Modify this value to change the number of nodes

# Generar Nodos de Chebyshev
x = np.cos(np.linspace(0, np.pi, n))
x = 4 * x  # Multiplicar por 4 para extender de [-1, 1] a [-4, 4].

# Sort x in ascending order and calculate the corresponding y values
x = np.sort(x)
y = np.array([funcion1a(xi) for xi in x])

# Create the cubic spline for each interval
splines = []
# Initialize m_prev and c_prev
m_prev, c_prev = 0, 0

def calculate_splines(x, y):
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

# Calculate the splines
splines = calculate_splines(x, y)

# Plot the function and the interpolation
x_plot = np.linspace(-4, 4, 1000)
y_plot = np.array([funcion1a(xi) for xi in x_plot])
plt.plot(x_plot, y_plot, label='Original function')

def spline_interpolation(x, splines, x_values):
    for i in range(len(splines)):
        if x >= x_values[i] and x <= x_values[i+1]:
            return splines[i][0] + splines[i][1] * (x - x_values[i]) + splines[i][2] * (x - x_values[i]) ** 2 + splines[i][3] * (x - x_values[i]) ** 3
    return None


for i in range(len(splines)):
    xi = np.linspace(x[i], x[i+1], 100)
    y_spline = np.array([spline_interpolation(xi, splines, x) for xi in x_plot])
plt.plot(x_plot, y_spline, label='Cubic spline interpolation')

plt.legend()
plt.show()






# TODO ESTO PUEDE QUE SEA IRRELEVANT Y BORRABLE

#Ahora con splines
#Paso 1: creamos lista de puntos no equiespacidos para usar como "ground truth" usando los nodos de Chebyshev
# cheb_points_1a_splines = funcionesTP1.chebyshev_nodes(-4, 4, 15)
# print(cheb_points_1a_splines)

# # Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
# eval_points_1a_splines_cheb = funcionesTP1.eval_points_lister(cheb_points_1a_splines, funcion1a)

# # Paso 3: Definsimos una función que cree funciones cúbicas entre los puntos que cumplas las condiciones de splines
# def funcionInterpol1aSplinesNoEquiespaciados(x):
#     return funcionesTP1.spline_interpolation(x, cheb_points_1a_splines, eval_points_1a_splines_cheb)

# # Paso 4: Graficamos la función original y la interpolada
# x_range = np.linspace(-4, 4, 50)
# y_originalSplines_Chebyshev = [funcion1a(xi) for xi in x_range]
# y_interpoladaSplines_Chebyshev = [funcionInterpol1aSplinesNoEquiespaciados(xi) for xi in x_range]

# # graficar
# plt.plot(x_range, y_originalSplines_Chebyshev, label='Función original')
# plt.plot(x_range, y_interpoladaSplines_Chebyshev, label='Función interpolada')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interpolación Splines con nodos de Chebyshev')
# plt.show()