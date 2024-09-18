""" 1 """
"""Создайте словарь"""

my_bio = {'name': 'Saiahmad','age':19,'fav color':'black'}
# print(my_bio)

""" 2 """
"""Добавьте элемент(хобби)"""

my_bio['hobby'] = "coding"
# print(my_bio)

""" 3 """
"""Извлечь значения(возраст)"""

# print(my_bio.get("age"))

""" 4 """
"""Обновить значения(Любимый цвет)"""

my_bio['fav color'] = "blue"
# print(my_bio)

""" 5 """
"""Удалить значения(хобби)"""

del my_bio['hobby']
# print(my_bio)

""" Set """

"""Уникальные элементы"""


def unique_elements(input_list):
    return set(input_list)

my_list = [1,2,3,4,5,6,7,1,2,3,4]
unique_set = unique_elements(my_list)
print(unique_set)


# def unique_elements(input_list):
#     return {x for x in input_list}

# my_list = [1,2,3,4,5,6,7,1,2,3,4]
# unique_set = unique_elements(my_list)
# print(unique_set)

""" Объединение множеств """

# num_1 = {1,2,3,4,5,6,7}
# num_2 = {4,5,6,7,8,9,0}
# result = num_1.union(num_2)
# print("Объединенное множесто:",result)


# num_1 = {1,2,3,4,5,6,7}
# num_2 = {4,5,6,7,8,9,0}
# result = num_1 | num_2
# print("Объединенное множесто:",result)

""" Пересечение множеств """

# def intersection(num_1,num_2):

#     result = num_1.intersection(num_2)
#     return result

# num_1 = {1,2,3,4,5,6,7}
# num_2 = {4,5,6,7,8,9,0}

# result = intersection(num_1,num_2)
# print("Пересечение множеств:",result)

"""Удаление дубликатов из списка"""

# def remove_duplicates(input_list):
  
#     unique_elements = set(input_list)
      
#     result_list = list(unique_elements)
    
#     return result_list

# my_list = [1, 2, 2, 3, 4, 4, 5]
# result = remove_duplicates(my_list)
# print("Список без повторяющихся элементов:", result)


# def remove_duplicates(input_list):
#     unique_elements = set(input_list)
#     result_list = list(unique_elements)
#     return result_list

# my_list = [1, 2, 2, 3, 4, 4, 5]
# result = remove_duplicates(my_list)
# print("Список без повторяющихся элементов:",result)

"""Проерка подмножество"""

# def is_subset(set1, set2):
#     return set1.issubset(set2)

# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,5,6,7,8}

# result = is_subset(set1,set2)
# print("Является ли set1 подмножеством set2?",result)





"""Frozensen"""

"""Создание frozenset"""

# numbers = frozenset([1,2,3,4,5,6,7,8])
# numbers.add(0)
# print(numbers)

"""Пересечение frozenset"""

# def frozenset_intersection(fset1, fset2):
#     return fset1.intersection(fset2)

# fset1 = frozenset([1, 2, 3, 4])
# fset2 = frozenset([3, 4, 5, 6])

# result = frozenset_intersection(fset1, fset2)
# print("Пересечение двух frozenset:", result)

"""Сравнение frozenset"""

# def compare_frozensets(fset1, fset2):
#     if fset1 == fset2:
#         return "Множества равны"
#     elif fset1 < fset2:
#         return "Первое множество является подмножеством второго"
#     elif fset2 < fset1:
#         return "Второе множество является подмножеством первого"
#     else:
#         return "Множества не равны и ни одно не является подмножеством другого"

# fset1 = frozenset([1, 2, 3, 4])
# fset2 = frozenset([3, 4, 5, 6])

# result = compare_frozensets(fset1, fset2)
# print(result)

"""Преоброзавание frozenset в список"""

# frozen_set = frozenset([1,2,3,4,5,6,7,8])
# list_from_frozenset = list(frozen_set)
# print(list_from_frozenset)

"""Сложение frozenset"""

# fset1 = frozenset([1,2,3])
# fset2 = frozenset([4,5,6])
# fset3 = fset1 | fset2
# print(fset3)