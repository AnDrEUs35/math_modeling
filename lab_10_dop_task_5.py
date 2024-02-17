import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

def help_me(z, x):
    y, w = z
    dw_dx = x * w - (1 - x ** 2) - 2 * y
    dy_dx = w
    return dy_dx, dw_dx

y0 = 3
w0 = 0
z = y0, w0

sol = odeint(help_me, z, x)

plt.plot(x, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(x, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_dop_10_fig_5.png')
