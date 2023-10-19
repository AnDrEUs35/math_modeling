god = int(input('введите год'))

if (god % 4 == 0 and god % 100 != 0) or (god % 100 != 0 and god % 400 == 0):
    print('високосный')
else:
    print('невисокосный')



