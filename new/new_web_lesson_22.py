#Полиморфизм в процедурном программировании на основе знака "+"
# num1 = 1
# num2 = 2
# print(num1+num2)

# str1 = "hi "
# str2 = "Python"
# print(str1+str2)

#Полиморфизм в функциях len()
# print(len((1,2,4,5,6,4)))
# print(len([1,2,4,5,6,4]))
# print(len({1:"mon",2:"Tue",4:"wed",5:"Th"}))

#Полиморфизм в классах
# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Animal - Cat\n"
#               f"Age - {self.age}\n"
#               f"Name - {self.name}")
#
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Animal - Dog\n"
#               f"Age - {self.age}\n"
#               f"Name - {self.name}")
#
#     def make_sound(self):
#         print("Bark")
#
#
# cat1 = Cat("Kitty",7)
# dog1 = Dog("Fluffy",8)
#
# for animal in (cat1,dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

#Перегрузка операторов
# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     #перегрузка оператора +
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"Vector({self.x},{self.y})"
#
# v1 = Vector(2,4)
# v2 = Vector(5,-1)
#
# v3 = v1 + v2
# print(v3)

#пошаговый разбор
# v1+v2
# v1.__add__(v2)

import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(30, 50)
print("Rectangle area:", rect.area())


#https://habr.com/ru/articles/552922/
#https://metanit.com/python/tutorial/7.8.php