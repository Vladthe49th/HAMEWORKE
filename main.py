print("Task 1: ")
def multiply(lst: list):
    result = 1
    for num in lst:
        result *= num
    return result

def get_list():
    user_input = input("Enter elements of the list using space bar: ")
    elems = user_input.split()
    int_elements = [int(elem) for elem in elems]
    return int_elements

user_list = get_list()
result = multiply(user_list)
print("Multiplication of list elements is", result)


print("Task 2: ")
def get_min(lst: list):
    minimal = min(lst)
    return minimal

def get_list():
    user_input = input("Enter list elements: ")
    elems = user_input.split()
    int_elements = [int(elem) for elem in elems]
    return int_elements

user_list = get_list()
result = get_min(user_list)
print("List minimal is", result)


print("Task 3: ")

def prime_num(num: int):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_user_list():
    user_input = input("Enter list elements: ")
    numbers = [int(num) for num in user_input.split()]
    count = 0
    for num in numbers:
        if prime_num(num):
            count += 1
    return count

result = count_primes_in_user_list()
print("Count of prime numbers in the list is", result )

print("Task 4: ")
def delete_elem(lst: list, num: int):
    delete_count = 0
    while num in lst:
        lst.remove(num)
        delete_count += 1
    return delete_count

def get_list():
    user_input = input("Enter list elements: ")
    elems = user_input.split()
    int_elements = [int(elem) for elem in elems]
    return int_elements

user_list = get_list()
delete_num = int(input("Type a number from the list you want to delete: "))
deleted = delete_elem(user_list, delete_num)
print("List after deletion is ", user_list)

print("Task 5: ")

def append_lists(lst1: list, lst2:list):
    aligned_list = []
    for elem in lst1:
        aligned_list.append(elem)
    for elem in lst2:
        aligned_list.append(elem)
    return aligned_list

def get_list():
    user_input = input("Enter first list elements: ")
    elems = user_input.split()
    int_elements = [int(elem) for elem in elems]
    return int_elements

def get_list2():
    user_input2 = input("Enter second list elements: ")
    elems2 = user_input2.split()
    int_elements2 = [int(elem) for elem in elems2]
    return int_elements2

user_list1 = get_list()
user_list2 = get_list2()
result = append_lists(user_list1, user_list2)
print("Aligned list is", result)

print("Task 6: ")

def power_calculation(lst: list, power: int):
    return [num ** power for num in lst]

def get_list():
    user_input = input("Enter list elements: ")
    elems = user_input.split()
    int_elements = [int(elem) for elem in elems]
    return int_elements
user_list = get_list()
power = int(input("Type power in which numbers must appear: "))
result = power_calculation(user_list, power)
print("List in desired power is", result)


