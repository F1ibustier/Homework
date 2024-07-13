#Пространство имён
# coded by f1ibustier

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list):
    count_calls()
    if string.lower() in map(str.lower, list_to_search):
        return True
    else:
        return False


print(string_info('Benetton'))
print(string_info('Abrakadabra'))
print(string_info('Samurai'))
print(is_contains('Город', ['гоРОД', 'Городской', 'гора', 'Горад']))
print(is_contains('Велосипед', ['Велосипедист', 'Велоспорт']))
print(calls)
