import re
print("Task 1: ")
expresion = input("Gimme expression: ")
elements = re.findall(r'\d+|\S', expresion)

if len(elements) != 3:
    print("Something isn`t right!")
else:
 number1, operator, number2 = elements
 number1 = int(number1)
 number2 = int(number2)
 result = 0
 if operator == "+":
    result = number1 + number2
 elif operator == "-":
    result = number1 - number2
 elif operator == "*":
    result = number1 * number2
 elif operator == "/":
    result = number1 / number2
 else:
    print("This is not an expression, and I don`t know what to do, I am just a calculator, please, give me expressions Please!!")
print(result)

print("\n Task 2: ")
import random
random_list = [random.randint(-200, 200) for _ in range(20)]
print(f"List of random numbers is {random_list}")
min_num = min(random_list)
max_num = max(random_list)
odd_count = sum(1 for num in random_list if num < 0)
even_count = sum(1 for num in random_list if num > 0)
zero_count = sum(str(num).count('0') for num in random_list)
print(f"Minimum number is {min_num}")
print(f"Maximum number is {max_num}")
print(f"Count of odd numbers is {odd_count}")
print(f"Count of even numbers is {even_count}")
print(f"Count of zeros in the list is {zero_count}")


