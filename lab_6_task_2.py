import matplotlib.pyplot as plt
import numpy as np

def hiperbola(x_min1, x_max1, x_min2, x_max2, N):
    x = np.linspace(x_min1, x_max1, N)
    k = 10
    y = k / x
    plt.plot(x, y)

    x = np.linspace(x_min2, x_max2, N)
    k = 10
    y = k / x
    plt.plot(x, y)


    plt.savefig('fig_lab_2.png')

x_min1 = -10
x_max1 = -1

x_min2 = 1
x_max2 = 10

if __name__ == '__main__':
    hiperbola(x_min1, x_max1, x_min2, x_max2, 100)