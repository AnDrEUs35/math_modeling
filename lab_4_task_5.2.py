import numpy as np

def ploshad(figura, *args):
    if figura == 'круг':
        S = 2 * np.pi * args[0] ** 2
    elif figura == 'прямоугольник':
        S = args[0] * args[1] 
    else:
        rad = args[0] * np.pi / 180 
        S = (args[1] * args[2]) / 2 * np.sin(rad)
    return S

print(ploshad('прямоугольник', 10, 20))
print(ploshad('круг', 10))
print(ploshad('треугольник', 60, 10, 5))
