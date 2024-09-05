# Позиционирование в файле
# coded by f1ibustier

def custom_write(file_name, strings):
    strings_position = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            begin_byte = file.tell()
            file.write(f'{string}\n')
            strings_position[(i, begin_byte)] = string
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
