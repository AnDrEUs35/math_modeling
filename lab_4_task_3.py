from constants import svobodnoe_padenie as g
h = float(input('Введите высоту: '))
V = float(input('Введите скорость: '))
m = float(input('Введите массу: '))

# x - скорость
# y - высота
# z - масса
# u - ускорение

def energia(x, y, z, u):
    E_pt = z * u * y
    E = E_pt
    return E
mass = energia(V, h, m, g)
print(mass)

