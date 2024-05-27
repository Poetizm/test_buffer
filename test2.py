import datetime

class Buffer:
  ''' Плюсы: 1. Легкочитаем; 2. Не имеет сторонних библиотек; 3. Выполняет основную задачу
      Минусы: 1. Громоздко; 2. Плохая производительность с большим объёмом данных; 3. Нет обработки ошибок
  '''
  def __init__(self, size): 
      self.buffer = list()
      self.size = size 
 
  def add_value(self, value): 
    # Новое значения вставляется в конец буфера и удаляется первый элемент из начала буфера 
    if len(self.buffer) < self.size:
        self.buffer.append(value)
    else:
       self.buffer.append(value)
       self.buffer.pop(0)

start1 = datetime.datetime.now()
print('Время старта: ' + str(start1))
buf = Buffer(500)
p = 0
while  p < 100000:
    buf.add_value(p)
    p+=1
finish1 = datetime.datetime.now()
print('Время окончания: ' + str(finish1))
print(f'Время выполнения: {finish1-start1}') 

print('-' * 30)

class Buffer_2:
    ''' Плюсы: 1. Легкочитаем; 2. Не имеет сторонних библиотек; 3. Выполняет основную задачу
        Минусы: 1. Громоздко; 2. Худшая производительность с большим объёмом данных; 3. Нет обработки ошибок
    '''
    def __init__(self, size):
        self.buffer = list()
        self.size = size

    def add_value(self, value):
        # Новое значение становится первым элементом в буфере и удаляется самый старый элемент из конца буфера
        if len(self.buffer) < self.size:
            self.buffer.insert(0, value)
        else:
            self.buffer.insert(0, value)
            self.buffer.pop()

start2 = datetime.datetime.now()
print('Время старта: ' + str(start2))
buf_2 = Buffer_2(500)
p = 0
while  p < 100000:
    buf_2.add_value(p)
    p+=1
finish2 = datetime.datetime.now()
print('Время окончания: ' + str(finish2))
print(f'Время выполнения: {finish2-start2}')
      
print('-' * 30)

from collections import deque

class Buffer_3:
    ''' Плюсы: 1. Простота; 2. Имеет обработку ошибки при заданном размере <= 0. 3. Самая лучшая производительность; Имеет дополнительные методы буфера
        Минусы: 1. Импорт библиотеки 
    ''' 
    def __init__(self, size):
        if size <=0:
            raise ValueError('Размер должен быть положительным')        
        self.buffer = deque(maxlen=size)

    def add_value(self, value):
        self.buffer.append(value)

    def get_buffer(self):
        return list(self.buffer)
    
    def empty_buffer(self):
        return len(self.buffer) == 0
    
    def clear_buffer(self):
        self.buffer.clear()
    
start3 = datetime.datetime.now()
print('Время старта: ' + str(start3))
buf_3 = Buffer_3(500)
p = 0
while  p < 100000:
    buf_3.add_value(p)
    p+=1
finish3 = datetime.datetime.now()
print('Время окончания: ' + str(finish3))
print(f'Время выполнения: {finish3-start3}')
