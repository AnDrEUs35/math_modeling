import numpy as np
x = int(input('введите координату: '))
y = int(input('введите координату: '))
mass = np.zeros((x, y))
a = -1
for i in range(x):
    a += 1
    b = -1
    for i in range(y):
        b += 1
        mass[a, b] = float(input('введите элемент массива: '))
print(mass)
b = -1
for i in range(y):
    b += 1
    a = -1
    c = 0
    for i in range(x):
        a += 1
        if c == 0:
            c = mass[a, b]
        elif mass[a, b] >= c:
            c = mass[a, b]
    print(c)
