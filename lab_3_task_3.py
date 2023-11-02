import numpy as np
from lab_3_task_1 import svobodnoe_padenie as g

x0 = float(input('введите х0: '))
y0 = float(input('введите y0: '))
v0x = float(input('введите v0x: '))
v0y = float(input('введите v0y: '))
t = np.arange(0, 5, 0.1)

x = x0 + v0x * t
y = x0 + v0y * t - (g * t ** 2) / 2

result = np.zeros((len(t), 3))
for i in range(len(t)):
    result[i, 0] = t[i]
    result[i, 1] = x[i]
    result[i, 2] = y[i]
    
print(result)
