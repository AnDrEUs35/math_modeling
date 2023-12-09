name = 'Андрей Кокорин'

name_ = '_'.join(name)
print(name_)

NAME = name_.upper()
print(NAME)

NAME_ord = (ord(symbol) for symbol in NAME)

list1 = []
for object in NAME_ord:
    list1.append(object)
print(list1)

name_low = name_.lower()
print(name_low)

name_low_ord = (ord(symbol) for symbol in name_low)

list2 = []
for object in name_low_ord:
    list2.append(object)
print(list2)

print(max(list1))
print(max(list2))

