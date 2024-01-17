first_num = int(input("Enter first number: "))
last_num = int(input("Enter last number: "))
print("All prime numbers in range:")
for num in range(first_num, last_num + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
print("\n")

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i}*{j} = {result}", end = "\n")
print()

print("\n")

start_range = int(input("Range start: "))
end_range = int(input("Range end: "))
for i in range(start_range, end_range + 1):
    for j in range(start_range, end_range + 1):
        result = i * j
        print(f"{i}*{j} = {result}", end="\n")
print()