chislo = int(input('введите число: '))

for i in range(1000):
    if chislo % 2 == 0 :
        chislo = chislo / 2
        print(2, end='*')
    elif chislo % 3 == 0 :
        chislo = chislo / 3
        print(3, end='*')
    elif chislo % 5 == 0 :
        chislo = chislo / 5
        print(5, end='*')
    elif chislo % 7 == 0 :
        chislo = chislo / 7
        print(7, end='*')
    elif chislo % chislo == 0:
        if chislo == 1:
            chislo * 0
        else:    
            print(chislo)    
        break
