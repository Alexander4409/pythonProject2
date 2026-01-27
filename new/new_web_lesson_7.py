#Лябмбда выражения
#lambda - оператор для определения лямбда выражений
#Формальная запись - 	lambda [параметры] : инструкция

# message = lambda :print("hello")
#
#
# message()
#
# #Эквивалент на def
# def say_hi():
#     print("Hello")
#
#
# say_hi()
#параметры лямбда выражений
# mult = lambda num_1, num_2: num_1*num_2
#
# print(mult(2,3))

#передача лямбда выражений в качестве параметра
# def do_operation(num_1,num_2,operation):
#     res = operation(num_1,num_2)
#     return print(f"результат = {res}")
#
# do_operation(3,4, lambda num_1,num_2: num_1+num_2)
# do_operation(5,2, lambda num_1,num_2: num_1-num_2)

#Возвращения параметров

# def select_operation(choice):
#     if choice == 1:
#         return lambda num_1, num_2: num_1+num_2
#     elif choice == 2:
#         return lambda num_1, num_2: num_1-num_2
#     else:
#         return print(f"Error")
#
# operation = select_operation(1)
# print(operation(3,4))
#
# operation = select_operation(5)
# print(operation(4,5))

#Область видимости переменных
#Глобальный контекст
# name = "John Doe"
#
# def say_hi():
#     print(f"Hi {name}")
#
#
# def say_bye():
#     print(f"Bye {name}")
#
#
# say_hi()
# say_bye()

#Локальный контекст
# def say_hi():
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def say_bye():
#     name = "Tom"
#     print("Good bye", name)
#
#
# say_hi()
# say_bye()

# Скрытие переменных

# name = "John Doe"
#
# def say_hi():
#     name = "Mary Doe" # Скрытие глобального значения
#     print(f"Hi {name}")
#
#
# def say_bye():
#     print(f"Bye {name}")
#
#
# say_hi()
# say_bye()

#global

# name = "John Doe"
#
# def say_hi():
#     global name
#     name = "Mary Doe" # Скрытие глобального значения
#     print(f"Hi {name}")
#
#
# def say_bye():
#     print(f"Bye {name}")
#
# say_hi()
# say_bye()

#nonlocal
### Бибилотека
# import random
#
# while True:
#     random_num = random.randint(1,1000000000000000000000)
#     print(random_num)

# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num = 25
#         print(num)
#
#     inner()
#     print(num)
#
# outer()

# Замыкание

'''Технически замыкание включает три компонента:

1 внешняя функция, которая определяет некоторую область видимости и в которой определены некоторые переменные и параметры - лексическое окружение

2 переменные и параметры (лексическое окружение), которые определены во внешней функции

3 вложенная функция, которая использует переменные и параметры внешней функции'''

def outer():
    num = 1

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner

fn = outer()

fn()
fn()
fn()
fn()
fn()
fn()
fn()

# https://metanit.com/python/tutorial/2.19.php

# ДЗ
# Напишите функцию make_protected_callback(password, callback).
# Она должна возвращать новую функцию, которая запрашивает пароль.
# Если пароль совпадает с заданным при создании, вызывается callback, если нет —
# выводится сообщение об ошибке.
# пример
# def say_hello():
#     print("Доступ разрешен: Привет!")
#
# protected = make_protected_callback("1234", say_hello)
# protected("1111") # "Ошибка: неверный пароль"
# protected("1234") # "Доступ разрешен: Привет!"