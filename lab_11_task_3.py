import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, vx, y, vy = z
    dxdt = vx
    dydt = vy
    dvxdt = k1 * (A - vx - vy)
    dvydt = k2 * (A - vx - vy)
    return dxdt, dvxdt, dydt, dvydt
k1 = 0.2
k2 = 0.3
A = 30
v0 = 0
alpha = 60 * np.pi / 180

x0 = 0
vx0 = v0 * np.cos(alpha)
y0 = 0
vy0 = v0 * np.sin(alpha)

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)

def solve_func(i, key):
    if key =='point':
        x = sol[i, 0]
        y = sol[i, 1]
    else:
        x = sol[:i, 0]
        y = sol[:i, 1]
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))
ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 40
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('lab_11_animation_3.gif')