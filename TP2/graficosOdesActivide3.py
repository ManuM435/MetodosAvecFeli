#odes tp 2
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 0.5    # Tasa de crecimiento de las presas
alpha = 0.1 # Eficiencia de captura de los predadores
beta = 0.02 # Eficiencia de conversión de presas en nuevos predadores
q = 0.1     # Tasa de mortalidad per cápita de los predadores

# Rango de valores para N y P
N = np.linspace(0, 50, 400)
P = np.linspace(0, 50, 400)

# Gráfica de dN/dt variando r
fig, ax = plt.subplots()
for r_val in [0.3, 0.5, 0.7]:
    dN_dt = r_val * N - alpha * N * 10  # Asumimos P constante
    ax.plot(N, dN_dt, label=f'r={r_val}')
ax.set_xlabel('N (Número de presas)')
ax.set_ylabel('dN/dt')
ax.legend()
ax.set_title('dN/dt vs N variando r')
plt.grid()
plt.show()

# Gráfica de dN/dt variando alpha
fig, ax = plt.subplots()
for alpha_val in [0.05, 0.1, 0.2]:
    dN_dt = r * N - alpha_val * N * 10  # Asumimos P constante
    ax.plot(N, dN_dt, label=f'alpha={alpha_val}')
ax.set_xlabel('N (Número de presas)')
ax.set_ylabel('dN/dt')
ax.legend()
ax.set_title('dN/dt vs N variando alpha')
plt.grid()
plt.show()

# Gráfica de dP/dt variando beta
fig, ax = plt.subplots()
for beta_val in [0.01, 0.02, 0.03]:
    dP_dt = beta_val * 10 * P - q * P  # Asumimos N constante
    ax.plot(P, dP_dt, label=f'beta={beta_val}')
ax.set_xlabel('P (Número de predadores)')
ax.set_ylabel('dP/dt')
ax.legend()
ax.set_title('dP/dt vs P variando beta')
plt.grid()
plt.show()

# Gráfica de dP/dt variando q
fig, ax = plt.subplots()
for q_val in [0.05, 0.1, 0.15]:
    dP_dt = beta * 10 * P - q_val * P  # Asumimos N constante
    ax.plot(P, dP_dt, label=f'q={q_val}')
ax.set_xlabel('P (Número de predadores)')
ax.set_ylabel('dP/dt')
ax.legend()
ax.set_title('dP/dt vs P variando q')
plt.grid()
plt.show()

# Parámetros adicionales
K = 50  # Capacidad de carga del ambiente para las presas

# Gráfica de dN/dt variando K
fig, ax = plt.subplots()
for K_val in [30, 50, 70]:
    dN_dt = r * N * (1 - N / K_val) - alpha * N * 10  # Asumimos P constante
    ax.plot(N, dN_dt, label=f'K={K_val}')
ax.set_xlabel('N (Número de presas)')
ax.set_ylabel('dN/dt')
ax.legend()
ax.set_title('dN/dt vs N variando K')
plt.grid()
plt.show()

# Gráfica de dN/dt variando r (modelo extendido)
fig, ax = plt.subplots()
for r_val in [0.3, 0.5, 0.7]:
    dN_dt = r_val * N * (1 - N / K) - alpha * N * 10  # Asumimos P constante
    ax.plot(N, dN_dt, label=f'r={r_val}')
ax.set_xlabel('N (Número de presas)')
ax.set_ylabel('dN/dt')
ax.legend()
ax.set_title('dN/dt vs N variando r (modelo extendido)')
plt.grid()
plt.show()

# Gráfica de dN/dt variando alpha (modelo extendido)
fig, ax = plt.subplots()
for alpha_val in [0.05, 0.1, 0.2]:
    dN_dt = r * N * (1 - N / K) - alpha_val * N * 10  # Asumimos P constante
    ax.plot(N, dN_dt, label=f'alpha={alpha_val}')
ax.set_xlabel('N (Número de presas)')
ax.set_ylabel('dN/dt')
ax.legend()
ax.set_title('dN/dt vs N variando alpha (modelo extendido)')
plt.grid()
plt.show()
