import time
import datetime
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'w') as out_f:
        for i in range(word_count):
            out_f.write("Какое-то слово № " + str(i))
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}.")


start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
finish_time = time.time()
print("время выполнения в одном потоке = ", str(datetime.timedelta(seconds=finish_time - start_time)))

threads = [threading.Thread(target=wite_words, args=(10, 'example5.txt')),
           threading.Thread(target=wite_words, args=(30, 'example6.txt')),
           threading.Thread(target=wite_words, args=(200, 'example7.txt')),
           threading.Thread(target=wite_words, args=(100, 'example8.txt'))]

start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

finish_time = time.time()

print("время выполнения потоков = ", str(datetime.timedelta(seconds=finish_time - start_time)))
