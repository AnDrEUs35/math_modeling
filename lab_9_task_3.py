import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def move(V, t):
    dVdt = 10 - 0.6 * V ** 2
    return dVdt
V_0 = 0

V_t = odeint(move, V_0, t)

plt.plot(t, V_t[:, 0])
plt.savefig('lab_3.png')