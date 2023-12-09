import numpy as np
import time

N = 5
M = 5


timer = time.time()
for y in range(0, M):
    time.sleep(1)
    print(y)
    for x in range(0, N):
       time.sleep(1)
       print(x)
       
print(timer)