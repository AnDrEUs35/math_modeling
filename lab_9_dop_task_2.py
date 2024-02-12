import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 200)

def Victoria(k, a, angle, t, S):
    dSdt = k * (S / np.pi) ** 0.5 * a * S * np.cos(angle)
    return dSdt

angle = np.linspace(0, 90, 200) + np.linspace(90, 0, 200) * np.pi / 180
k = 0.1
a = 1360.8
S_0 = 0.16

S_t = odeint(Victoria, k, a, angle, t, S_0)

plt.plot(t, S_t[:, 0])
plt.savefig('dop_lab_2.png')


