import numpy as np
from constants import svobodnoe_padenie as g
h = float(input('Введите высоту: '))
m = float(input('Введите массу: '))

def energia(h, m, g):
    E = m * g * h
    c = h / 0.5
    mass = np.zeros((int(c), 3))
    i = -1
    for h in np.arange(0, h, 0.5):
        E_pt = m * g * h
        E_kin = E - E_pt
        i += 1
        mass[i, 0] = E_pt
        mass[i, 1] = E_kin
        mass[i, 2] = E
    return mass

      
mass = energia(h, m, g)
print(mass)

