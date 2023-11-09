import numpy as np

mass = np.zeros((6, 5))
m = [55, 61, 4, 3, 5, 7, 8, 9, 11, 10, 13, 14, 15, 16, 8, 7, 6, 4, 7 ,10, 11, 7, 8, 1, 2, 10, 5, 3, 4, 8]
o = -1
for i in range(6):
    for j in range(5):
        o += 1
        mass[i, j] = m[o]
print(mass)

slice1 = mass[0:2:, 0:2:]
print(slice1)

slice2 = mass[0:1:, 2:5:1]
print(slice2)

slice3 = mass[1:4:, 0]
print(slice3)

slice4 = mass[4:5:1, 2:5:1]
print(slice4)

slice5 = mass[1:3:, 2:4]
print(slice5)

slice6 = mass[2:4:, 1:3:]
print(slice6)

slice7 = mass[4:6:, 0:2:]
print(slice7)

slice8 = mass[4:6:, 2:5:]
print(slice8)

slice9 = mass[1:5:, 2:5:]
print(slice9)