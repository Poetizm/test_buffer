import datetime

def isEven(value):
      ''' Плюсы: 1. Простота
          Минусы: 2. Нет проверки на тип аргумента 
      '''
      return value % 2 == 0

def isEven2(value):
      ''' Плюсы: 1. Есть проверка на тип аргумента
          Минусы: 2. Громоздко
      '''
      if isinstance(value,(int,float)):
            return type(value // 2) ==  int


start1 = datetime.datetime.now()
print('Время старта: ' + str(start1))
print(isEven(2))
finish1 = datetime.datetime.now()
print('Время окончания: ' + str(finish1))
print(f'Время выполнения: {finish1-start1}') 

print('-'* 20)
start2 = datetime.datetime.now()
print('Время старта: ' + str(start2))
print(isEven2(2))
finish2 = datetime.datetime.now()
print('Время окончания: ' + str(finish2))
print(f'Время выполнения: {finish2-start2}') 
