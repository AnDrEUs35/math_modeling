n = int(input('введите число: '))
n = n + 1
for sov_ch in range(n):

    if sov_ch % 2 == 0 :
        sov_ch = sov_ch / 2
        print(2, end='')
    elif sov_ch % 3 == 0 :
        sov_ch = sov_ch / 3
        print(3, end='*')
    elif sov_ch % 5 == 0 :
        sov_ch = sov_ch / 5
        print(5, end='*')
    elif sov_ch % 7 == 0 :
        sov_ch = sov_ch / 7
        print(7, end='*')
    elif sov_ch % sov_ch == 0:
        if sov_ch == 1:
            sov_ch * 0
        else:    
            print(sov_ch)    
        break

    print(sov_ch)