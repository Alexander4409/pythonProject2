#Списки
#Обращение к элементам списка и срезы
# people = ["Tom","John","Marry","Nancy"]
#
# print(people[-1])
# print(people[1])
# print(people[-2])

#Срезы
# lst[1:3:1] - start:stop:step /начало,конец,шаг(все обозначается цифрами(индексами))
# people = ["Tom","John","Marry","Nancy","Bob","Sam"]
# s_people = people[::-1]
# print(s_people)

#Получение и изменение элементов списка
# people = ["Tom","John","Marry","Nancy"]
# people[1] = "Mike"
# print(people)

#Сортировка
# count_to_ten = [1,4,2,5,3,6,8,7,9,10]
# print(count_to_ten)
# count_to_ten.sort()
# count_to_ten.reverse()
# print(count_to_ten)


# people = ["Tom","john","Marry","Nancy","bob", "alice", "Sam", "Bill"]
# print(people)
# people.sort()
# print(people)
# people.sort(key= str.lower)
# print(people)
# sorted_people = sorted(people,key= str.lower)
# print(sorted_people)

#Фильтрация
# filter(foo,iter)
# nums = [-5,-4,-3,-2,1,4,2,5,-3,6,-8,-7,9,-10]
#
# def condition(num):
#     return num > 0
#
# res = filter(condition,nums)
#
# for n in res:
#     print(n,end=",")

#map Проекция\преобразование списков
# nums = [1,2,3,4,5]
#
# def power_3(num):
#     return num ** 3
#
# res = map(power_3,nums)
#
# for n in res:
#     print(n,end=' ')

#дз
# Реализуйте код который отфильтрует список
# элементов на четные и не четные при помощи функции filter

# Задача написать код для преобразования отрицательных
# чисел из списка в положительные при помощи map