# task 3
# nums = [1, 2, 3, 1, 2, 5, 6, 2, 3]
#
#
# def find_longest_incremental(data):
#     if not data: return []
#
#     sequences = []
#     current_seq = [data[0]]
#
#     for i in range(1, len(data)):
#         if data[i] > data[i - 1]:
#             current_seq.append(data[i])
#         else:
#             sequences.append(current_seq)
#             current_seq = [data[i]]
#     sequences.append(current_seq)
#
#     max_len = len(max(sequences, key=len))
#     return [seq for seq in sequences if len(seq) == max_len]
#
#
# print("Самые длинные возрастающие последовательности:", find_longest_incremental(nums))

#https://www.geeksforgeeks.org/python/python-program-right-rotate-list-n/
# Сортировка перемешиванием
# Гномья сортировка
# Плавная сортировка
# сортировка пузырьком
# сравнить время работы с разными типами списков
# (Список с маленькими числами 0.00002 и большими 10000000)


# ДЗ
# историческая справка сортировки
# показать реализацию
# какой тип списков она отсортирует быстрее всех
# ресурсы
# презентация


