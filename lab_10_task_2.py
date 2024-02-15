import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def merschwimen(z, t):
    x, y = z
    dx_dt = 3 * x - 2 * y + (np.e ** (3 * t) / (np.e ** t + 1))
    dy_dt = x - (np.e ** (3 * t) / (np.e ** t + 1))
    return dx_dt, dy_dt

x0 = 5
y0 = -7
z  = x0, y0

sol = odeint(merschwimen, z, t)

plt.plot(t, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(t, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_10_fig_2.png')
