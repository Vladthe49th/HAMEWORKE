import random

random_numbers = [random.randint(-100, 100) for _ in range(20)]
print("Згенерований список:", random_numbers)

negative_sum = sum(i for i in random_numbers if i < 0)
print("Сума від'ємних чисел:", negative_sum)

even_sum = sum(i for i in random_numbers if i % 2 == 0)
print("Сума парних чисел:", even_sum)

odd_sum = sum(i for i in random_numbers if i % 2 != 0)
print("Сума непарних чисел:", odd_sum)

mult_3 = 1
for i, num in enumerate(random_numbers):
    if i % 3 == 0:
        mult_3 *= num
print("Добуток елементів з індексами кратними 3:", mult_3)

min_index = random_numbers.index(min(random_numbers))
max_index = random_numbers.index(max(random_numbers))
if min_index > max_index:
    min_index, max_index = max_index, min_index
min_max = 1
for num in random_numbers[min_index + 1:max_index]:
   min_max *= num
print("Добуток елементів між мінімальним і максимальним елементом:", min_max)

positive_indices = [i for i, num in enumerate(random_numbers) if num > 0]
if len(positive_indices) >= 2:
    first_positive_index = positive_indices[0]
    last_positive_index = positive_indices[-1]
    sum_between_positive = sum(random_numbers[first_positive_index + 1:last_positive_index])
    print("Сума елементів, що знаходяться між першим та останнім додатними елементами:", sum_between_positive)

