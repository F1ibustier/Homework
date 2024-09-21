# Создание потоков
# coded by f1ibustier
import time
from time import sleep
from datetime import datetime
from threading import Thread



def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(20, 'example3.txt')
write_words(1, 'example4.txt')

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)

time_start2 = datetime.now()

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words(word_count=30, file_name='example6.txt'))
thr_3 = Thread(target=write_words(word_count=20, file_name='example7.txt'))
thr_4 = Thread(target=write_words(word_count=1, file_name='example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)
