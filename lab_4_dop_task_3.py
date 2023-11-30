linza = input('Какая линза?: ')
pr_lin = int(input('Введите расстояние от предмета до линзы: ')) 
focus = int(input('фокусное расстояние:'))

def func(linza):
    if linza == 'собирающая':
            if pr_lin > focus:
                if pr_lin < focus * 2:
                    picture = 'действительное, увеличенное, перевернутое'
                elif pr_lin > focus * 2:
                    picture = 'действительное, уменьшенное, перевернутое'
                elif pr_lin == focus * 2:
                    picture = 'действительное, реального размера, перевернутое'
            elif pr_lin < focus:
                picture = 'мнимое, увеличенное, прямое' 
            elif pr_lin == focus:
                picture = 'действительное, увеличенное, перевернутое'

    elif linza == 'рассеивающая':
        if pr_lin > focus:
            if pr_lin < focus * 2:
                picture = 'мнимое, прямое, уменьшенное'
            elif pr_lin > focus * 2:
                picture = 'мнимое, прямое, уменьшенное'
            elif pr_lin == focus * 2:
                    picture = 'мнимое, уменьшенное, прямое'
        elif pr_lin < focus:
            picture = 'мнимое, уменьшенное, прямое'    
        elif pr_lin == focus:
                picture = 'мнимое, уменьшенное, прямое'
    return picture

picture = func(linza)
print(picture)
