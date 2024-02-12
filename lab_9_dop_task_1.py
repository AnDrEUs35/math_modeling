import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 30, 0.1)

def meteorit(t):
    dhdt = 10 * t
    return dhdt

V_t = odeint(meteorit, t)

plt.plot(t, V_t[:, 0])
plt.savefig('dop_lab_3.png')