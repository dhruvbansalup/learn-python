# Sin and cos on same graph

import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π with a small step size for smoothness
x = np.linspace(0, 2 * np.pi, 400)  # 400 points between 0 and 2π

# Compute the y values for sin(x) and cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.plot(x, y_sin, label='f(x) = sin(x)', color='blue')  # Plot sin(x)
plt.plot(x, y_cos, label='g(x) = cos(x)', color='red')   # Plot cos(x)

# Add labels and a title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x) = sin(x) and g(x) = cos(x)')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)  # Optional: Add grid lines for better readability
plt.show()
