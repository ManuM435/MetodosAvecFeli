#Ejercicio 3
import fonctions_auxiliares as aux

def ODE(n,p,r,a,b,q):
    dNdt = r*n - a*n*p
    dPdt = b*n*p - q*p
    return [dNdt, dPdt]

def LVE(n,p,r,a,b,q,k):
    dNdT = r*n*(1-n/k) - a*n*p
    dPdt = b*n*p - q*p
    return [dNdT, dPdt]

def rkSolve(ode, y0, t, h):
    '''Resuelve el sistema de ecuaciones diferenciales con el método de Runge-Kutta'''
    return aux.runge_kutta_4(ode, y0, t, h)

#datos
datos0 = (10, 10, 0.1, 0.5, 0.01, 0.66)     #n,p,r,
