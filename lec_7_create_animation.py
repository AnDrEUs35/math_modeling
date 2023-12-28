import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # объект анимации

xdata, ydata = [], [] # координаты

ax.set_xlim(0, 2 * np.pi) # пределы изменения переменной х
ax.set_ylim(-1, 1) # пределы изменения переменной y

# функция подстановки координат
def update(frame):
    xdata.append(frame) # рассчет координаты х
    ydata.append(np.sin(frame)) # рассчет координаты у
    anim_object.set_data(xdata, ydata) # передача координат

ani = FuncAnimation(fig, # вызов пространства
                    update, frames = np.arange(0, 2 * np.pi, 0.1),
                    interval=100 # интервал между кадрами
                    )# по умолчанию 200 милисекунд 
ani.save('animation.gif')