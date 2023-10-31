import numpy as np
mass1 = np.zeros(5)
mass2 = []
x = -1
for i in range(4):
    x += 1
    for i in range(1):
        mass1[x] = float(input('Введите элемент массива: '))  
        mass2.append(mass1[x])  


x = int(input('Введите координату: '))
mass1[x] = float(input('Введите элемент массива: '))


y = 4 - x
z = x -1
if x == 4:
    print(mass1)
elif x != 4:
    for i in range(y):
        x += 1
        z += 1
        for i in range(1):
            mass1[x] = mass2[z]
    print(mass1)