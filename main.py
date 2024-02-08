import random

list_1 = [random.randint(-100, 100) for _ in range(10)]
list_2 = [random.randint(-200, 200) for _ in range(10)]
print(list_1)
print(list_2)
list_3 = list_1 + list_2
print(f"Elemtents of both lists: \n{list_3}")
list_4 = set(list_3)
print(f"All elements without repeats: \n{list_4}")
list_5 = [element for element in list_1 if element in list_2]
print(f"Common elements: \n{list_5}")
list_6 = [element for element in list_1 if element not in list_2]
list_7 = [element for element in list_2 if element not in list_1]
print(f"Unique elements: \n{list_6 + list_7}")
min_max_1 = [min(list_1), max(list_1)]
min_max_2 = [min(list_2), max(list_2)]
min_max_3 = min_max_1 + min_max_2
print(f"Min and max elements: \n{min_max_3}")