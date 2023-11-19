n = int(input('Введите число: '))

def fibonachi(n):
    if n > 0:
        fib1 = -1
        fib2 = 1
        for i in range(n):
            fib = fib2 + fib1
            fib1 = fib2
            fib2 = fib
        print(fib)
    elif n < 0:
        n = n * -1
        fib1 = 1
        fib2 = 1
        for i in range(n):
            fib = fib1 - fib2
            fib1 = fib2
            fib2 = fib
        print(fib)

            

fibonachi(n)