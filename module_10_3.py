import time
import threading
from random import randint


class Bank:
    def __init__(self, lock, balance):
        self.lock = lock
        self.balance = balance

    def deposit(self):

        for i in range(100):
            cred = randint(50, 500)
            self.balance += cred
            print(f"Пополнение: {cred}. Баланс: {self.balance}")
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            deb = randint(50, 500)
            print(f"Запрос на: {deb}.")
            if self.balance >= deb:
                self.balance -= deb
                print(f"Снятие: {deb}. Баланс: {self.balance}")
                time.sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств.")
                self.lock.acquire()


lock = threading.Lock()
bk = Bank(lock, 0)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
