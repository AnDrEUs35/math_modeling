import numpy as np



def function(a, b, N):
    massiv_x = np.linspace(a, b, N)
    massiv_y = massiv_x ** 2  
    return massiv_y

mass = function(0, 100, 10)
print(mass)





