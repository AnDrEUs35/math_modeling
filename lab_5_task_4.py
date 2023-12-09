import random
list_flowers = ['гладиолус', 'мак', 'роза']
list_colors = ['розовый', 'красный', 'белый', 'оранжевый', 'синий']

list_colors_rand = list(random.choice(list_colors) for i in range(3))
print(list_colors_rand)

dict_zip = dict(zip(list_flowers, list_colors_rand))
print(dict_zip)