import matplotlib.pyplot as plt
import  numpy as np

t = np.arange(-100, 100, 0.01)
a = 1
A = 1
b = 2
B = 1

x = A * np.sin(a * t + np.pi / 2)
y = B * np.sin(b * t)

plt.plot(x, y, label='lissazhu', marker='o')
plt.legend()
plt.grid()
plt.savefig('fig_dop_1.png')



