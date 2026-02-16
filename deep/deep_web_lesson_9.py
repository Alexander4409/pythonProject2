#Инкапсуляция
#Нельзя допускать изменение чувствительной информации извне класса
# __ - Инкапсуляция для создания приватных атрибутов

# class Human:
#     def __init__(self,name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_info(self):
#         print(f'Name - {self.__name}\n'
#               f'Age - {self.__age}')
#
#
# jeffry = Human("Jeffry",45)
# jeffry.print_info()
#
# jeffry._Human__name = 'Badman'
# jeffry.print_info()


#Методы доступа
#1 Геттеры и Сеттеры

# class Human:
#     def __init__(self,name, age):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self,age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print(f'Incorrect age')
#
#     def get_age(self):
#         return self.__age
#
#
#     def get_name(self):
#         return self.__name
#
#     def print_info(self):
#         print(f'Name - {self.__name}\n'
#               f'Age - {self.__age}')
#
#
# jeffry = Human("Jeffry",45)
# jeffry.print_info()
# jeffry.set_age(-1232123)
# jeffry.set_age(12)
# jeffry.print_info()

#2 Аннотации свойств

# class Human:
#     def __init__(self,name, age):
#         self.__name = name
#         self.__age = age
#
#     #геттер
#     @property
#     def age(self):
#         return self.__age
#
#     #Сеттер
#     @age.setter
#     def age(self,age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print(f'Incorrect age')
#
#     @property
#     def name(self):
#         return self.__name
#
#     def print_info(self):
#         print(f'Name - {self.__name}\n'
#               f'Age - {self.__age}')
#
#
# jeffry = Human("Jeffry",45)
# jeffry.print_info()
# jeffry.age = -1232123
# jeffry.age = 12
# jeffry.print_info()
# 1 - сеттер определяется после геттера
# 2 - сеттер и геттер называются одинаково
# 3 - Если геттер называется (имя) то над сеттером ставим аннотацию (@имя.setter)

# Напишите класс электронная библиотека
# 1 (пользователь заносит книги в список) задаётся список книг(после этого название книги, имя автора и вес - поменять
# нельзя, но можно получить данные
# о страницах о весе книги, и об авторе)
# 2 можно измять данные о % прочитывания книги, предусмотреть отрицательные % и проценты < 100%, Больше 100 % нельзя

