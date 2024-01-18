import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# скорость звука в воздухе
v = 343

# определяем функции для рисования синей и красной волн
def drawing1(A, f, x0, v_source, v_observer):
    t = np.linspace(0, 2, 100)
    f_obs = f * (1 + v_source/v) / (1 + v_observer/v)
    y = A * np.sin(f_obs * t)
    x = x0 + t 
    return x, y

def drawing2(A, f, x0, v_source, v_observer):
    t = np.linspace(0, 2, 100)
    f_obs = f * (1 + v_source/v) / (1 + v_observer/v)
    y = A * np.sin(f_obs * t)
    x = x0 + -t
    return x, y

def animate(phi):
    sin1.set_data(drawing1(A=1.5, f=phi, x0=phi * 0.5, v_source=0.5, v_observer=0.5))
    sin2.set_data(drawing2(A=1.5, f=-phi, x0=phi * 0.5, v_source=0.5, v_observer=0.5))

# создаем фигуру и оси
fig, ax = plt.subplots()

sin1, = plt.plot([], [], '-', color='r')
sin2, = plt.plot([], [], '-', color='b')

# устанавливаем пределы осей
edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# сохраняем анимацию в файл GIF
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 5, 70), interval=100)
ani.save('project.gif')