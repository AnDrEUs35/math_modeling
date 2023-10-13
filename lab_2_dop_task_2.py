AB = int(input('введите АВ: '))
BC = int(input('введите BC: '))
AC = int(input('введите АC: '))

if (AB + BC > AC or AB + AC > BC or BC + AC > AB) and (AB != BC and BC != AC):
    print("треугольник существует")
    print('треугольник разносторонний')
elif AB + BC < AC or AB + AC < BC or BC + AC < AB:
    print('треугольник не существует')
elif (AB == BC and BC != AC)  or (AB == AC and AC != BC) or (BC == AC and AC != AB):
    print("треугольник существует")
    print('треугольник равнобедренный')
elif AB == BC and AB == AC:
    print("треугольник существует")
    print('треугольник равносторонний')




