import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def i_love_rabbits(w, x):
    y, z = w
    dy_dx = y ** 2 * z
    dz_dx = z / x - y * z ** 2
    return dy_dx, dz_dx

z0 = -3
y0 = 1
w = y0, z0

sol = odeint(i_love_rabbits, w, x)

plt.plot(x, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(x, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_10_fig_1.png')
