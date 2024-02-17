import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.01)
def shieldkrote(z, x):
    y, w = z
    dwdx = w ** 2 + y - (3 * y ** 2) / x ** 0.5
    dydx = w
    return dydx, dwdx
y0 = 0
w0 = 1
z = y0, w0

sol = odeint(shieldkrote, z, x)

plt.plot(x, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(x, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_dop_10_fig_2.png')