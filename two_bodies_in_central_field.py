import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def  move_func(s, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2) = s

    dxdt1 = vx1
    dvxdt1 = -G * m * x1 / (x1**2 + y1**2) ** 1.5
    dydt1 = vy1
    dvydt1 = -G * m * y1 / (x1**2 + y1**2) ** 1.5

    dxdt2 = vx2
    dvxdt2 = -G * m * x2 / (x2**2 + y2**2) ** 1.5
    dydt2 = vy2
    dvydt2 = -G * m * y2 / (x2**2 + y2**2) ** 1.5
    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x01 = 149 * 10**9
vx01 = 0
y01 = 0
vy01 = 30000

x02 = 0
vx02 = -47360
y02 = 0.387 * 149 * 10**9
vy02 = 0
s0 = (x01, vx01, y01, vy01,
      x02, vx02, y02, vy02)

sol = odeint(move_func, s0, t)

def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
    elif key == 'line':
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
    return ((x1, y1), (x2, y2))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

plt.plot([0], [0], 'o', color='orange', ms=20)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])
    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')

edge = 2*x01
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('earth_sun2.gif')
