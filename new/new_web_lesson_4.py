#Циклы
#while
#Проверяет истинность условия и пока это выражение нам возвращает True то цикл работает
#while устолвное_выражение:
#   инструкция
# num = 1
# while True:
#     print(f'число - {num}')
#     if num == 4:
#         print("Мы почти у цели")
#     num *= 1
# print("конец программы")
# число - 1 - итерация
# число - 2
# число - 3
# число - 4
# число - 5
# конец программы
#https://keyboard-type-simulator.vercel.app/learn - клавиатурный тренажер
from pyexpat.errors import messages

#break - завершает цикл
# num = 1
# while True:
#     print(f'число - {num}')
#     if num == 4:
#         print("Мы почти у цели")
#     elif num == 100:
#         print(f'Число = {num}')
#         # break
#     num += 1


#continue - пропускает итерацию

# number = 0
# while number < 5:
#     number += 1
#     if number == 3 :    # если number = 3, переходим к новой итерации цикла
#         continue
#     print(f"number = {number}")

#вложенный цикл while
# цикл вывода таблицы умножения
# i = 1 # столбцы
# j = 1 # ряды
# while i < 10:
#     while j < 10:
#         print(i*j, end='\t' )
#         j += 1
#     print('\n')
#     j = 1
#     i += 1
#for
# message = "Hello"
#
# for c in message:
#     print(c)
#" условно бесконечный цикл for"
# for i in range(999999999999999999999999999999999999999999999999999999999999999):
#     i += 1
#     print(i)
# вложенный цикл for

#
# for i in "as":
#     for j in "sa":
#         print(f'{i}{j}')

# n = 7
# for i in range(0,n):
#     for j in range(0,n):
#         if(i == 0 or i == n-1 or j == i or j == n-i-1):print('*',end='')
#         else:print(" ",end="")
#     print()
# дз - составить код который выводит сердечко (Используйте циклы, чтобы вывести на консоль эту фигуру)
#  **   **
# **** ****
# *********
#  *******
#   *****
#    ***
#     *


