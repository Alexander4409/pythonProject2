#Сортировка - это перестановка элементов массива или списка каким либо особым образом
# Оптимальные алгоритмы позволяют снизить выполнение различных задач
# Пузырьковая сортировка - Сравнивает элементы и если один больше другого то она их переставляет.
# Сортировка вставками - Работает путем вставки элемента в уже отсортированный массив О(n^2)
# Сортировка выбором - выбирает минимальный элемент из не отсортированной части
# и помещает его в конец отсортированной
# Пирамидальная сортировка - использует heap !!!
# ДЗ повторить сложности алгоритмов!!!!

# Временная сложность - сколько времени требуется на сортировку (О - большое (n)ключевые понятия)
# Пространственная сложность - сколько памяти будет потреблять алгоритм
# Стабильность алгоритма - сохранение относительного порядка при сортировке
# элементов с несколькими ключами

# Классификация
# Внутренние или внешние
# Методика реализации


# быстрая сортировка
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr # базовый случай если длинна списка <= 1
#
#     pivot = arr[len(arr) // 2] # выбираю середину списка
#     left = [x for x in arr if x < pivot]
#     midl = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quick_sort(left) + midl + quick_sort(right)
#
# arry = [10,3,5,2,56,8,45,86,3]
#
# sorted_lst = quick_sort(arry)
#
# print(f'un sorted - {arry}\n'
#       f'sorted List {sorted_lst}')


# сортировка слиянием

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)


def merge(left,right):
    sorted_lst = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    sorted_lst.extend(left[i:])
    sorted_lst.extend(right[j:])
    return sorted_lst


arry = [10,3,5,2,56,8,45,86,3]

sorted_lst = merge_sort(arry)

print(f'un sorted - {arry}\n'
      f'sorted List {sorted_lst}')

