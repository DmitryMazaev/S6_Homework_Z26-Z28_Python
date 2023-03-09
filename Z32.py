# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Введите размер списка: "))
a = int(input("Введите заданный минимум: "))
b = int(input("Введите заданный максимум: "))
import random


def List():
    List_1 = []
    for i in range(n):
        List_1.append(random.randint(1, 20))
    print(List_1)
    List_2 = []
    for i in range(n):
        if List_1[i] >= a and List_1[i] <= b:
            List_2.append(i)
        else:
            List_2.append("-")
    print(List_2)
List()
