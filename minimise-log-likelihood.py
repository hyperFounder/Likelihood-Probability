import numpy as np
import matplotlib.pyplot as plt

# Define the cost function
def cost_function(p):
    return -np.log(p**5 * (1 - p)**3)

# Define the gradient of the cost function
def gradient(p):
    return -(5/p - 3/(1-p))

# Gradient Descent function
def gradient_descent(p_initial, learning_rate, num_iterations):
    p_values = [p_initial]

    for _ in range(num_iterations):
        p_update = learning_rate * gradient(p_values[-1])
        p_values.append(p_values[-1] - p_update)

    return np.array(p_values)

# Set initial values
p_initial = 0.5
learning_rate = 0.01
num_iterations = 1000

# Run gradient descent
p_values = gradient_descent(p_initial, learning_rate, num_iterations)

# Plot the cost function and the path of gradient descent
p_range = np.linspace(0.001, 0.999, 1000)
cost_values = cost_function(p_range)

plt.plot(p_range, cost_values, label=r'$-\ln(p^5(1-p)^3)$')
plt.scatter(p_values, cost_function(p_values), color='red', label='Gradient Descent Path')
plt.title('Gradient Descent to Minimize Cost Function')
plt.xlabel('p')
plt.ylabel(r'$-\ln(p^5(1-p)^3)$')
plt.legend()
plt.grid(True)
plt.show()
