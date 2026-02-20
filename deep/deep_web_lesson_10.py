#Наследование
# Супер класс - базовый класс в котором есть
# реализация методов и атибутов и от которого они наследуются другими подклассами
# Подкласс(дочерний класс)-наследует от супер класса все публичные атрибуты и методы

# class Human:
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_inf(self):
#         print(f"Name: {self.__name}")
#
#
# class Employer(Human):
#
#     def go_to_work(self):
#         print(f"{self.name} go to work")
#
#
#
# bob = Employer('Bob')
# bob.go_to_work()
# bob.display_inf()

#Множественное наследование

# class Human:
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_inf(self):
#         print(f"Name: {self.__name}")
#
#
# class Employer(Human):
#
#     def go_to_work(self):
#         print(f"{self.name} go to work")
#
#
# class Student(Human):
#
#     def go_to_lecture(self):
#         print(f"{self.name} go to lecture")
#
#
# class WorkingStudent(Employer,Student):
#
#     # def...
#     pass
#
# bob = Employer('Bob')
# bob.go_to_work()
# bob.display_inf()
#
# john = Student('John')
# john.go_to_lecture()
# john.display_inf()

#Очень плохо когда есть методы с одинаковым названием
class Student:
    def do(self):
        print("Student studies")

class Employee:
    def do(self):
        print("Employee works")


# class WorkingStudent(Student,Employee):
class WorkingStudent(Student, Employee):
    pass


tom = WorkingStudent()
tom.do()  # ?


#посмотреть очерёдность применения функционала
print(WorkingStudent.__mro__)
print(WorkingStudent.mro())


# Дз Умный дом (Инкапсуляция + Наследование)
# Создайте класс Device (прибор) с атрибутом __is_on (приватный) и методами turn_on()/turn_off().
# Дочерние классы: Light (с регулировкой яркости) и AirConditioner (с установкой температуры).
# Задача: Сделайте так, чтобы изменить температуру или яркость можно было только если прибор включен.
# Если прибор выключен, метод должен выводить предупреждение.
