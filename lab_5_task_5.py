FIO = 'Кокорин Андрей'

list1 = [i.upper() for i in FIO]
list2 = [i.lower() for i in FIO]
print(list1)
print(list2)

list1_ord = list(ord(i) for i in list1)
list2_ord = list(ord(i) for i in list2)
print(list1_ord)
print(list2_ord)