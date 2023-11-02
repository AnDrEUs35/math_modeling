import numpy as np
#A[i, j] = sin(N · (i+1) + M · (j + 1)) 
M = int(input('введите ')) 
N = int(input('введите '))
NxM = np.zeros((N, M))
a = -1

for i in np.arange(N):
    a += 1
    b = -1
    for j in np.arange(M):
        b += 1
        NxM[a, b] = np.sin(N * (a + 1) + M * (b + 1))


a = -1
for i in range(N):
    a += 1
    b = -1
    for i in range(M):
        b += 1
        if NxM[a, b] < 0:
            NxM[a, b] = 0
        elif NxM[a, b] >= 0:
            NxM = NxM
print(NxM)