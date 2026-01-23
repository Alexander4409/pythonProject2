# упорядочивание - основа управления данными
# Сортировка - перестановка элементов в массиве определённым образом
#1 пузырьковая сортировка - сравнение двух чисел согласно условиям они меняются
# или не меняются местами
#2 Быстрая сортировка - деление массива на под-массивы с последующей рекурсией
#3 Сортировка вставками - Работает путем вставки каждого нового
# элемента в уже отсортированный массив.
#4 сортировка выбором - на каждом шаге мы ищем минимальное и максимальное значение О(n^2)
#5 Сортировка слиянием - есть общее с бинарным поиском
# Временная сложность
# - O(n) линейная сложность
# пространственная сложность - определяет сколько памяти надо для работы алгоритма
# Стабильность - сохранения порядка одинаковых элементов,
# особенно при сортировке элементов с несколькими ключами

# Быстрая сортировка
# def quik_sort(arr):
#     if len(arr) <= 1:
#         return arr
#         # базовый случай когда массив состоит из 0 или 1 элемента
#
#     pivot = arr[len(arr) // 2 ] # выбрали середину в качестве опорного элемента
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quik_sort(left) + middle + quik_sort(right)
#
# arry = [2,3,5,2,4,7,8,6,43,32,54]
#
# print(f'non sorted  - {arry}')
#
# sorted_arry= quik_sort(arry)
#
# print(f'sorted arry - {sorted_arry}')

import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        # Фиксируем время начала
        start_time = time.perf_counter()

        # Выполняем саму функцию
        result = func(*args, **kwargs)

        # Фиксируем время окончания
        end_time = time.perf_counter()

        # Вычисляем разницу
        run_time = end_time - start_time

        print(f"Функция: {func.__name__}")
        print(f"Время выполнения: {run_time:.4f} сек.")
        print("-" * 30)

        return result

    return wrapper
#Сортировка слиянием
@benchmark
def merge_sort(arr):
    if len(arr) <=1:
        return arr #базовый случай

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)


def merge(left, right):
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

arr = [2,3,5,2,4,7,8,6,43,32,54]

sorted_arr= merge_sort(arr)

print(f'sorted arr - {sorted_arr}')

#ДЗ вам нужно сравнить временную сложность этих двух алгоритмов
#  сколько памяти требуется на работу алгоритма (доп задание)




# Пример использования
@benchmark
def fetch_data():
    time.sleep(1.5)  # Имитация долгой работы
    return "Данные получены"


fetch_data()