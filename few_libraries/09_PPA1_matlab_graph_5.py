import math
import matplotlib.pyplot as plt

# Define the logarithmic function
def f(x):
    return math.log(x)

# Generate x values from a small number close to 0 to 10, avoiding zero
x = [i * 0.1 for i in range(1, 101)]  # Generates values from 0.1 to 10 with step size 0.1

# Compute the y values using the logarithmic function
y = [f(xi) for xi in x]

# Create the plot
plt.plot(x, y, label='f(x) = log(x)', color='green')

# Add labels and a title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Logarithmic Function f(x) = log(x)')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)  # Optional: Add grid lines for better readability
plt.show()
