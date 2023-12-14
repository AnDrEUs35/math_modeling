import matplotlib.pyplot as plt
import numpy as np

def ellips(x_min, x_max, N, radius = 10):
    x = np.linspace(x_min * radius, x_max * radius, N)
    y = np.linspace(x_min * radius, x_max * radius, N)

    x, y = np.meshgrid()

    fxy = x ** 2 + y ** 2 -radius ** 2









