# lambda (параметры) : инструкция - https://metanit.com/python/tutorial/2.18.php
from random import choice


# def message():
#     print("hello")
#
# #анонимная функция
# message_1 = lambda: print("hello")
#
# message_1()
# message()

#передача лямбда выражения в функцию в качестве параметра
# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# do_operation(5, 4, lambda a, b: a + b)  # result = 9
# do_operation(5, 4, lambda a, b: a * b)  # result = 20

#возвращение лямбда выражение в качестве результата работы функции
# def select_opt(user_choice):
#     if user_choice == 1:
#         return lambda num_1, num_2: num_1*num_2
#     elif user_choice == 2:
#         return lambda num_1, num_2: num_1+num_2
#
#
# operation = select_opt(1)
# print(operation(2,3))
#
# operation = select_opt(2)
# print(operation(2,3))

#область видимости переменных - https://metanit.com/python/tutorial/2.9.php
#Глобальный контекст

# name = "Sara"
#
# def say_hi():
#     print(f'Hello {name}')
#
# def say_bye():
#     print(f'Bye {name}')
#
#
# say_hi()
# say_bye()

#Локальный контекст


# def say_hi():
#     name_1 = "Sara"
#     print(f'Hello {name_1}')
#
# def say_bye():
#     name = "Sara"
#     sur_name = "Konnor"
#     print(f'Bye {name} {sur_name}')
#
#
# say_hi()
# say_bye()

#Скрытие переменных /global
# name = "T-800"
# print(name)
#
# def say_hi():
#     global name
#     name = "Sara"
#     print(f'Hello {name}')
#
# def say_bye():
#     print(f'Bye {name} ')
#
#
# say_hi()
# say_bye()

# nonlocal

# def outer(): # - внешняя
#     num = 5
#
#     def inner(): #- вложенная
#         nonlocal num # - указываем, что num это переменная из окружающей функции
#         num = 25
#         print(num)
#
#     inner() # 25
#     print(num)
#
# outer() # 25


#замыкания - https://metanit.com/python/tutorial/2.19.php

# def outer(): # - внешняя
#     num = 5 # - лексическое окружение
#
#     def inner(): #- вложенная
#         nonlocal num # - указываем, что num это переменная из окружающей функции
#         num += 1
#         print(num)
#
#     return inner
#
#
# fu = outer()
# fu()
# fu()
# fu()

#Применение параметров
def multiply(n):
    def inner(m): return n * m

    return inner


fn = multiply(5)
print(fn(5))  # 25
print(fn(6))  # 30
print(fn(7))  # 35
