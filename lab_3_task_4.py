import numpy as np
#A[i, j] = sin(N · (i+1) + M · (j + 1)) 
M = int(input('введите'))
N = int(input('введите'))
NxM = np.zeros(N, M)
i = np.arange(0, N)
j = np.arange(0, M)

for i in range(N):
    i += 1
    for j in range(M):
        j += 1
        NxM[i, j] = np.sin(N * i + M * j)

print(NxM)







