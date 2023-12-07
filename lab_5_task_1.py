import numpy as np
N = 10
mass1 = np.random.randint(0, 100, N)
mass2 = np.random.randint(0, 100, N)
mass3 = np.random.randint(0, 100, N)
print(mass1)
print(mass2)
print(mass3)

print(max(mass1))
print(max(mass2))
print(max(mass3))

sum1 = sum(mass1)
sum2 = sum(mass2)
sum3 = sum(mass3)

print('суммы:', sum1, sum2, sum3)

sum = sum1 + sum2 + sum3
print(sum)