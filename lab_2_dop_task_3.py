chislo = int(input('введите число: '))
if chislo < 0:
    chislo = chislo * (-1)

for i in range(1, chislo):
    if chislo > 9 or chislo < (-9):
        chislo_p = chislo % 10 
        print(chislo_p, end='')
        chislo = chislo // 10
    else:
        print(chislo, end=' ')
        break


