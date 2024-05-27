import random
import datetime

class Buffer:
    def __init__(self, size): 
        self.buffer = list()
        self.size = size

    def add_value(self, value):
        self.buffer.append(value)

size = 100000

buf = Buffer(size)

while len(buf.buffer) < size:
    buf.add_value(random.randint(0,1000))

start1 = datetime.datetime.now()
print('Время старта: ' + str(start1))
buf.buffer.sort()
finish1 = datetime.datetime.now()
print('Время окончания: ' + str(finish1))
print(f'Время выполнения: {finish1-start1}') 

print('-'*30)

start2 = datetime.datetime.now()
print('Время старта: ' + str(start2))
sorted_buf = sorted(buf.buffer)
finish2 = datetime.datetime.now()
print('Время окончания: ' + str(finish2))
print(f'Время выполнения: {finish2-start2}') 


# Наиболее эффективным алгоритмом сортировки массивов является Timsort. 
# Timsort сначала анализирует список, который он пытается отсортировать, и на его основе выбирает наилучший подход.
# Исходя из тестов, проведенных выше, рандомный массив чисел отсортируется эффективнее функцией sorted()