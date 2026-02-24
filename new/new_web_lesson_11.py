#Списки
#Обращение к элементам списка и срезы
# people = ["Tom","John","Marry","Nancy"]
#
# print(people[-1])
# print(people[1])
# print(people[-2])

#Индексы у списков начинаются с 0
#Срезы
#lst[start:stop:step]
# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# half_people_list = people[::-1]
# print(half_people_list)
# lst = [1,2,3,4,5,6,7,8,9,10]

#Замена элементов
# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# people[1] = "Mike"
# print(people)

#сортировка списков
# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# print(people)
# people.sort()
# print(people)
# people = ["Tom", "bob", "Alice", "Sam", "tim", "Bill"]
# print(people)
# sorted_people_lst = sorted(people, key=str.lower)
# print(sorted_people_lst)

#фильтрация списка
# numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
# def condition_nums(number):
#     return number > 1
#
# res = filter(condition_nums,numbers)
#
# for num in res:
#     print(num,end=", ")

# Функция map (Преобразование списков)
# numbers = [ 1, 2, 3, 4, 5]
# def square(nums):
#     return nums ** 2
#
# res = map(square,numbers)
#
# for num in res:
#     print(num,end=", ")

# дз для тех кто не сделал
# Реализуйте код который отфильтрует список
# элементов на четные и не четные при помощи функции filter

# Задача написать код для преобразования отрицательных
# чисел из списка в положительные при помощи map