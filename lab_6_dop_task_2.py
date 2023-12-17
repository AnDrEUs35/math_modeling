import matplotlib.pyplot as plt
import  numpy as np

f = np.pi * 8
e = np.arange(0.01, 0.99, 0.001)
p = np.arange(1, 99, 0.1)

r = p / (1 + e * np.cos(f))

x = r * np.cos(f)
y = r * np.sin(f)

plt.plot(x, y)
plt.savefig('fig_dop_2')













