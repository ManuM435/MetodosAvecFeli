import numpy as np

def exact_solution(t, N0, r):
    return N0 * np.exp(r * t)

def euler_method(func, initial_condition, t0, tf, num_steps, *args):
    h = (tf - t0) / num_steps  # Step size
    t_values = [t0]
    y_values = [initial_condition]

    t = t0
    y = initial_condition

    for _ in range(num_steps):
        y += h * func(t, y, *args)
        t += h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Define the population growth function
def population_growth(t, N, r):
    return r * N

# Example usage
initial_population = 100  # Initial population
growth_rate = 0.1  # Growth rate
t0 = 0  # Initial time
tf = 10  # Final time
num_steps = 1000  # Number of steps for Euler method

# Compare exact solution with Euler method approximation
t_exact = np.linspace(t0, tf, 1000)  # Time points for exact solution
N_exact = exact_solution(t_exact, initial_population, growth_rate)


# Perform Euler integration
t_values, N_values = euler_method(population_growth, initial_population, t0, tf, num_steps, growth_rate)

# Plot the results
import matplotlib.pyplot as plt

# Plot both exact solution and Euler method approximation
plt.plot(t_values, N_values, label='Euler Method Approximation')
plt.plot(t_exact, N_exact, label='Exact Solution', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Growth: Euler Method vs Exact Solution')
plt.legend()
plt.grid(True)
plt.show()


def runge_kutta_4(func, initial_condition, t0, tf, num_steps, *args):
    h = (tf - t0) / num_steps
    t_values = [t0]
    y_values = [initial_condition]

    t = t0
    y = initial_condition

    for _ in range(num_steps):
        k1 = h * func(t, y, *args)
        k2 = h * func(t + 0.5 * h, y + 0.5 * k1, *args)
        k3 = h * func(t + 0.5 * h, y + 0.5 * k2, *args)
        k4 = h * func(t + h, y + k3, *args)

        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t += h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Example usage with population growth function
initial_population = 100  # Initial population
growth_rate = 0.1  # Growth rate
t0 = 0  # Initial time
tf = 10  # Final time
num_steps = 1000  # Number of steps for RK4 method

# Perform RK4 integration
t_values_rk4, N_values_rk4 = runge_kutta_4(population_growth, initial_population, t0, tf, num_steps, growth_rate)

# Plot the results
plt.plot(t_values_rk4, N_values_rk4, label='RK4 Approximation')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Growth: RK4 Method')
plt.legend()
plt.grid(True)
plt.show()
