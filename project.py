import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# определяем функции для рисования синей и красной волн
def drawing1(A1, f1, t, x0):
    y1 = A1 * np.sin(f1 * t)
    x = x0 + 100 * t
    return x, y1

def drawing2(A2, f2, t, x0):
    y2 = A2 * np.sin(f2 * t)
    x = x0 + -100 * t
    return x, y2

# определяем функцию обратного вызова для анимации
def animate(i):
    sin1.set_data(drawing1(A1=30, f1=np.linspace(0, 5, 1000) * i, t=np.linspace(0, 1, 1000), x0=0))
    sin2.set_data(drawing2(A2=30, f2=np.linspace(0, np.linspace(1, 3, 1000), 1000) * i, t=np.linspace(0, 1, 1000), x0=0))

# создаем фигуру и оси
fig, ax = plt.subplots()


sin1, = plt.plot([], [], '-', color='r')
sin2, = plt.plot([], [], '-', color='b')

# устанавливаем пределы осей
edge = 200
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# сохраняем анимацию в файл GIF
ani = FuncAnimation(fig, animate, frames=180, interval=60)
ani.save('project.gif')
