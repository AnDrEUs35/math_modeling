import numpy as np
from lab_3_task_1 import svobodnoe_padenie as g

x0 = int(input('введите х0: '))
y0 = int(input('введите y0: '))
v0 = int(input('введите v0: '))
t = int(input('введите t(0 - 5 секунд): '))

a = []

x = x0 + v0 * t
y = y0 + v0 * t - (g * t ** 2 / 2)

a.append(t)
a.append(x)
a.append(y)
result = np.array(a)
print(result)

