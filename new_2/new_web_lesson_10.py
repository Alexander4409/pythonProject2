#Списки - list
# list - функция преврощяет какую либо последовательность в список
# ! не удобно
# name = "John"
# name1 = "Mike"
# ...
# Список = Удобное хранение нескольких данных в одной переменной
# names = ['John', 'Mike']
# print(names)
# user_name = input("Enter new user name")
# names.append(user_name)
# print(names)
# while True:
#     user_name = input("Enter new user name")
#     if user_name == "stop":
#         print(names, "Bye bye")
#         break
#     names.append(user_name)
#     print(names)

# напишите калькулятор, который умеет складывать и вычитать в зависимости от выбора
# пользователя два числа, используйте def при помощи цикла и списков сохраните
# результаты в список

# results = []
#
#
# def manager(user_choice,num1,num2):
#     if user_choice == 1:
#         results.append(summ(num1,num2))
#
#     elif user_choice == 2:
#         results.append(substract(num1,num2))
#
#
#
# def summ(num1,num2):
#     res = num1 + num2
#     return res
#
# def substract(num1,num2):
#     res1 = num1 - num2
#     return res1
#
#
#
# user_choice = int(input())
# num1 = int(input())
# num2 = int(input())
#
# manager(user_choice, num1, num2)

# lst= [True,0.2,3,"gfgfgf",[1,2,3]]
# список может хранить все типы данных
# letters = list("Hello")
# print(letters)
# обращение к индексам
# names = ['John', 'Mike', 'Tom']
# print(names[1])
#
# print(names[-1])
# перебор элементов списка/
# for
# people = ["Tom","Jeff", "Bob"]
# for index, person in enumerate(people):
#     print(f'Index : {index}, Name: {person}')
# while
# people = ["Tom","Jeff", "Bob"]
# i = 0
#
# while i < len(people):
#     person = people[i]
#     print(f'Index: {i}, Name: {person}')
#     i += 1

# Методы списков
# append(item): добавляет элемент item в конец списка
#
# insert(index, item): добавляет элемент item в список по индексу index
#
# extend(items): добавляет набор элементов items в конец списка
#
# remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
#
# clear(): удаление всех элементов из списка
#
# index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
#
# pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
#
# count(item): возвращает количество вхождений элемента item в список
#
# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
#
# reverse(): расставляет все элементы в списке в обратном порядке
#
# copy(): копирует список

# Библиотека
# 1 Пользователь вносит книги в библиотеку
# 2 пользователь может удалить конкретную книгу по её индексу
# 3 пользователь может удалить все книги
# 4 пользователь может узнать сколько всего книг в библиотеке
# Доделать
books = []


def add_book(user_input):
    return books.append(user_input)


def del_book(user_index_input):
    return books.pop(user_index_input)



while True:

    user_choice = int(input("Enter your choice"))


    if user_choice == 1:
        user_input = input('Enter book name')
        add_book(user_input)

    elif user_choice == 2:
        user_index_input = input('Enter book index for del')
        del_book(user_index_input)

    elif user_choice == 3:
        print(books)







