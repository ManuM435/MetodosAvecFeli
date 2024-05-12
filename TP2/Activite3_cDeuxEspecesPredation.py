#Ejercicio 3
import fonctions_auxiliares as aux
import numpy as np
import matplotlib.pyplot as plt

def ODE(n, p, r, a, b, q):
    dNdt = r * n - a * n * p
    dPdt = b * n * p - q * p
    return [dNdt, dPdt]

def LVE(n, p, r, a, b, q, k):
    dNdT = r * n * (1 - n / k) - a * n * p
    dPdt = b * n * p - q * p
    return [dNdT, dPdt]

def rkSolve(ode, y0, t, h):
    # Fijarse si sirve la 2 de species
    return 


#parametros
par0 = (0.1, 0.5, 0.01, 0.66)     #rpos,a,b,q
par1 = (-0.1, 0.5, 0.01, 0.66)     #rneg,a,b,q
par2 = (0, 0.5, 0.01, 0.66)         #r0,a,b,q,k

t0 = 0
tf = 100
num_steps = 1000
t = np.linspace(t0,tf, num_steps)
h = 0.1


#Ejercicio 3
# rpos
y0 = [10, 10]
values0 = rkSolve(ODE, y0, t0,tf,  num_steps, *par0)
t_values0 = values0[0]
y_values0 = values0[1]

#rneg
y0 = [10, 10]
values1 = rkSolve(ODE, y0, t0, tf, num_steps, *par1)
t_values1 = values1[0]
y_values1 = values1[1]

#r0
y0 = [10, 10]
values2 = rkSolve(LVE, y0, t0, tf, num_steps, *par2)
t_values2 = values2[0]
y_values2 = values2[1]

#grafico
plt.plot(t_values0, y_values0, label='rpos')
plt.plot(t_values1, y_values1, label='rneg')
plt.plot(t_values2, y_values2, label='r0')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Población en el tiempo')
plt.legend()
plt.show()

# def EquilibriumPoint_ODE(r,a,b,q):
#     '''Calcula el punto de equilibrio del sistema de ecuaciones diferenciales'''
#     N = q/b
#     P = r/a
#     return [N, P]

# punto_de_equilibrio_0 = (EquilibriumPoint_ODE(*par0))
# punto_de_equilibrio_1 = (EquilibriumPoint_ODE(*par1))
# punto_de_equilibrio_2 = (EquilibriumPoint_ODE(*par2))

# print(f"Los Puntos de Equilibrio son: {punto_de_equilibrio_0}, {punto_de_equilibrio_1}, {punto_de_equilibrio_2}")



