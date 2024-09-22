import matplotlib.pyplot as plt

# Define the quadratic function
def f(x):
    return x**2 + 2*x - 15

# Generate x values from -10 to 10 with a small step size for smoothness
x = [i * 0.1 for i in range(-400, 401)]  # Generates values from -10 to 10 with step size 0.1

# Compute the y values using the quadratic function
y = [f(xi) for xi in x]

# Create the plot
plt.plot(x, y, label='f(x) = x^2 + 2x - 15', color='green')

# Add labels and a title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Quadratic Function f(x) = x^2 + 2x - 15')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)  # Optional: Add grid lines for better readability
plt.show()
