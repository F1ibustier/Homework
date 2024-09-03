# Try и Except
# coded by f1ibustier

def add_everything_up(a, b):
    try:
        summ = a + b
        return summ
    except TypeError:
        summ = str(a) + str(b)
        print('Складывать данные с разными типами некорректно:')
        return summ

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
