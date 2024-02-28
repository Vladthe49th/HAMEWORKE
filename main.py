# document = open("consequence.txt", "a", encoding="utf-8")
# document.write("Python and HTML\n")
# document.close()

# document = open("consequence.txt", "r", encoding="utf-8")
# for i in document.readline():
#     print(i, end=" ")
# document.close()
# import pickle

# with open("good.txt", "ab") as file:
#     pickle.dump(info, file)
#
# with open("good.txt", "rb") as file:
#     print(pickle.load(file))

# info = {"name": "Vlad", "age": "16"}
# with open("product.txt", "ab") as file:
#       pickle.dump(info, file)
#
# with open("product.txt", "rb") as file:
#     for i in pickle.load(file).items()



# import re
#
with open("re.txt") as file:
    file_data = file.read()
# print(file_data)
#
# look = r"(?![<td>])[\w.-_]+@(?!aol\.couk)(?!outlook\.couk)(?!yahoo\.org)[\w.]+"
#
# result = re.findall(look, file_data)
# print(result)
# print(len(result))

# data = "Під час Другої світової війни, у 1941—1944 роках, перебувало під окупацією Румунії. Від 1991 року — у складі незалежної України."
#
# look = r"[(\b\w+][0-9]+"
# result = re.findall(look, data)
# print(result)

# def elem_sum(q, w):
#     print(id(q), id(w))
#     c = q + w
#     return c
#
# a = 5
# b = 7
# print(id(a), id(b))
# print(elem_sum(a, b))

def odd_elem(q, w):
    for i in range(q, w+1):
        if not i % 2:
            print(i, end=" ")

a = 5
b = 17
odd_elem(a, b)
