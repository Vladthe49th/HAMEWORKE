print("Task 1: ")
def line_draw(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for _ in range(length):
            print(symbol)

line_draw(length=int(input("Length: ")), direction=input("Vertical or horizontal?: "), symbol=input("line symbol: "))

print("Task 2: ")

def max_number(a,b,c,d):
    max_num = max(a, b, c, d)
    print(max_num)
first = int(input("First num: "))
second = int(input("Second num: "))
third = int(input("Third num: "))
fourth = int(input("Fourth num: "))
max_number(first, second, third, fourth)

print("Task 3: ")
def sum_nums(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    print(sum)
first = int(input("range start: "))
second = int(input("range end: "))
sum_nums(first, second)

print("Task 4: ")

def simple_num(a):
    if a <= 1:
        print(False)
    elif a % 2 == 0 or a % 3 == 0:
        print(False)
    else:
        print(True)

a = int(input("Type a number: "))
simple_num(a)

print("Task 5: ")

def happy_num(a):
    first_half = a // 1000
    second_half = a % 1000


    sum_first_half = sum(map(int, str(first_half)))
    sum_second_half = sum(map(int, str(second_half)))


    if sum_first_half == sum_second_half:
        print(True)
    else:
        print(False)


a = int(input("Type six-digit num: "))
happy_num(a)