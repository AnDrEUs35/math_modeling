import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]

plt.plot(x, y, color='g', label='Graf 1', marker='>', ms=5)
plt.plot(y, x, color='r', label='Graf 2', marker='o', ms=3) # ms-размер, 

#--- Украшательства ---

plt.xlabel('coord: x') # подпись координат
plt.ylabel('coord: y')
plt.legend() # вызов легенды (там подписи)
plt.title('Base') # заголовок
plt.grid() # подключение сетки
plt.savefig('fig_2.png')