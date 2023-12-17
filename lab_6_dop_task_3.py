import matplotlib.pyplot as plt
import  numpy as np

x = np.arange(0, 100, 0.1)
a = 5
b = 87
for i in x:
    if x[i] < a:
        x = a ** 2
        y =  a ** 2
    elif x[i] >= a and x[i] <= b:
        x = x ** 2
        y = x
    else:
        x = b ** 2
        y = x


plt.plot(x, y)
plt.axis('equal')








plt.savefig('fig_dop_3')

