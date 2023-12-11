import random

def func(n, list0):
    while True:
        rand_num = random.randint(0, n)
        for i in list0:
            if rand_num == i:
                break
            elif rand_num != i and i == list0[-1]:
                return rand_num 
            
print(func(10, [3, 9, 1, 5]))        
