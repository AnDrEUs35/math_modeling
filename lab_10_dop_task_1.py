import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-2, -0.5, 0.01)

def pimkin(w, t):
    x, y, z = w
    dx_dt = 3 * x - y + z
    dy_dt = x + y + z
    dz_dt = 4 * x - y + 4 * z
    return dx_dt, dy_dt, dz_dt

x0 = -71
y0 = 1
z0 = -3
w = x0, y0, z0
sol = odeint(pimkin, w, t)

plt.plot(t, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(t, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.plot(t, sol[:, 2], 'red')
plt.savefig('lab_dop_10_fig_1.png')
