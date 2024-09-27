# Plot the following functions using Matplotlib, each on a separate graph.
# f(x)=sin(x)

import matplotlib.pyplot as plt
import math

# Generate x values from 0 to 2π with a small step size for smoothness
x = [i * 0.01 for i in range(int(2 * math.pi / 0.01) + 1)]

# Compute the sine of each x value
y = [math.sin(xi) for xi in x]

# Create the plot
plt.plot(x, y, label='sin(x)', color='blue')

# Add labels and a title
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Continuous Plot of the Sine Function')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)  # Optional: Add grid lines for better readability
plt.show()

