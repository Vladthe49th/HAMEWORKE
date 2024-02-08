import random
# liest_1 = [i*i for i in range(6)]
# print(liest_1)
# liest_2 = [i+"/" for i in "Vlad"]
# print(liest_2)
# liest_3 = [i*2 for i in "Konstantin"]
# print(liest_3)
# liest_4 = [i*i for i in range(1,12) if i % 2 == 0]
# print(liest_4)
# liest_5 = ["Maul", "Battle droid", "Plagueis", "Sheev"]
# liest_6 = [i for i in liest_5 if i!= "Maul" and i!= "Plagueis"]
# print(liest_6)

# liest_6 = [[x*y for x in range(1, 5)] for y in range(1, 5)]
# print(liest_6)

# liest_1 = ["JavaScript", 668, 99.9, 47, "Burden 1", "C++"]
# print(liest_1[0], liest_1[-4])
# print(liest_1[1:4])
# print(liest_1[-4:-1])
# print(liest_1[:-1])
# print(liest_1[3:])
# print(liest_1[::2])
# print(liest_1[::-1])
# print(liest_1[-4::-1])
# name = "Qui-Gon"
# liest_1[-1] = name
# print(liest_1)

# login = ["Sysadmin", "dominant", "submissive", "consumer", "har", "consumer", "har"]
# if ("consumer" in login):
#     print("consumer open doc")
# else:
#     print("error")

random_numbers = [random.randint(-100, 100) for _ in range(20)]

even_numbers = [num for num in random_numbers if num % 2 == 0]

odd_numbers = [num for num in random_numbers if num % 2 != 0]

negative_numbers = [num for num in random_numbers if num < 0]

positive_numbers = [num for num in random_numbers if num > 0]

print("Список випадкових чисел:", random_numbers)
print("Список парних чисел:", even_numbers)
print("Список непарних чисел:", odd_numbers)
print("Список від'ємних чисел:", negative_numbers)
print("Список додатніх чисел:", positive_numbers)


