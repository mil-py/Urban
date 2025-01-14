import time
import threading
from random import randint
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            sited = False
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    sited = True
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            if not sited:
                self.q.put(guest)
                print(f"{guest.name} в очереди")

    def serve_guests(self):

        while not self.q.empty() or len(list(filter(lambda table: table.guest, self.tables))) > 0:
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    table.guest = None
                    print(f"Стол номер {table.number} свободен")
                    if not self.q.empty():
                        table.guest = self.q.get()
                        print(F"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.serve_guests()
