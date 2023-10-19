n = int(input('введите кол-во чисел ряда фибоначчи: '))
fib1 = 1
fib2 = 1
for i in range(n):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print(fib1)
