# Распаковка позиционных параметров
# coded by f1ibustier

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = (56.3, 'top', False)
values_dict = {'a': 21, 'b': 'try', 'c': 12.5}
values_list_2 = (-5.8, 'pot')

print_params(5, 6)
print_params(c=6)
print_params()
print_params(b=25, c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
