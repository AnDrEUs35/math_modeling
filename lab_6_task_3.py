import matplotlib.pyplot as plt
import numpy as np

def ellips(x_min, x_max, N, a = 10, b = 5):
    x = np.linspace(x_min, x_max, N)
    y = np.linspace(x_min, x_max, N)

    x, y = np.meshgrid(x, y)

    fxy = x**2 / a**2 + y**2 / b**2 - 1

    plt.contour(x, y, fxy, levels=[0])
    plt.axis('equal')

    plt.savefig('fig_lab_3.png')

ellips(-50, 50, 1000)