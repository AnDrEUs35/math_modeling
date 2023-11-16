import numpy as np

kolvo = 5
mass = []

for i in range(0, kolvo):
    mass.append(int(input('Введите эл. массива: ')))
mass = np.array(mass)

i = -1

def sr_arifm(x, y):
    srednee = None
    for i in range(0, y):
        if srednee == None:
            srednee = x[i]
        elif srednee != None:
            srednee = srednee + x[i] 
    srednee = srednee / y    
    return srednee

srednee = sr_arifm(mass, kolvo)
print(srednee)


