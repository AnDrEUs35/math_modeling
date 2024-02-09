import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 8, 0.01)

def invest(N, t):
    dNdt = -0.08 * N * t
    return dNdt

N_0 = 1000
N_t = odeint(invest, N_0, t)

plt.plot(t, N_t[:, 0])
plt.savefig('lab_2.png')
