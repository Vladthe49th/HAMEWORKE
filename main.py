print("Picture 1: \n")
a = 10
for i in range(a):
    for j in range(a):
        if i == a or j >= i:
            print('*', end='')
        else:
            print(' ', end='')

    print()
print("\n")
print("Picture 2: \n")
a = 10
for i in range(a):
    for j in range(a):
        if i == a or j <= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print("\n")
print("Picture 3: \n")
a = 5

for i in range(a):
    spaces = " " * i
    stars = "*" * (2 * (a - i) - 1)
    print(spaces + stars)
print("\n")

print("Picture 4:")
a = 5

for i in range(a):
    spaces = " " * (a - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars + spaces)
print("\n")

print("Picture 5:")
a = 5

for i in range(a):
    spaces = " " * i
    stars = "*" * (2 * (a - i) - 1)
    print(spaces + stars)

b = 5

for i in range(b):
    bspaces = " " * (a - i - 1)
    bstars = "*" * (2 * i + 1)
    print(bspaces + bstars + bspaces)
print("\n")

print("Picture 6:")
a = 5


for i in range(1, a + 1):
    print('*' * i)


for i in range(a - 1, 0, -1):
    print('*' * i)
print("\n")

print("Picture 7:")
a = 5

for i in range(a):
    for j in range(a):
        if j >= a - i - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

for i in range(a-2, -1, -1):
    for j in range(a):
        if j >= a - i - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
print("\n")

print("Picture 8:")
a = 5

for i in range(a):
    for j in range(i + 1):
        print('*', end='')

    for k in range(2 * (a - i - 1)):
        print(' ', end='')

    for l in range(i + 1):
        print('*', end='')

    print()
for i in range(a-2, -1, -1):
    for j in range(i + 1):
        print('*', end='')
    for k in range(2*(a - i -1)):
        print(' ', end='')
    for l in range(i + 1):
        print('*', end='')
    print()
print("\n")

print("Picture 9:")
a = 10
for i in range(a):
    for j in range(a-2, -1, -1):
        if i == a or j >= i:
            print('*', end='')
        else:
            print(' ', end='')

    print()
print("\n")

print("Picture 10:")
a = 10
for i in range(a):
    for j in range(a-2, -1, -1):
        if i == a or j <= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()