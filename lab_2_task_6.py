a = 0
b = 0

for i in range(1, 10):
    a += 1
    for i in range(1, 10):
        b += 1
        c = a * b
        print(c)

