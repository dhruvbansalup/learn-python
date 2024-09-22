import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def f(x):
    return 5 * (x - 1) * (x - 2) * (x - 3)

# Generate x values from 0 to 4 with a fine step size for smoothness
x = np.linspace(0, 4, 400)

# Compute the y values using the polynomial function
y = f(x)

# Create the plot
plt.plot(x, y, label='f(x) = 5(x - 1)(x - 2)(x - 3)', color='blue')

# Add labels and a title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Polynomial Function f(x) = 5(x - 1)(x - 2)(x - 3)')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)  # Optional: Add grid lines for better readability
plt.show()
