import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.01)

def reproduction(N, t):
    dNdt = k * N
    return dNdt

N_0 = 5
k = 0.3

N_t = odeint(reproduction, N_0, t)

plt.plot(t, N_t[:, 0])
plt.savefig('lab_1.png')