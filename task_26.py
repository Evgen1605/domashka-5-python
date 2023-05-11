# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

num_A = int(input('Введите число A: '))
num_B= int(input('Введите число B: '))


def Exponentiation(a, b):
    if b == 0:
        return 1
    return a * Exponentiation(a, b -1)

print(f"{num_A} в степени {num_B} = {Exponentiation(num_A, num_B)}") 
