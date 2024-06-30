#Неизменяемые и изменяемые объекты. Кортежи и списки
#coded by f1ibustier

immutable_var = (1, 2, 'name', True)   #это кортеж
#immutable_var[3] = False (выдает ошибку в связи с тем, что кортеж не поддерживает изменения)
print(immutable_var)
mutable_list = [1, 2, 'name', True]  #это список
mutable_list[1] = 5
print(mutable_list)
