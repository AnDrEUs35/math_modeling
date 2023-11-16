import numpy as np
srednee = 0
i = -1
def sr_arifm(x):
    for i in range(0, max(x)):
        if srednee == 0:
            srednee = x[i]
        else:
            srednee = srednee + x[i]  
    return srednee

srednee = sr_arifm

mass = np.zeros((3))
for i in range(0, 3):
    mass[i] = int(input('Введите эл. массива: ')) 

sr_arifm(mass)

print(sr_arifm(srednee))


