def changer(a, b):
    a = 2
    b[0] = 'Good'

X = 10
L =[1, 2]

changer(X, L) # вызов функции для  X, L

print(X)
print(L)

L = [1, 2]
changer(X, L[:])

print(L)

# complex numbers
x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)
print(z + w)

#strings

s = 'hello'
print(s[0])

#s[0] = 'H' cтроки изменять нельзя
#print(s)

# Tuple
t = (1, 4, 9)
print(t)

print(t[0])
#t[0] = 6 кортежи изменять нельзя

#list
l = [1, 4, 9]
l[0] = 1000 # списки изменять можно
print(l)

#Dict
d = {'al':4, 4:'al', 'str':'Hello'} # al, str - ключи
print(d['al']) # можно вызывать ключами
print(d[4])
print(d['str'])

d['str'] = 'Good'
print(d)

