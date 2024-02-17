import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.01)

def I_dont_know(z, t):
    y, w = z
    dwdt = 1 ** 0.5 - w
    dydt = w
    return dwdt, dydt
y0 = 1
w0 = 0
z = y0, w0

sol = odeint(I_dont_know, z, t)

plt.plot(t, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(t, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_dop_10_fig_3.png')