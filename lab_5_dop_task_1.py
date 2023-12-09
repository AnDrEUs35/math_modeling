import time

def umnozhator(a):
    a = a ** 3
    return a


timer = time.time()
list_for = []
for i in range(0, 10 ** 5 + 1):
    list_for.append(umnozhator(i))
print(list_for)

timer1 = time.time() - timer


timer = time.time()
list_listcomp = [umnozhator(x) for x in range(0, 10 ** 5 + 1)]
print(list_listcomp)

timer2 = time.time() - timer


timer = time.time()
list0 = [y for y in range(10 ** 5 + 1)]
list_map = list(map(umnozhator, list0))
print(list_map)

timer3 = time.time() - timer

print(timer1)
print(timer2)
print(timer3)