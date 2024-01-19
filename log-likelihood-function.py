import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a range of values for p
p_values = np.linspace(0.001, 0.999, 1000)  # Avoid log(0) by excluding 0 and 1

# Step 2: Calculate the negative log of the function for each p
negative_log_values = -np.log(p_values**5 * (1 - p_values)**3)

# Step 3: Plot the negative log of the function
plt.plot(p_values, negative_log_values, label=r'$-\ln(p^5(1-p)^3)$')
plt.title('Plot of $-\ln(p^5(1-p)^3)$')
plt.xlabel('p')
plt.ylabel(r'$-\ln(p^5(1-p)^3)$')
plt.legend()
plt.grid(True)
plt.show()
