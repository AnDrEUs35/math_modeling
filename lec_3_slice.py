import numpy as np
a = [4, 16, 10, 5, 7, 1, 8]

slice = a[2: 5: 1] # вырезает из списка / массива какие-то значения 
print(slice)

a = [1, 5, 3, 6]

slice = a[0:2:1] # имя можно любое
print(slice)

slice = a[3:0:-1] # идти в обратном порядке списка
print(slice)

slice = a[ : :-1] # в обратном порядке в самое начало
print(slice)

b = np.array([a, np.array(a) * 3])
print(b)

slice = b[::] # вырезать все
print(slice)

slice = b[::, 1] # взять все значения со столбца
print(slice)

slice = b[1,2::1]
print(slice)





