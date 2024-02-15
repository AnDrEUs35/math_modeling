import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)
def  dubovik(z, t):
    y, w = z
    dy_dt = w
    dw_dt = -4 * w - 5 * y
    return dy_dt, dw_dt
y0 = 4
w0 = -1
z = y0, w0

sol = odeint(dubovik, z, t)

plt.plot(t, sol[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(t, sol[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('lab_10_fig_4.png')
