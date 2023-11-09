import numpy as np
from lab_3_task_4 import NxM, M, N
x = int(input('введите номер столбца'))
y = int(input('введите номер столбца'))

slice1 = NxM[::, x]
slice2 = NxM[::, y]
print(slice1)
print(slice2)

c = []
d = []
for i in range(0, len(slice1)):
    c.append(slice1[i])
    d.append(slice2[i])
    
slice1 = np.array(d)
slice2 = np.array(c)

for i in range(len(slice1)):
    NxM[i, x] = slice1[i]
    NxM[i, y] = slice2[i]
print(NxM)