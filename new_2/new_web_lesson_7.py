#Lambda функции

# message = lambda:print("Hello")
#
# message()


#эквивалент def

# def say_hi():
#     return print("Hello")
#
# say_hi()

# power = lambda num,pow: num**pow
#
# print(power(3,4))
# print(power(5,2))

#передача ламбда функции в качестве параметра
# def do_operation (num_1,num_2, operation):
#     res = operation(num_1,num_2)
#     return print(res)
#
# do_operation(54, 55, lambda num_1,num_2: num_1+num_2)
# do_operation(54, 55, lambda num_1,num_2: num_1-num_2)
# do_operation(54, 55, lambda num_1,num_2: num_1*num_2)

#Возвращение лямбда выражений из функции
# def select_operation(choice):
#     if choice == 1:
#         return lambda num_1,num_2: num_1+num_2
#     elif choice == 2:
#         return lambda num_1, num_2: num_1 - num_2
#     else:
#         return print("Неверная операция")
#
# operation = select_operation(1)
# print(operation(10,4))
#
# operation = select_operation(4)
# print(operation(3,4))

# генератор рандомных чисел
# import random
#
# random_int = random.randint(1,10)
# print(random_int)

#Локальные и глобальные переменные и их скрытие
# name = "Bob"
#
# def say_hi():
#     name = "Tom" # Скрытие значения глобальной переменной
#     print("Hello ", name)
#
# def say_by():
#     print("By ", name)
#
#
# say_hi()
# say_by()

#Global
# name = "Mary"
#
#
# def say_hi():
#     global name
#     name = "Tom" # Скрытие значения глобальной переменной
#     print("Hello ", name)
#
# def say_by():
#     print("By ", name)
#
#
#
# say_hi()
# say_by()


#Nonlocal

# def out():
#     num = 1
#
#     def inner():
#         nonlocal num
#         num = 25
#         print(num)
#
#     inner()
#     print(num)
#
# out()

#Замыкания
def out():
    num = 0
    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


fn = out()

fn()
fn()
fn()
fn()
fn()
fn()

'''1 внешняя функция, которая определяет некоторую область видимости и в которой определены 
некоторые переменные и параметры - лексическое окружение

2 переменные и параметры (лексическое окружение), которые определены во внешней функции

3 вложенная функция, которая использует переменные и параметры внешней функции'''
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


#Решение
# def protected_callback():
#
#     actually_password = input("Установите пароль: ")
#
#     def check_password():
#         password_input = input("Введите пароль для входа: ")
#         if password_input == actually_password:
#             return "Доступ разрешен: Привет!"
#         return "Ошибка: неверный пароль"
#
#     return check_password
#
# verify = protected_callback()
#
# while True:
#     result = verify()
#     print(result)
#     if "Доступ разрешен" in result:
#         break


