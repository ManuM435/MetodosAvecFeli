#Actividad 2: Modelos de competencia Lotka-Volterra
"""Consideremos que en el sistema ahora hay dos especies que compiten por los mismos recursos. La ecuación
logística ya considera la existencia de competencia intraespecífica, debido a que los recursos se transforman
en un limitante a medida que la población se incrementa. Sin embargo, la ecuación logística 4 no es
suficiente si tenemos dos especies en el sistema. Es necesario modelar cómo las dos especies se interrelacionan
estableciendo una competencia entre ellas por los recursos (competencia interespecífica). La forma más
sencilla de modelar la competencia interespecífica es mediante un término que reduzca la capacidad de carga
y sea proporcional a la cantidad de individuos de cada especie. De esta forma se definen las ecuaciones de
competencia de Lotka-Volterra:
dN1
dt
= r1N1
K1 − N1 − α12N2
K1
(5)
dN2
dt
= r2N2
K2 − N2 − α21N1
K2
(6)
Donde para la especie i tenemos que Ni representa su población, Ki su capacidad de carga en el sistema,
ri su tasa intrínseca de crecimiento y αij es el coeficiente de competencia interespecífica de la especie j sobre
la especie i. Y no necesariamente αij = αji."""

"""Ahora que hay un sistema de ecuaciones encontrar la solución exacta no es trivial.
Con el método numérico elegido de la actividad 1, aproximen las soluciones N1(t) y N2(t) utilizando
distintos valores de los parámetros (N1(t = 0), N2(t = 0), r1, r2, K1, K2, α12, α21) de forma que cubran
todos los casos relevantes.
Para obtener más información de las soluciones es importante estudiar los puntos de equilibrio de cada
especie, donde dN1
dt = 0 y dN2
dt = 0. Estos puntos en el grafico de N2 vs N1 definen curvas denominadas
isoclinas cero. Donde se cruzan las isoclinas de cada especie son puntos de equilibrio del sistema, ya que la
2
cantidad de individuos de cada especie permanece constante. Entonces analicen que forma tienen las isoclinas
en este sistema de ecuaciones y determinen sus puntos de equilibrio. Verifiquen que dependiendo de los
parámetros (K1, K2, α12, α21) hay cuatro tipos de gráficos distintos. Para cada tipo de gráfico elijan distintos
valores inicialesN1(t = 0) yN2(t = 0) y grafiquen la evolución temporalN1(t) yN2(t) o sea las trayectorias.
Describan cómo evoluciona el sistema para cada caso dependiendo de las condiciones iniciales. También
pueden graficar el campo de vectores para acompañar la explicación."""

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Definimos las ecuaciones diferenciales
def lotkaVolterra(t, y, r1, r2, K1, K2, alpha12, alpha21):
    N1, N2 = y
    dN1dt = r1 * N1 * (1 - N1 / K1 - alpha12 * N2 / K1)
    dN2dt = r2 * N2 * (1 - N2 / K2 - alpha21 * N1 / K2)
    return [dN1dt, dN2dt]

# Definimos los parámetros
r1 = 0.1
r2 = 0.1
K1 = 1000
K2 = 1000
alpha12 = 0.01
alpha21 = 0.01

# Definimos los valores iniciales
N1_0 = 10
N2_0 = 10
y0 = [N1_0, N2_0]

# Definimos el tiempo
t = np.linspace(0, 100, 1000)

#