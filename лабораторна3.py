import math as m
import numpy as np
from scipy.misc import derivative


def f(x):
    return 2 * m.pow(x, 4) + 4 * m.pow(x, 3) - m.pow(x, 2) - 3 * x - 1

eps = 0.0001 #точність

def find_segments():  # відокремлюємо корені
    search_range = np.arange(-10, 10, 1)
    a = None
    previous_x = None
    current_x = None
    segments = []
    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x != None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x=current_x
    return segments

segments=find_segments()

for a, b in segments:
    print(f'Found segment:  [{a}, {b}]')

def nuton(a,b,eps):

    df2 = derivative(f, b, n = 2)

    if (f(b)*df2>0):

        xi = b

    else:

        xi = a

    df = derivative(f,xi, n = 1)

    xi_1 = xi - f(xi)/df

    while (abs(xi_1 - xi)>eps): #accuracy check

        xi = xi_1

        xi_1 = xi - f(xi)/df

    return print ('Solving the equation by Newton*s method x = ', round(xi_1, 4))
a = -2  # початок першого відрізка
b = -1  # кінець першого відрізка
a1 = 0  # початок другого відрізка
b1 = 1  # кінець другого відрізка
print(f'Solution of a nonlinear equation on a segment [{a}, {b}]')
nuton (a,b,eps)
print(f'Solution of a nonlinear equation on a segment [{a1}, {b1}]')
nuton (a1,b1,eps)