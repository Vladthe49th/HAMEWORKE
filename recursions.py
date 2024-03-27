# def my_reverse(s):
#     if s == "":
#         return s
#     if len(s) == 1:
#         return s
#     if len(s) == 2:
#         return s[1] + s[0]
#     return my_reverse(s[1:]) + s[0]
# print(my_reverse(""))
# print(my_reverse("1"))
# print(my_reverse("12"))
# print(my_reverse("Hello!"))


# def my_pow(x, y):
#     if y == 0:
#         return 1
#     if y == 1:
#         return x
#     if y == 2:
#         return x * x
#     return x * my_pow(x, y - 1)
# print(my_pow(2, 5))



try:
    a = 5
    b = int(input('B '))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("ZeroDivisonError")


    def func():
        return 55
    func()
except ValueError:
    print("None")
else:
    print("ELSE")
finally:
    print("Finally")