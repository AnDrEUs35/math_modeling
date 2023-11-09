import numpy as np
import random as r

mass = np.zeros(10)

for i in range(10):
    mass[i] = r.randint(0, 1000)
print(mass)
i = -1
for h in range(0, len(mass)):
    i += 1
    c = i + 1
    if mass[0] > mass[1]:
        mass[0] = mass[1]
        if mass[c] > 10:
            break     
print(mass)


