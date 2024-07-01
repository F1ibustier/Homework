#Словари и множества
#coded by f1bustier

#словари
my_dict = {'Viktor': 1984, 'Alex': 1988, 'Anna': 1985}
print(my_dict)
print(my_dict['Viktor'])
#print(my_dict['Sasha']) ошибка
print(my_dict.get('Sasha', 'Данное имя отсутствует в Вашем словаре'))
my_dict.update({'Ivan': 1980, 'Oleg': 1975}) #добавление в словарь
print(my_dict.pop('Anna')) #вытаскивает из словаря
print(my_dict)

#множества
my_set = {1975, 1985, 1975, 'Ivan', 'Ivan', 'Oleg', (1, 2, 3)}
print(my_set)
my_set.add(56.78, 12)
my_set.add(123)
my_set.discard('Oleg')
print(my_set)
