import numpy as np


def sr_arifm(array):
    s = 0
    for i in range(len(array)):
        s += array[i]
        
    return s / len(array)


mass = np.arange(100)
srednee = sr_arifm(mass)
print(srednee)


