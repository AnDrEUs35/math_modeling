import numpy as np
N = int(input('введите число:'))
M = int(input('введите число:'))
i = -1
j = -1
A = np.zeros((N, M))


for i in range(N):
    i +=1
    for j in range(M):
        j += 1 
        A[i, j] = np.sin(N * i + M * j)
print(A)











