# Многопроцессное программирование
# coded by f1ibustier
from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


file_names = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
start = datetime.now()
for file_name in file_names:
    read_info(file_name)
end = datetime.now()
print('Длительность выполнения программы при линейном вызове функции', end - start)

# Многопроцессный вызов
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end = datetime.now()
    print('Длительность выполнения программы при многопроцессном вызове функции', end - start)
