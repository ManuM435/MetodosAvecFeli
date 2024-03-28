import funcionesTP1
import numpy as np
import matplotlib.pyplot as plt
# Redefinir en este archivo para evitar problemas de importaciones circulares, y ahorrar espacio de codigo en el futuro del archivo
def funcion1a(x):
    return funcionesTP1.functionFormula1a(x)

# Paso 1: creamos lista de puntos equiespacidos para usar como "ground truth"
equi_points_1a_lagrange = np.linspace(-4, 4, 8) 

# Paso 2: Luego de crear la lista de puntos, evaluamos la función en cada punto
eval_points_1a_lagrange = funcionesTP1.eval_points_lister(equi_points_1a_lagrange, funcion1a)

# Paso 3: Creamos una funcion matematica en base a nuestro "ground truth" para interpolar
def funcionInterpol1aLagrange(x):
    return funcionesTP1.lagrange_interpolation(x, equi_points_1a_lagrange, eval_points_1a_lagrange)

x = np.linspace(-4, 4, 1000)

funcionesTP1.errorPointsPlotter(range(2, 15), funcionesTP1.lagrangeErrorPerPoint(funcion1a, x, range(2, 15), 'equiespaciados'), 'Error', 'Error en interpolación Lagrange por puntos equiespaciados utilizados')

# Generate Chebyshev nodes
chebyshev_nodes = funcionesTP1.Chebyshev(50)

# Evaluate the function at the Chebyshev nodes
eval_points_1a_chebyshev = funcionesTP1.eval_points_lister(chebyshev_nodes, funcion1a)

# Create a mathematical function based on our "ground truth" to interpolate
def funcionInterpol1aChebyshev(x):
    return funcionesTP1.lagrange_interpolation(x, chebyshev_nodes, eval_points_1a_chebyshev)

# Plot the error from Lagrange interpolation in function of points used, but with Chebyshev nodes instead of equidistant points
funcionesTP1.errorPointsPlotter(range(2, 50), funcionesTP1.lagrangeErrorPerPoint(funcion1a, x, range(2, 50), 'chebyshev'), 'Error', 'Error en interpolacion de Lagrange por nodos de Chebyshev utilizados')
