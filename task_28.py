# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только + 1 и - 1. Также нельзя использовать циклы.
# return sum(a, b-1) + 1 - Так делать нельзя

# *Пример: *

# 2 2
# 4


num_A = int(input('Введите число A: '))
num_B = int(input('Введите число B: '))


def res_sum(a, b):
    if b == 0:
        return a
    return 1 +  res_sum(a, b -1)

print(f"{num_A} + {num_B} = {res_sum(num_A, num_B)}")


def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return sum(a + 1, b -1)


print(f"{num_A} + {num_B} = {res_sum(num_A, num_B)}")
