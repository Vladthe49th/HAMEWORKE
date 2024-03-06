# a = ("Vlad", "Konstantin", "Andrew")
# b = ("Droid", "Plagueis")
# x = zip(a, b)
# print(list(x))
import math


# def get_even(a:int, b:int) -> list[int]:
#     """
#
#     :param a: min
#     :param b: max
#     :return: None
#     """
#     lst = [i for i in range(a, b + 1) if not i % 2]
#     return lst
#
#
# print(get_even(a=int(input("number one: ")), b=int(input("number two: "))))


# def draw_sq(length: int, sym: str, flag: bool)-> None:
#     if flag:
#         for i in range(length):
#             print(sym*length)
#     else:
#         for i in range(length):
#             for j in range(length):
#                 if i == 0 or i == length - 1 or j == 0 or j == length - 1:
#                     print(sym, end=" ")
#                 else:
#                     print(" ", end=" ")
#             print()
#
# draw_sq(length=int(input("Length: ")), sym=input("symbol"), flag=True)
# draw_sq(length=int(input("Length: ")), sym=input("symbol"), flag=False)


# def product_numbers(x, c, *, a: int, b: int) -> int:
#     if a > b:
#         a, b = b, a
#     result = 1
#     for i in range(a, b + 1):
#         result *= i
#     return result
#
#
# product_numbers(100, 0, a=int(input("First number: ")), b=int(input("Second number: ")))


# def get_min(flag = True, *args, **kwargs):
#     print(args, kwargs)
#     return flag, kwargs['name']
#
# print(get_min(True,8,7, name="Palpatine", age= 15))


# def my_max(lst: list)-> int:
#     temp = lst[0]
#     for i in lst:
#         if temp < i:
#             temp = i
#     return temp
#
# x = 10.5
# print(math.ceil(x))
# print(math.floor(x))
# print(math.modf(x))
# print(math.trunc(x))
# x = -10.5
# print(math.fabs(x))
# print(abs(x))
#
# print(math.factorial(x))
# print(math.gcd(10, 6))
# print(math.prod([1, 2, 4, 5]))
# print(math.lcm(11, 6))
#
#
# import random
#
# print(random.random())
# print(random.randint(5, 10, 2))