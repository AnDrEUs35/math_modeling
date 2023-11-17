import numpy as np
kolvo_el = 3
mass = np.zeros((kolvo_el))
for i in range(0, kolvo_el):
    mass[i] = int(input('Введите эл. массива: '))


def my_func(x, y):
    z = None
    for i in range(0, y):
        if z == None:
            z = x[i]
        else:
            z = x[i] * z
    return z

z = my_func(mass, kolvo_el)
print(z)




