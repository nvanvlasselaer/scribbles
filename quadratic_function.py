import matplotlib.pyplot as plt
import numpy as np

def calculate_discriminant(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    return discriminant

def calculate_roots(a, b, discriminant):
    # Calculate roots using the quadratic formula
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        # For complex roots, return None
        return None

def plot_quadratic(a, b, c):
    # Generate x values
    x = np.linspace(-10, 10, 100)

    # Calculate y values using the quadratic equation
    y = a * x**2 + b * x + c

    # Plot the quadratic equation
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

    # Add labels and title
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Quadratic Equation Plot')
    
    # Add a legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

def analyze_roots(a, b, c):
    # Calculate the discriminant
    discriminant = calculate_discriminant(a, b, c)
    
    print(f'Discriminant: {discriminant}')

    if discriminant > 0:
        print('Two distinct real roots.')
        root1, root2 = calculate_roots(a, b, discriminant)
        print(f'Root 1: {root1}, Root 2: {root2}')
    elif discriminant == 0:
        print('One real root (double root).')
        root, = calculate_roots(a, b, discriminant)
        print(f'Root: {root}')
    else:
        print('Complex roots (conjugate pair).')


# Example coefficients for a quadratic equation: y = 2x^2 - 3x + 1
a = -4.905
b = 10
c = 2

plot_quadratic(a, b, c)
analyze_roots(a, b, c)
