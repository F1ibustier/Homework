# Генераторы
# coded by f1ibustier

# def all_variants(text):
#     for i in range(len(text)):
#         for j in range(len(text)-i):
#             yield text[j:j+i+1]


def all_variants(text):
    from itertools import combinations
    for i in range(1, len(text)+1):
        for comb in combinations(text, i):
            yield ''.join(comb)


a = all_variants("abc")
for i in a:
    print(i)
