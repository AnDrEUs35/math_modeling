import numpy as np

a = np.zeros((4, 3))
b = np.zeros((4, 3))
c = np.zeros((4, 3))


x = -1
for i in range(4):
    x += 1
    y = -1
    for i in range(3):
        y += 1
        a[x, y] = int(input('введите массив а: '))
        
x = -1
for i in range(4):
    x += 1
    y = -1
    for i in range(3):
        y += 1
        b[x, y] = int(input('введите массив b: '))
x = -1
for i in range(4):
    x += 1
    y = -1 
    for i in range(3):
        y += 1
        if a[x, y] > b[x, y]:
            c[x, y] = a[x, y] 
        elif a[x, y] == b[x, y]:    
            c[x, y] = a[x, y]
        elif a[x, y] < b[x, y]:
            c[x, y] = b[x, y] 
print(c)





