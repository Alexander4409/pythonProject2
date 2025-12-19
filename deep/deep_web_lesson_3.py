#Иттераторы - https://habr.com/ru/companies/domclick/articles/674194/
# tumb = {"pencil", "apple", "book"}
#
# str_1 = "gfseodgndgndfjign"
#<str_ascii_iterator object at 0x00000164EC289360>

#Цикл for работает не с объектами внутри коллекции, а с правилом перебора этой коллекции
# print(iter(str_1))
#<list_iterator object at 0x0000019031BF9360>
# num = 23231
#
# print(iter(num))

# for obj in tumb:
#     print(obj)
'''Аналог цикла for написанный через while'''

# tumb = {1,3,54,323,False,"fdff",True}
#
# it = iter(tumb)
#
# try:
#     while True:
#         next_value = next(it)
#         print(f'One more value {next_value}')
# except StopIteration:
#     print("Iteration is stopped")
# print("Program is stopped")
'''Функции'''
# name - аргумент
# Инструкция
# def say_hi (name):
#     print(f"Привет {name}")
#
# say_hi("Sasha")


# def sum(num,num_1):
#     res = num + num_1
#     return res
#
# print(sum(1,2))

# def print_mesage():
#     # Локальные функции
#     def say_by ():print(f"by")
#     def say_hi ():print(f"hi")
#
#
#     say_hi()
#     say_by()
#
# print_mesage()
#Организация программы функции main
# def main():
#     say_hi()
#     say_by()
#
# def say_by ():
#     print(f"by")
#
#
# def say_hi ():
#     print(f"hi")
#
# main()

# def main():
#     num_1 = 3
#     num_2 = 2
#     print(multiplication(num_1, num_2))
#     print(summ(num_1, num_2))
#
#
#
#
# def summ(num_1,num_2):
#     res_summ = num_1 + num_2
#     return res_summ
#
#
# def multiplication(num_1,res_summ):
#     res_mult = num_1 * res_summ
#     return res_mult
#
# main()\
#передача множественных аргументов
#Доразобрать!!! - https://metanit.com/python/tutorial/2.15.php
def say_hello(name="Tom", age = 12):
    print(f"Hello, {name}")
    print(f'{name}s age is {age}')


say_hello(age=12)  # здесь параметр name будет иметь значение "Tom"
say_hello("Bob",12)  # здесь name = "Bob"