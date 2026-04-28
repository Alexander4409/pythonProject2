#Деструкторы класса
# class Human:
#     #метод класса
#     def __init__(self,name,age):
#         # Атрибуты класса
#         self.name = name
#         self.age = age
#         print("Crate human name", self.name)
#
#     def __del__(self):
#         print("Delete human name", self.name)
#
#
#
# def create_human():
#     tom = Human("Tom",40)
#
# create_human()
# print("End program")



#Инкапсуляция
# class Human:
#     #метод класса
#     def __init__(self,name,age):
#         # Атрибуты класса
#         self.__name = name
#         self.__age = age
#         print("Crate human name", self.__name)
#
#     def print_info(self):
#         print(f'Name: {self.__name}\n'
#               f'Age: {self.__age}')
#
#
# tom = Human("Tom",40)
# tom.__name = "Человек муравей"
# tom.__age = -37
#
# print(tom.__name)
#
# tom.print_info()



#Шаблон для объявления атрибута
# _ClassName__atribute


#Геттеры и сеттеры

# class Human:
#     #метод класса
#     def __init__(self,name,age):
#         # Атрибуты класса
#         self.__name = name
#         self.__age = age
#         print("Crate human name", self.__name)
#
#     #Метод регулирования возраста
#     def set_age(self,age):
#         if 0 < age < 120:
#             self.__age = age
#         else:
#             print("Error, corrupted age!")
#
#     #Метод для получения возраста
#     def get_age(self):
#         return self.__age
#
#     # Метод для получения имени
#     def get_name(self):
#         return self.__name
#
#     def print_info(self):
#         print(f'Name: {self.__name}\n'
#               f'Age: {self.__age}')
#
#
#
# tom = Human("Tom",32)
# tom.print_info()
#
# tom.set_age(45)
# tom.print_info()
#
# print(tom.get_name())

#Аннотация свойств
# @property

class Human:
    #метод класса
    def __init__(self,name,age):
        # Атрибуты класса
        self.__name = name
        self.__age = age


    #Свойство геттер
    @property
    def age(self):
        return self.__age

    #Свойство сеттер
    @age.setter
    def age(self,age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Error, corrupted age!")

    #Мы можем определить только геттер без сеттера
    @property
    def name(self):
        return self.__name

    def print_info(self):
        print(f'Name: {self.__name}\n'
              f'Age: {self.__age}')


tom = Human("Tom",32)
tom.print_info()
#
print(tom.age)
tom.age = 25
tom.print_info()
#
# print(tom.get_name())