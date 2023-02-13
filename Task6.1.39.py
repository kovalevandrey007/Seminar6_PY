# №6.1[39]. Даны два списка чисел. Требуется вывести те
# элементы первого списка , которых нет во втором списке.
# Создайте функцию.
#     Аргументы: два списка целых чисел
#     Возвращает: список элементов (смотри условие)

# Примеры/Тесты:
#     <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
#     <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

# [*] Усложнение. Элементы необходимо возвращать в том порядке,
# в котором они находятся в первом списке, с учетом повторений
# Примеры/Тесты:
#     <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
#     <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]

# list1 = [3, 1, 3, 4, 2, 4, 12]
# list2 = [4, 15, 43, 1, 15, 1]


# 1 вариант 2 способами
# def difference_set(l: list, l_1: list) -> list:
#     return list(set(l).difference(set(l_1)))
#
# print(difference_set([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
# print(difference_set([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))
#
# n= 10000
# l
#
# def diff_list(l: list, l_1: list) -> list:
#     result = []
#     for element in l:
#         if element not in l_1:
#             result.append(element)
#     return result
# print(diff_list([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))

from time import perf_counter
from random import randint

def diff_set(l: list, l_1: list) -> list:
    t_1 = perf_counter()
    new_set = list(set(l).difference(set(l_1)))
    t_2 = perf_counter()
    return new_set, t_2 - t_1

def diff_list(l: list, l_1: list) -> list:
    t_1 = perf_counter()
    result = []
    for el in l:
        if el not in l_1 and el not in result:
            result.append(el)
    t_2 = perf_counter()
    return result, t_2 - t_1


n = 10000
lst1 = [randint(0,int(n)) for i in range(n)]
lst2 = [randint(0,int(n)) for i in range(n)]

print(diff_list(lst1, lst2)[1])
print(diff_set(lst1, lst2)[1])

