import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def catze(z, x):
    y, w = z
    dy_dx = w
    dw_dx = np.sin(x) + np.cos(x)
    return dy_dx, dw_dx

y0 = 3
w0 = 0
z0 = y0, w0
sol = odeint(catze, z0, x)

plt.plot(x, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(x, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_10_fig_3.png')

