# Введение в функциональное программирование
# coded by f1ibustier

def minimum(int_list):    #принимает список, возвращает минимальное значение из него.
    return min(int_list)


def maximum(int_list):    #принимает список, возвращает максимальное значение из него.
    return max(int_list)


def lenght(int_list):    #принимает список, возвращает кол-во элементов в нём.
    return len(int_list)


def summa(int_list):    #принимает список, возвращает сумму его элементов.
    return sum(int_list)


def sortirovka(int_list):    #принимает список, возвращает новый отсортированный список на основе переданного.
    return sorted(int_list)


functions = [minimum, maximum, lenght, summa, sortirovka]


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
