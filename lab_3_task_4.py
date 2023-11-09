import numpy as np

M = int(input('введите ')) 
N = int(input('введите '))
NxM = np.zeros((N, M))


for i in np.arange(N):
    for j in np.arange(M):
        if i == 0 and j == 0:
            NxM[i, j] = np.sin(N * (i + 1) + M * (j + 1))
        else:
            NxM[i, j] = np.sin(N * i + M * j) 



for i in range(N):
    for j in range(M):
        if NxM[i, j] < 0:
            NxM[i, j] = 0
        elif NxM[i, j] >= 0:
            NxM = NxM
print(NxM)