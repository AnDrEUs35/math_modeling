a = float(input('Введите число: '))
n = int(input('Введите число: '))

def stepen(a, n):
    n += 1
    b = 0
    for i in range(1, n):
        if b == 0:
            b = a
        else:
            b = a * b
    return b

b = stepen(a, n)
print(b)