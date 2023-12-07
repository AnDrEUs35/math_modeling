name = 'Андрей Кокорин'

name_ = '_'.join(name)
print(name_)

NAME = name_.upper()
print(NAME)

NAME_ord = (ord(symbol) for symbol in name)

mass = []
for object in NAME_ord:
    mass.append(object)
print(mass)

name_nsh = NAME.lower()
print(name_nsh)
