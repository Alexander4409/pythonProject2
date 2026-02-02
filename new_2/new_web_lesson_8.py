#Декораторы



# *******
# Hello
# *******
#Декоратор
# def select(input_func):
#     def stars(name):
#         print("*" * 5)
#         input_func(name)
#         print("*" * 5)
#     return stars
#
#
# @select
# def hi(name):
#     print(f"Hello {name}")
#
#
# hi(input())


# def doubel_res(func):
#     def wrapper(*args):
#         res = func(*args)
#         return res * 2
#     return wrapper
#
# @doubel_res
# def summ(num1,num2):
#     return num1+num2
#
# print(summ(4,5))


#Перехват аргументов функции
# def check(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age < 0: age = 1
#         input_func(name, age)
#     return output_func
#
#
# @check
# def print_person_info(name,age):
#     print(f'Name: {name}, Age: {age}')
#
# print_person_info("Tom", -23)

