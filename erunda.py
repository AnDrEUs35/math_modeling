import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from start_data2 import *
frames = 200
t = np.linspace(0, 10**(-6), frames)

def move_func(s, t):
    (x1, vx1, y1, vy1) = s
    
    dxdt1 = vx1      
    dvxdt1 = k * Q * q1 * x1 / ((x1**2 + y1**2)**1.5 * m)
    dydt1 = vy1
    dvydt1 = k * Q * q1 * y1 / ((x1**2 + y1**2)**1.5 * m)
    return (dxdt1, dvxdt1, dydt1, dvydt1)

k = 9 * 10**9
q1 = -1.67262192 * 10 ** (-27)
Q = 5 * 10 ** (-3)
m = 9.1093837 * 10 ** (-31)

s0 = (x01, vx01, y01, vy01)

sol = odeint(move_func, s0, t)
print(sol)
def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
    elif key == 'line':
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
    return (x1, y1)

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

plt.plot([0], [0], 'o', color='black', ms=20)

def animate(i):
    ball1.set_data(solve_func(i, 'point'))
    ball_line1.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')

edge = 0.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab_12_task_2asdasd.gif')