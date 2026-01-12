#Циклы
#while
#цикл проверяет истинность некоторого выражения и если условие возвращает True то цикл запускается
#while условное_выражение(True):
    #инструкция

# num = 0
# while num <20:
#     print(f'число = {num}')
#     num += 1
# print("Работа программы завершена")
# итерация это единичное выполнение блока с инструкцией

# num = 0
# while True:
#     print(f'число = {num}')
#     num += 1
#     if num == 10:
#         print("цикл скоро завершиться")
#     elif num == 17:
#         print("мы почти у цели")
# else:
#     print(f'число = {num}. Работа цикла завершена')
# print("Работа программы завершена")
#операторы для управление циклом
# break - выход из цикла
# num = 0
# while num < 20:
#     print(f'число = {num}')
#     num += 1
#     if num == 17:
#         print(f' мы достигли числа {num}')
#         break
# print("Работа программы завершена")
# continue - пропускает текущую итерацию и продолжает цикл со следующей итерацией
# number = 0
# while number < 5:
#     number += 1
#     if number == 3 :    # если number = 3, переходим к новой итерации цикла
#         continue
#     print(f"number = {number}")

#предусмотрите выход из программы
# while True:
#     num_1 = int(input("Enter first number"))
#     num_2 = int(input("Enter second number"))
#
#     print(f'Summ of numbers = {num_1+num_2}')
#
#     exit_from_prog = input("Enter X to exit from program")
#     if exit_from_prog == "X":
#         break

# i = 1
# j = 1
# while i < 10:
#     while j <10:
#         print(i * j, end= "\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1


#for
#Этот цикл пробегается по набору значений,
# помещает каждое значение в переменную, и затем в цикле мы можем с
# этой переменной производить различные действия.
# for i in range(2,20):
#     print(i*2)

# message = "Hello"
#
# for c in message:
#     print(c)

# for c1 in  "ab":
#     for c2 in "ba":
#         print(f"{c1}{c2}")

#Самостоятельно разобраться с алгоритмом
# n = 7
# for i in range(0, n):
#     for j in range(0, n):
#         if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
#         else: print(" ", end="")
#     print()

#ДЗ составить алгоритм для вывода этой фигуры в консоль при помощи циклов
#  **   **
# **** ****
# *********
#  *******
#   *****
#    ***
#     *

h = 7
w = h + 2
m = w //4
for i in range(1, h+1):
    if (i <= m):
        print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
    else:
      print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))
