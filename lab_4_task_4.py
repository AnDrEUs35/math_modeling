import numpy as np
a = int(input('Введите первый ограничитель:'))
b = int(input('Введите второй ограничитель:'))
N = int(input('Введите точки:'))
massiv_x = np.linspace(a, b, N)
print(massiv_x)

def function(massiv_x):
    massiv_y = massiv_x ** 2  
    return massiv_y

mass = function(massiv_x)
print(mass)





