import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from start_data2 import *
frames = 200
t = np.linspace(0, 10**(-6), frames)

def move_func(s, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2,
     x3, vx3, y3, vy3,
     x4, vx4, y4, vy4,
     x5, vx5, y5, vy5,
     x6, vx6, y6, vy6) = s
    
    dxdt1 = vx1 # - синий
    dvxdt1 = k * Q * q * x1 / ((x1**2 + y1**2)**1.5 * m)
    dydt1 = vy1
    dvydt1 = k * Q * q * y1 / ((x1**2 + y1**2)**1.5 * m)
    
    dxdt2 = vx2 # + красный
    dvxdt2 = k * Q * -q * x2 / ((x2**2 + y2**2)**1.5 * m)
    dydt2 = vy2
    dvydt2 = k * Q * -q * y2 / ((x2**2 + y2**2)**1.5 * m)

    dxdt3 = vx3 # - коричневый
    dvxdt3 = k * Q * q * x3 / ((x3**2 + y3**2)**1.5 * m)
    dydt3 = vy3
    dvydt3 = k * Q * q * y3 / ((x3**2 + y3**2)**1.5 * m)

    dxdt4 = vx4 # - зеленый
    dvxdt4 = k * Q * q * x4 / ((x4**2 + y4**2)**1.5 * m)
    dydt4 = vy4
    dvydt4 = k * Q * q * y4 / ((x4**2 + y4**2)**1.5 * m)
    
    dxdt5 = vx5 # + пурпурный
    dvxdt5 = k * Q * -q * x5 / ((x5**2 + y5**2)**1.5 * m)
    dydt5 = vy5
    dvydt5 = k * Q * -q * y5 / ((x5**2 + y5**2)**1.5 * m)

    dxdt6 = vx6 # + голубой
    dvxdt6 = k * Q * -q * x6 / ((x6**2 + y6**2)**1.5 * m)
    dydt6 = vy6
    dvydt6 = k * Q * -q * y6 / ((x6**2 + y6**2)**1.5 * m)
    
    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2,
            dxdt3, dvxdt3, dydt3, dvydt3,
            dxdt4, dvxdt4, dydt4, dvydt4,
            dxdt5, dvxdt5, dydt5, dvydt5,
            dxdt6, dvxdt6, dydt6, dvydt6) 

k = 9 * 10**9
q = -1.67262192 * 10 ** (-27)
Q = 5 * 10 ** (-3)
m = 9.1093837 * 10 ** -31

s0 = (x01, vx01, y01, vy01,
      x02, vx02, y02, vy02,
      x03, vx03, y03, vy03,
      x04, vx04, y04, vy04,
      x05, vx05, y05, vy05,
      x06, vx06, y06, vy06)

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

        x6 = sol[i, 20]
        y6 = sol[i, 22]

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

        x6 = sol[:i, 20]
        y6 = sol[:i, 22]
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='brown')
ball_line3, = plt.plot([], [], '-', color='brown')

ball4, = plt.plot([], [], 'o', color='green')
ball_line4, = plt.plot([], [], '-', color='green')

ball5, = plt.plot([], [], 'o', color='purple')
ball_line5, = plt.plot([], [], '-', color='purple')

ball6, = plt.plot([], [], 'o', color='skyblue')
ball_line6, = plt.plot([], [], '-', color='skyblue')

plt.plot([0], [0], 'o', color='black', ms=20)

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

    ball6.set_data(solve_func(i, 'point')[5])
    ball_line6.set_data(solve_func(i, 'line')[5])
ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')

edge = 0.5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('lab_12_task_2.gif')
