# Блокировки и обработка ошибок
# coded by f1ibustier
import threading
import time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            with self.lock:
                deposit = randint(50, 500)
                self.balance += deposit
                print(f'Пополнение: {deposit}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            with self.lock:
                take = randint(50, 500)
                print(f'Запрос на {take}')
                if take <= self.balance:
                    self.balance -= take
                    print(f'Снятие: {take}. Баланс: {self.balance}')
                if take > self.balance:
                    print('Запрос отклонён, недостаточно средств')
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
