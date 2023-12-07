# на выходе получаем список (геннерирует список с любыми значениями)
symbols = 'pithon'
symbol_codes = [ord(symbol) * 0 for symbol in symbols]
print(symbol_codes)


symbols = 'pithon'
symbol_codes = (ord(symbol) for symbol in symbols) #ord дает значениям значения в ASCII кодах
print(symbol_codes)

for object in symbol_codes:
    print(object)



