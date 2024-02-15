print("Task 1: \n")

n = int(input("Triangle length: "))
numbers = []
num = 1
for i in range(1, n + 1):
    rows = []
    for j in range(i):
        rows.append(num)
        num += 1
    numbers.append(rows)

for rows in numbers:
    for num in rows:
        print(num, end=" ")
    print()

print("Task 2: \n")
n = int(input("Triangle length: "))
numbers = []
for i in range(1, n + 1):
    rows = []
    for j in range(1, i + 1):
        rows.append(j)
    for j in range(i - 1, 0, - 1):
        rows.append(j)
    numbers.append(rows)
for rows in numbers:
    print(" ".join(map(str, rows)))

print("Task 3: ")
a = int(input("Type first number: "))
b = int(input("Type second number: "))
if a >= b:
    print("First number must always be less than the second!")
else:
    max_number = b
    max_div_sum = 1
    for i in range(a, b + 1):
        div_sum = 1
        for j in range(2, int(i**0.5) + 1):
            if j % i == 0:
                div_sum += j
            if j != i // j:
                div_sum += j
        if div_sum > max_div_sum:
            max_number = i
            max_div_sum = div_sum
    print(f"The number with biggest sum of divisors in this range is {max_number} with a sum of {max_div_sum} divisors")
