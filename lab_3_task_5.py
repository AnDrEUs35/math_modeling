import numpy as np
from lab_3_task_4 import NxM, M, N

slice1 = NxM[::, 0]

slice2 = NxM[::, 1]
c = []
d = []
for i in range(0, len(slice1)):
    c.append(slice1[i])
    

for i in range(0, len(slice2)):
    d.append(slice2[i])
    
slice1 = np.array(d)
slice2 = np.array(c)

for i in range(len(slice1)):
    NxM[i,0] = slice1[i]

for i in range(len(slice2)):
    NxM[i, 1] = slice2[i]
print(NxM)