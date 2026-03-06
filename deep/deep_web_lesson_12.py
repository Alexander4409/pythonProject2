#Статические методы и атрибуты класса

#Задаёт общий атрибут класса
# class Person:
#     type = "Person"
#     description = "Описание персоны"
#
# print(Person.type)
# print(Person.description)
#
# Person.type = "Class Person"
# print(Person.type)


# class Person:
#     type = "Person"
#     def __init__(self,name):
#         self.name = name
#
# tom = Person("Tom")
# bob = Person("Bob")
#
# print(tom.type)
# print(bob.type)
#
# Person.type = "Class Person"
#
# print(tom.type)
# print(bob.type)


#Статические методы

# class Person:
#     __type = "Person"
#     description = "Описание персоны"
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def type_info():
#         print(Person.__type)
#
# Person.type_info()
#
# tom = Person("Tom")
# bob = Person("Bob")
#
# tom.type_info()
# bob.type_info()

#Переопределение __str__()
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(self)
#
#         print(self.__str__())
#         # print(f"Name :{self.name}\n"
#         #       f"Age :{self.age}")
#
#     def __str__(self):
#         return f"Name :{self.name} Age :{self.age}"
#
#
# tom = Person("Tom", 22)
#
# tom.display_info()

#Абстрактные классы
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

rect = Rectangle(11,22)
print("Rectangle area", rect.area())