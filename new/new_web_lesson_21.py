#Наследование
# подкласс(класс ребенок) - класс, который заимствует функционал класса родителя(супер класса)
# Супер класс (Базовый класс) - содержит реализацию основного функционала

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_inf(self):
#         print(f'User name - {self.__name}')
#
#
# class Employer(Person):
#
#
#     def work(self):
#         print(f'{self.name}, is working')
#
#
# class Student(Person):
#
#     def study(self):
#         print(f'{self.name}, is learning')
#
#
# tom = Employer("Tom")
# tom.display_inf()
# tom.work()
#
# bob = Student('Bob')
# bob.display_inf()
# bob.study()

# class Shape:
#     def __init__(self,figur_name):
#         self.figur_name = figur_name
#
#     def get_area(self):
#         raise NotImplementedError("Method error")
#
#
# class Rectangle(Shape):
#     def __init__(self,width, height):
#         super().__init__("Rectangle")
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.height * self.width
#
# class Triangle(Shape):
#     def __init__(self,base, height):
#         super().__init__("Triangle")
#         self.base = base
#         self.height = height
#
#     def get_area(self):
#         return 0.5 * self.base * self.height
#
#
# shapes = [ Rectangle(3,10), Triangle(3,4) ]
# for shape in shapes:
#     print(f"Figure {shape.figur_name}, Area = {shape.get_area()}")



class Employee:
    def __init__(self,hourly_rate):
        self.hourly_rate = hourly_rate

    def calc_salery(self, hours):
        return self.hourly_rate * hours

    def work(self):
        print("Employer works")


class Student:
    def __init__(self,scholarship):
        self.scholarship = scholarship

    def study(self):
        print("Student studies")

class WorkingStudent(Employee, Student):
    def __init__(self, hourly_rate, scholarship):
        Employee.__init__(self,hourly_rate)
        Student.__init__(self,scholarship)

    def get_total_income(self, hours):
        salary = self.calc_salery(hours)
        total = salary + self.scholarship
        return total

tom = WorkingStudent(100, 1000)

hours_worked = 40
print(f'Salary: {tom.calc_salery(hours_worked)}\n'
      f'Scholarship: {tom.scholarship}\n'
      f'Total income: {tom.get_total_income(hours_worked)}')

#доп материалы - https://metanit.com/python/tutorial/7.3.php



