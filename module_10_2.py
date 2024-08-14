# Домашнее задание по теме "Потоки на классах".
# Цель: научиться создавать классы наследованные от класса Thread.

import time
from time import sleep
from datetime import datetime
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0  # Добавляем счетчик дней

    def run(self):
        for i in range(100, 0, -self.power):
            count_war = i - self.power  # Количество оставшихся врагов
            time.sleep(1)
            self.days += 1
            print(f'{self.name} сражается {self.days} день(дня)..., осталось {count_war} воинов.\n')
            if count_war <= 0:
                print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


# Создание объекта класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
print(f'{first_knight.name}, на нас напали!')
print(f'{second_knight.name}, на нас напали!')
first_knight.join()
second_knight.join()
# print(f'{first_knight.name} одержал победу спустя {first_knight.days} дней(дня)!')
# print(f'{second_knight.name} одержал победу спустя {second_knight.days} дней(дня)!')
# Вывод строки об окончании сражения
print('Все битвы закончились!')
