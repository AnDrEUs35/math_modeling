import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from start_data import *

plt.style.use('dark_background')
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def  move_func(s, t):
    ( x1, vx1, y1, vy1, 
      x2, vx2, y2, vy2,
      xw, vxw, yw, vyw,
      xm, vxm, ym, vym,
      xf, vxf, yf, vyf) = s
#земля
    dxdt1 = vx1
    dvxdt1 = -G * m * x1 / (x1**2 + y1**2) ** 1.5
    dydt1 = vy1
    dvydt1 = -G * m * y1 / (x1**2 + y1**2) ** 1.5
#меркурий
    dxdt2 = vx2
    dvxdt2 = -G * m * x2 / (x2**2 + y2**2) ** 1.5
    dydt2 = vy2
    dvydt2 = -G * m * y2 / (x2**2 + y2**2) ** 1.5
#венера
    dxdt3 = vxw
    dvxdt3 = -G * m * xw / (xw**2 + yw**2) ** 1.5
    dydt3 = vyw
    dvydt3 = -G * m * yw / (xw**2 + yw**2) ** 1.5
#марс
    dxdt4 = vxm
    dvxdt4 = -G * m * xm / (xm**2 + ym**2) ** 1.5
    dydt4 = vym
    dvydt4 = -G * m * ym / (xm**2 + ym**2) ** 1.5
#фаэтон
    dxdt5 = vxf
    dvxdt5 = -G * m * xf / (xf**2 + yf**2) ** 1.5
    dydt5 = vyf
    dvydt5 = -G * m * yf / (xf**2 + yf**2) ** 1.5

    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2,
            dxdt3, dvxdt3, dydt3, dvydt3,
            dxdt4, dvxdt4, dydt4, dvydt4,
            dxdt5, dvxdt5, dydt5, dvydt5)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)


s0 = (x0e,  vx0e,  y0e,  vy0e,
      x0me, vx0me, y0me, vy0me,
      x0w,  vx0w,  y0w,  vy0w,
      x0m,  vx0m,  y0m,  vy0m,
      x0f,  vx0f,  y0f,  vy0f)

sol = odeint(move_func, s0, t)

def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        
        x4 = sol[i, 12]
        y4 = sol[i, 14]

        x5 = sol[i, 16]
        y5 = sol[i, 18]

    elif key == 'line':
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]

        x5 = sol[:i, 16]
        y5 = sol[:i, 18]
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='white')
ball_line3, = plt.plot([], [], '-', color='white')

ball4, = plt.plot([], [], 'o', color='green')
ball_line4, = plt.plot([], [], '-', color='green')

ball5, = plt.plot([], [], 'o', color='purple')
ball_line5, = plt.plot([], [], '-', color='purple')

plt.plot([0], [0], 'o', color='orange', ms=20)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])

    ball5.set_data(solve_func(i, 'point')[4])
    ball_line5.set_data(solve_func(i, 'line')[4])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')

edge = 4*x0e
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab_12_task_1.gif')