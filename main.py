from random import randint


comp = randint(1, 100)
user = 0
count = 0
while user != comp:
    count += 1
    user = int(input('Введіть своє число '))
    if comp > user:
        print("Твоє число менше, введи більше")
    elif comp < user:
        print("Твоє число більше, введи менше")
else:
    print(f"Ви вгадали з {count} спроби!")
