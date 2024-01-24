my_list = [1, "bye", True, [9, 10, 11],{"m": "k"}]
print(len(my_list))
print(my_list[3])
print(my_list[2])
print(my_list[1:4])
print(my_list.append(200))
print(my_list)
my_list.insert(1, 0.5)
print(my_list)
my_list[4].append(False)
print(my_list.count(200))
print(my_list.index(200))
my_list.remove(True)
print(my_list)
my_list = [10, 0.5, 'bye', True, [7,8,9,False], {'m': 'k'}, 200, 600]
new = my_list.copy()
print(new)
my_list[4][3] = True
print(my_list)
print(new)
import copy
my_list = [10, 0.5, 'bye', True, [7, 8, 9, False], {'m': 'k'}, 200, 600]
new = copy.deepcopy(my_list)

my_list[4][3] = True
print(my_list)
print(new)
my_list.extend(new)
my_list += new
print(my_list)
my_list.clear()
print(my_list)



a = list('py')
print(a)