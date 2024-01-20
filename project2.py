import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем функции для рисования синей и красной волн
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

def circle(f, x0):
    R = 0.2
    x = x0 + R * np.cos(f)
    y = R * np.sin(f)
    return x, y

# Скорости источника и наблюдателя
v_source = 0.1  # Скорость источника, движущегося к наблюдателю
v_observer = 0  # Скорость наблюдателя
c = 1  # Скорость света

# Начальная частота волн
f0 = 1

def animate(phi):
    # Вычисляем частоту волн в зависимости от относительной скорости
    f = f0 * (1 + v_source / c) / (1 - v_source * np.cos(phi) / c)
    
    # Обновляем данные для синей и красной волн
    sin1.set_data(*drawing1(A=1.5, f=f, x0=phi))
    sin2.set_data(*drawing2(A=1.5, f=-f, x0=phi))
    
    # Обновляем данные для точки
    x, y = circle(x0=phi, f=phi)
    point.set_data(x, y)

# Создаем фигуру и оси
fig, ax = plt.subplots()

sin1, = plt.plot([], [], '-', color='r')
sin2, = plt.plot([], [], '-', color='b')
point, = plt.plot([], [], 'o', color='green')

# Устанавливаем пределы осей
edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# Сохраняем анимацию в файл GIF
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 180), interval=50)
ani.save('project_test.gif', writer='imagemagick')

plt.show()
