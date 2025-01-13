import time
import threading


class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}! на нас напали!")
        n = 100
        d = 0
        while n > 0:
            time.sleep(1)
            n -= self.power
            d += 1
            print(f"{self.name} сражается {d} дней(дня)..., осталось {n} воинов.")
        print(f"{self.name} одержал победу спустя {d} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
