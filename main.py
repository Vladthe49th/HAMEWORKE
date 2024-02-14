# t = tuple()
# print(type(t))
# t = (11, (2, 3, 4), 31)
# t = (11, [2, 3, 4], 31)
# t[1][2] = 201
# result = (6 + 9 * 3)
# print(type(result))
# print(t)
#
# a = 4
# b = 4
# if a == b:
#     print("Not ok")
# else:
#     print("Ok")

# st = set()
# st = {1, 1, 1, 1, 2, 2, 3}
# print(st)
# st.add(10)
# st = list(st)
# st = set(st)
# print(sorted(st))

# dc = {"key": "value"}
# dc = {(1, 2, 3): 55}
# print(dc[1, 2, 3])
# dc = {None: 0}
# print(dc[None]

# study = {'name': "Vlad", "age": 16, "phone": False, "grade": [11, 9, 13]}
# print(study['age'])
# print(len(study))
# print(list(study))
# print(list(study.keys()))
# print(list(study.values()))
# print(list(study.items()))
# study["Gender"] = "male"
# print(study)
# print(id(study))
# study['age'] = 21
# print(study)
# print(id(study))
#
# print(study['age'])
# print(study.get("age"))
# print(study.get('AGE'))
# print(study.popitem())

import requests

url = "https://api.openweathermap.org/data/2.5/weather"
TOKEN = "8cd37a85cb531687fb540b8030c7248e"
city = input("City: ")
params = {"q": city, "appid": TOKEN}

r = requests.get(url=url, params=params)
data = r.json()
# print(data)

print(data['main']["temp"])

for k, v in data.items():
    print(k, v)