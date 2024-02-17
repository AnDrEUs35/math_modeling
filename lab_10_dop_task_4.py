import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.001)
def raven(z, x):
    y, w = z
    dwdx = (4 * x**2 + 0.5) * y - x * w - x**2
    dydx = w
    return dydx, dwdx
y0 = 3
w0 = 0

z = y0, w0

sol = odeint(raven, z, x)

plt.plot(x, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(x, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_dop_10_fig_4.png')