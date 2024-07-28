import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write('Какое-то слово № %d\n' % (i + 1))
            time.sleep(0.1)
    print("Завершилась запись в файл %s." % file_name)

# Вызовы функций без потоков
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Измерение времени выполнения функций
start_time = time.time()

# Вызовы функций в потоках
filenames = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]
threads = []
for count, filename in filenames:
    t = Thread(target=write_words, args=(count, filename))
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

end_time = time.time()
print("Работа потоков %s." % str(end_time - start_time))
