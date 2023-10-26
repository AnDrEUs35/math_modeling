n = int(input('введите число: '))
n = n + 1
x = 0
for i in range(n):
    x += 1
    x1 = 0
    x2 = 0
    for i in range(n):

        x2 = x1 * x2
        if x % 2 == 0:
            x1 = 2
            
        elif x % 3 == 0:
            x1 =3
        
        elif x % 4 == 0:
            x1 = 4
            
        elif x % 7 == 0:
            x1 = 7
               

    print(x2)
    

