# Потоки на классах
# coded by f1ibustier
from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemies):
            days += 1
            enemies -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {days} дней(дня)..., осталось {enemies} воинов.')
            if enemies <= 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')