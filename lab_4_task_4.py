import numpy as np
a = int(input('Введите первый ограничитель:'))
b = int(input('Введите второй ограничитель:'))



def function(a, b):
    c = (b - a) / 0.2
    i = -1
    mass = np.zeros((int(c), 2))
    for x in np.arange(a, b, 0.2):
        y = x ** 2
        i += 1
        mass[i, 0] = x
        mass[i, 1] = y
    return mass

mass = function(a, b)
print(mass)





