#ООП
#объект - имеет 3 ключевых показателя, тип, идентификатор, значение
# num = 14
#
# print(id(num))
#
# num_2 = 15
# print(hex(id(num_2)))


# класс - это шаблон благодаря которому мы можем перенести некоторые
# физические свойства объекта в цифровой мир
# class Person:
#     pass
# # tom и bob это экземпляры(объекты) класса которые получены из класса Person
# tom = Person()
# bob = Person()
#
# print(type(tom))

class Human:
    #метод класса
    def __init__(self,name,age):
        # Атрибуты класса
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello")



# Объекты класса (экземпляры)
tom = Human("Tom",23)
bob = Human("Bob", 24)

bob.say_hi()

# #Обращение к атрибутам экземпляров класса
# print(tom.age)
# print(bob.age)
# print(tom.name)
#
# tom.age = 37
# print(tom.age)
# #Динамический атрибут !!! ненада
# tom.company = "VK"
# print(tom.company)

#https://metanit.com/python/tutorial/7.1.php


