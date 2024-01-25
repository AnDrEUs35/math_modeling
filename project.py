import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# определяем функции для рисования синей и красной волн
def drawing1(A, f, x0):
    t = np.linspace(0, 5, 100)
    y = A * np.sin(f * t)
    x = x0 + t 
    return x, y

def drawing2(A, f, x0):
    t = np.linspace(0, 5, 100)
    y = A * np.sin(f * t)
    x = x0 + -t
    return x, y

def circle(f, x0):
    R = 0.2
    x = x0 + R * np.cos(f)
    y = R * np.sin(f)
    return x, y

# как сделать так, чтобы частота волн менялась со временем (я моделирую эффект Доплера)
def animate(phi):
    sin1.set_data(drawing1(A=np.linspace(1.5, 3, 100), f=phi, x0=phi * 0.5))
    sin2.set_data(drawing2(A=np.linspace(1.5, 0.5, 100), f=-phi, x0=phi * 0.5))
    point.set_data(circle(x0=phi * 0.5, f=np.linspace(0, 7, 70)))

# создаем фигуру и оси
fig, ax = plt.subplots()


sin1, = plt.plot([], [], '-', color='r')
sin2, = plt.plot([], [], '-', color='b')
point, = plt.plot([], [], '-', color='green')

# устанавливаем пределы осей
edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# сохраняем анимацию в файл GIF
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 5, 70), interval=100)
ani.save('project.gif')
