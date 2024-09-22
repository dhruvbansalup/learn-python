import math
import matplotlib.pyplot as plt

# Define the exponential function
def f(x):
    return math.exp(x)

# Generate x values from -2 to 2 with a small step size for smoothness
x = [i * 0.1 for i in range(-20, 21)]  # Generates values from -2 to 2 with step size 0.1

# Compute the y values using the exponential function
y = [f(xi) for xi in x]

# Create the plot
plt.plot(x, y, label='f(x) = e^x', color='red')

# Add labels and a title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Exponential Function f(x) = e^x')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)  # Optional: Add grid lines for better readability
plt.show()
