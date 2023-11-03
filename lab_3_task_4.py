import numpy as np
#A[i, j] = sin(N · i + M · j) 
M = int(input('введите ')) 
N = int(input('введите '))
NxM = np.zeros((N, M))


for i in np.arange(N):
    for j in np.arange(M):
        NxM[i, j] = np.sin(N * (i + 1) + M * (j + 1))


for i in range(N):
    for j in range(M):
        if NxM[i, j] < 0:
            NxM[i, j] = 0
        elif NxM[i, j] >= 0:
            NxM = NxM
print(NxM)