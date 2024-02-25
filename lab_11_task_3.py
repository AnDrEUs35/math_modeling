import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 10000, frames)

def move_func(z, t):
    x, vx, y, vy = z
    dxdt = vx
    dvxdt = k1 * (A - x - y)
    dydt = vx
    dvydt = k2 * (A - x - y)
    return dxdt, dvxdt, dydt, dvydt

k1 = 0.3
k2 = 0.7
A = 10
x0 = 0
vx0 = 0
vy0 = 0
y0 = 0

z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)

def solve_func(i):
    x = sol[:i, 0]
    y = sol[:i, 2]
    return x, y

fig, ax = plt.subplots()
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball_line.set_data(solve_func(i))
ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 30
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('lab_11_animation_3.gif')