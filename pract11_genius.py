from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, encoding='UTF-8') as f:
        while True:
            content = f.readline()
            if not content:
                break
            all_data += [content]


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

if __name__ == '__main__':
    start = datetime.now()
    # последовательный запуск:

    # for f in files:
    #     read_info(f)

    # запуск 4 процессов параллельно:

    with Pool(processes=4) as pool:
        pool.map(read_info, files)

    end = datetime.now()
    print('время', end - start)