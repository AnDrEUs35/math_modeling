import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, vx, y, vy = z

    #dxdt = vx
    dxdt = vx ** 2
    dvxdt = -m * vx
    dydt = vy
    #dydt = vy ** 2
    dvydt = -g - u * m * vy
    return dxdt, dvxdt, dydt, dvydt
g = 9.8
v0 = 20
alpha = 60 * np.pi / 180
u = 0.2
m = 0.5
F = 0.1

x0 = 0
vx0 = v0 * np.cos(alpha)
y0 = 0
vy0 = v0 * np.sin(alpha)

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)

def solve_func(i, key):
    if key =='point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))
ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge= 100
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('lab_11_animation_1.2.gif')