#Списки
#str,  int, float, bool(True/False)
# name = "Tom"
# name1 = "Bob"
# name2 = "Jef"
#...
# Удобное хранение нескольких элементов в одном месте (переменной)
# name_list =  ["Tom", "Bob", "Jef", 'Mary']
# list_of_objects = [1,2,0.4,"str",True,[1,2,3,"dfdf"]]
# print(list_of_objects)
# message = 11,23,2,32,3,24,4,23
# print(list(message))
# name_list.append("Jessy")
# name_list.remove("Bob")
# print(name_list)
# Задача написать программу которая позволит пользователю вносить столько имен в список сколько он хочет
# users_list = []
#
# while True:
#     users_input = input("Enter the name of user")
#     if users_input == "stop":
#         print(users_list)
#         break
#     else:
#         users_list.append(users_input)
#         print(users_list)

# напишите калькулятор, который умеет складывать и вычитать в зависимости от выбора
# пользователя два числа, используйте def при помощи цикла и списков сохраните
# результаты в список

# results = []  # Список для хранения истории результатов
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# while True:
#     print("\n--- Калькулятор ---")
#     print("1. Сложение")
#     print("2. Вычитание")
#     print("3. Показать историю")
#     print("0. Выход")
#
#     choice = input("Выберите действие: ")
#
#     if choice == "0":
#         print("Завершение работы.")
#         break
#
#     if choice == "3":
#         print(f"История результатов: {results}")
#         continue
#
#     if choice in ("1", "2"):
#         # Ввод чисел
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
#
#         if choice == "1":
#             res = add(num1, num2)
#             print(f"Результат: {res}")
#             results.append(res)  # Сохраняем в список
#
#         elif choice == "2":
#             res = subtract(num1, num2)
#             print(f"Результат: {res}")
#             results.append(res)  # Сохраняем в список
#     else:
#         print("Неверный ввод, попробуйте снова.")

#перебор элементов списка
# for
# name_list =  ["Tom", "Bob", "Jef", 'Mary']
# for person in name_list:
#     print(person)
#while
# name_list =  ["Tom", "Bob", "Jef", 'Mary']
#
# user_index = 0
# while user_index < len(name_list):
#     print(name_list[user_index])
#     user_index += 1

'''
append(item): добавляет элемент item в конец списка

insert(index, item): добавляет элемент item в список по индексу index

extend(items): добавляет набор элементов items в конец списка

remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

clear(): удаление всех элементов из списка

index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

count(item): возвращает количество вхождений элемента item в список

sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

reverse(): расставляет все элементы в списке в обратном порядке

copy(): копирует список
'''
# Библиотека
# 1 Пользователь вносит книги в библиотеку append
# 2 пользователь может удалить конкретную книгу по её индексу pop
# 3 пользователь может удалить все книги clear
# 4 пользователь может узнать сколько всего книг в библиотеке len
