
print('... x**2 + ...x - ... = 0')
print('Введите коэффициенты для квадратного ур-я.')


a = int(input('введите коэффициент а:'))
b = int(input('введите коэффициент b:'))
c = int(input('введите коэффициент c:'))

print(f'{a}* x ** 2 + {b} * x - {c} = 0')

D = b ** 2 - 4 * a * c
print(D)

if D > 0:
    print('2 корня')
    x1 = (-b + D ** 0.5) / 2 * a
    x2 = (-b - D ** 0.5) / 2 * a
    print(x1)
    print(x2)
elif D == 0:
    print('1 корень')
    x1 = (-b + D ** 0.5) / 2 * a
    print(x1)
elif D < 0:
    print('нет корней')





