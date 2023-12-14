import matplotlib.pyplot as plt
import numpy as np
#f(x, y) = 0

def cilcle_plotter(radius=10):
    x = np.arange(-2 * radius, 2 * radius, 0.1)
    y = np.arange(-2 * radius, 2 * radius, 0.1)

    # переход к неявнозаданным координатам
    x, y = np.meshgrid(x, y)

    fxy = x ** 2 + y ** 2 - radius ** 2 # ур-е окружности

    # команда рисования
    plt.contour(x, y, fxy, levels=[0])
    plt.axis('equal') # ОТКЛЮЧЕНИЕ МАСШТАБИРОВАНИЯ

    plt.savefig('fig_4.png')

if __name__ == '__main__':
    cilcle_plotter()