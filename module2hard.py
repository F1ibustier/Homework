#Основные операторы
# coded by f1ibustier

import random
vstavka_1 = random.randint(3, 21)
print(vstavka_1)
parol = ""
for vstavka_2_1 in range(1, vstavka_1+1):
    for vstavka_2_2 in range(vstavka_2_1+1, vstavka_1+1):
        if vstavka_1 % (vstavka_2_1 + vstavka_2_2) == 0:
            parol += str(vstavka_2_1) + str(vstavka_2_2)
print(parol)