#гитхаб подключение и регистрация 
# аналог - https://gitflic.ru
# Декораторы
# # модифицировать функцию не изменяя её исходного кода.
# def select(input_func):
#     def output_func():
#         print('**********')
#         input_func()
#         print('**********')
#     return output_func
#
# @select
# def hi():
#     print('Hi Web!')
#
# hi()

# материал лекции - https://metanit.com/python/tutorial/2.28.php
# курс степик для продвинутых - https://stepik.org/course/68343/promo

# ДЗ «Повторитель» (Декоратор с аргументами)
# Создайте декоратор repeat(n), который принимает число n и вызывает декорируемую функцию n раз.
# @repeat(3)
# def greet():
#     print("Привет!")
#
# greet()
# # Ожидаемый вывод:
# # Привет!
# # Привет!
# # Привет!
