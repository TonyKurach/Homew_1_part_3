import random

# Удалить элемент с введенным номером a

# создадим лист А из 5 элементов
A = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
     random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
     random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
     random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
print("Изначальный лист А:")
print(A)
# создадим переменную, которая принимает значения от 1 до 5 - по количеству элементов листа А
a = random.randint(0, 15)
print("Удаляем из листа А элемент под номером:")
print(a)
# удалим из листа А элемент под номером а
A.pop(a)
# новый лист А
print("Измененный лист А:")
print(A)
