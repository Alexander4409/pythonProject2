#Полиморфизм это способность кода работать с объектами разных типов через единый интерфейс.
# Это один из «трёх китов» объектно-ориентированного программирования (ООП), позволяющий
# одной и той же функции или методу вести себя по-разному в зависимости от того, с каким
# объектом они взаимодействуют.

# классический полиморфизм
# class Animal:
#     def create_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def create_sound(self):
#         return "Meow"
#
#
# class Dog(Animal):
#     def create_sound(self):
#         return "Bark"
#
#
# class Parrot(Animal):
#     def create_sound(self):
#         return "Hello there!"
#
#
# def make_animal_sound(animal):
#     print(animal.create_sound())
#
#
# animals = [Dog(), Cat(), Parrot()]
#
# for _ in animals:
#     make_animal_sound(_)


#Параметрический полиморфизм
# from typing import TypeVar,List
#
# T = TypeVar("T")
#
# def reverse_list(items: List[T]) -> List[T]:
# # функция вернёт список того же типа который и получила
#     return items[::-1]
#
# nums = reverse_list([1,2,3])
# lst_str = reverse_list(["a","d","g"])
#
# print(nums)
# print(lst_str)


# пример работы класса сейф
# from typing  import Generic,TypeVar, List
#
# T = TypeVar("T")
#
# class Storage(Generic[T]):
#     def __init__(self):
#         self.__items: List[T] = []
#
#     def put(self,item: T):
#         self.__items.append(item)
#         print(f"Добавлено: {item}")
#
#     def get_all(self) -> List[T]:
#         return self.__items
#
# #1 сейф для чисел
# int_storage = Storage[int]()
# int_storage.put(10)
# int_storage.put(20)
# int_storage.put("sdfsdfvcsd")# IDE вам посветит ошибку
# #2 сейф для букв
# str_storage = Storage[str]()
# str_storage.put("Gold")
# str_storage.put("Platinum")
#
# print(f"first storage : {int_storage.get_all()}")
# print(f"second storage : {str_storage.get_all()}")

#Магические методы
# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(1,2)
# v2 = Vector(4,5)
#
# print(v1+v2)

#ДЗ объём и площадь фигур дописать при помощи магических методов, и с применением полиморфизма