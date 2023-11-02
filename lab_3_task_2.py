import numpy as np
from lab_3_task_1 import svobodnoe_padenie as g
a = np.pi / 3
h = 100
b = 30 
V = ((g * h * (np.tan(b) ** 2)) / (2 * (np.cos(a) ** 2) * (1 - np.tan(b) * np.tan(a))))
print(V)

from lab_3_task_1 import chislo_Eylera, postoyannaya_Bolcmana, postoyannaya_planka
e = chislo_Eylera
k = postoyannaya_Bolcmana
h = postoyannaya_planka
E = 300
T = 200

N = (2 / np.pi ** 0.5) * (h / (k * T) ** (3 /2)) * e ** (-E / k * T) * E ** (T / 2)
print(N)
