import numpy as np
figura = str(input("Выберите площадь какой фигуры вам надо найти(круг, прямоугольник, треугольник): "))

def ploshad(figura):
    if figura == 'круг':
        R = float(input('Введите радиус: '))
        S = 2 * np.pi * R ** 2
    elif figura == 'прямоугольник':
        a = float(input('Введите a: '))
        b = float(input('Введите b: '))
        S = a * b
    else:
        print('Выберите формулу:')
        print('1. S = (a * b) / 2 * sinY \n2. S = (a * b) / 2 \n3. S = a / 2 * h')
        formula = int(input('Выберите номер формулы: '))
        if formula == 1:
            a = float(input('Введите a: '))
            b = float(input('Введите b: '))
            ugol = int(input('Введите градус угла: '))
            rad = ugol * np.pi / 180 
            S = (a * b) / 2 * np.sin(rad) # синус в радианах
        elif formula == 2:
            a = float(input('Введите a: '))
            b = float(input('Введите b: '))
            S = (a * b) / 2
        elif formula == 3:
            a = float(input('Введите a: '))
            h = float(input('Введите h: '))
            S = a / 2 * h
    return S

S = ploshad(figura)
print(S)

