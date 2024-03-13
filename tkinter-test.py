# with open("info", 'r', encoding="utf-8") as file:
#     result = file.read()
#
# print(result)
#
# for i in [".", ",", "!"]:
#     if i in result:
#         result = result.replace(f"{i}", "")
# print(result)
# temp = result.split()
# print(temp)
# res = " ".join([elem for elem in temp if len(elem) >= 7])
# print(res)
# # res = " ".join(new)
# # print(res)
# with open("info 2", "w", encoding="utf-8") as file:
#     file.write(res)

# with open("info", "r", encoding="utf-8") as file:
#     result = file.readlines()
# print(result)
# new = [i.replace("\n", "") for i in result]
# with open("info 2", "a", encoding="utf-8") as file:
#     for i in range(len(result)-1, -1, -1):
#         file.write(f"{result[i]}\n")

# with open("info", "r", encoding="utf-8") as file:
#     result = file.readlines()
# print(result)
# new = [i.replace("\n", "") for i in result]
# print(new)
# for line in range(len(new)):
#     if ',' in new[i]:
#         new.insert(i+1, ("*"*12))
#     else:
#         new.append("*"*12)
#     with open("info 2", "a", encoding="utf-8") as file:
#         for i in range(len(new)):
#             file.write(f"{new[i]}\n")

# def get_data()->list[str]:
#     with open("info", "r", encoding="utf-8") as file:
#         result = file.read()
#     temp = result.split()
#     return temp
# def counter_letter(temp: list[str], letter: str)->int:
#     count = 0
#     for elem in temp:
#         if elem.lower()[0] == letter.lower():
#             count += 1
#     return count
# print(counter_letter(get_data(), "d"))



# from tkinter import *

# W = 400
# H = 600
#
# root = Tk()
# root.geometry(f"{W}x{H}")
# root.resizable(False, False)
# background = Frame(root, bg="yellow")
# background.grid()
#
# for i in range(3):
#     for j in range(6):
#         cell = Frame(background, bg="blue", width=W/3, height=H/6)
#         cell.grid(row=i, column= j, padx=5, pady= 10)
#
# mainloop()


with open("info", "r") as file:
    result = file.readlines()
temp = [elem.replace("\n", "") for elem in result]

with open("info", "w") as file:
    for elem in temp:
        r = elem
        file.write(f"{elem} = {eval(r)}\n")
