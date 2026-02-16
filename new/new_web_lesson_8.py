#Декораторы
#*****
#Hello
#*****

# def decor(input_fuc):
#     def wrapper():
#         print("*" * 5)
#         input_fuc()
#         print("*" * 5)
#     return wrapper
#
#
# @decor
# def say_hi():
#     print("Hello")
#
# say_hi()
#
#
# def say_bye():
#     print("Good bye")
#
#
# say_hi()
#
# say_bye()

# def double_result(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result * 2
#     return wrapper
#
# @double_result
# def summ(num1,num2,num3):
#     return num1+num2+num3
#
#
# print(summ(4,5,6))

#Перехват параметров
def check(input_func):
    def wrapper(*args):
        name = args[0]
        age = args[1]
        if age < 0 : age = 67
        input_func(name,age)
    return wrapper


@check
def print_user_info(name,age):
    print(f'Name: {name}\n'
          f'Age: {age}')

print_user_info("John",21)
print_user_info("Франклин Клинтон",-25)

# Получение результата функции
# def check(input_func):
#     def wrapper(*args):
#         res = input_func(*args)
#         if res == 67:
#           res = 0
#         return res
#     return wrapper
#
# @check
# def summ(num1,num2):
#     return num1+num2
#
# @check
# def mult(num1,num2):
#     return num1*num2
#
#
#
# res1 = summ(60,7)
# print(res1)
#
# res2 = mult(60,7)
# print(res2)
