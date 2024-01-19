import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a range of values for p
p_values = np.linspace(0, 1, 1000)

# Step 2: Calculate the function values for each p
function_values = p_values**5 * (1 - p_values)**3

# Step 3: Plot the function
plt.plot(p_values, function_values, label=r'$p^5(1-p)^3$')
plt.title('Plot of $p^5(1-p)^3$')
plt.xlabel('p')
plt.ylabel(r'$p^5(1-p)^3$')
plt.legend()
plt.grid(True)
plt.show()
