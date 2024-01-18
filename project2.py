import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# определяем функции для рисования синей и красной волн
def drawing1(A, f, x0):
    t = np.linspace(0, 2, 100)
    y = A * np.sin(f * t)
    x = x0 + t 
    return x, y

def drawing2(A, f, x0):
    t = np.linspace(0, 2, 100)
    y = A * np.sin(f * t)
    x = x0 + -t
    return x, y

def animate(i):
    f = 1 - (i / 20)
    sin1.set_data(*drawing1(A=1.5, f=f, x0=f * 0.5))
    sin2.set_data(*drawing2(A=1.5, f=-f, x0=f * 0.5))

# создаем фигуру и оси
fig, ax = plt.subplots()

sin1, = plt.plot([], [], '-', color='r')
sin2, = plt.plot([], [], '-', color='b')

# устанавливаем пределы осей
edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# сохраняем анимацию в файл GIF
ani = FuncAnimation(fig, animate, frames=180, interval=100)
ani.save('project_test.gif', writer='pillow')