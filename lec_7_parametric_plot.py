import numpy as np
import matplotlib.pyplot as plt

def ellips(a=5, b = 20):
    t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    x = a * np.cos(t)
    y = b * np.sin(t)


    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig1.png')

if __name__ == '__main__':
    ellips()