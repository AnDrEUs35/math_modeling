import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, vx, y, vy = z

    dxdt = vx
    dvxdt = 0
    dydt = vy
    dvydt = g - k / m * y
    return dxdt, dvxdt, dydt, dvydt

g = 9.8
v = 0.1
k = 5
m = 1.5

x0 = 0
vx0 = 0
y0 = 10
vy0 = v

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

ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)

ani.save('lab_11_animation_4.gif')