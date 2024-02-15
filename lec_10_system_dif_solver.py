import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
'''
t = np.arange(0, 10, 0.01)

def diff_func(z, t):  # z - изменяемая величина для системы
    theta, omega = z

    dtheta_dt = omega
    domega_dt = -k * omega - c * np.sin(theta)

    return dtheta_dt, domega_dt

theta0 = np.pi - 0.1
omega0 = 0

z0 = theta0, omega0
k = 0.25
c = 5

sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 0], 'b')
plt.savefig('fig_1.png')
'''



x = np.arange(1, 3, 0.01)

def diff_func2(z, x):
    y, omega = z

    domega_dx = np.sin(y) * omega - 3 * (x * y) - 5
    dy_dx = omega

    return dy_dx, domega_dx


y0 = 0.01
omega0 = 0.05
z02 = y0, omega0

sol2 = odeint(diff_func2, z02, x)

plt.plot(x, sol2[:, 0], 'b')  # обращаемся к столбцу 0 
plt.plot(x, sol2[:, 1], 'green')  # обращаемся к столбцу 1 
plt.savefig('fig_2.png')

