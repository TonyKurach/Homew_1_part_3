
import random

# все четные по значению элементы исходного списка А поместить в новый список
A = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9),
     random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9),
     random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9),
     random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
print("Исходный список А:", A)
print("Длина списка А:", len(A), "элементов")
B = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i])
print("Новый список B с четными по значению элементами списка А", B)
print("Длина списка B:", len(B), "элементов")


