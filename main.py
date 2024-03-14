print("Task 1: ")
with open("info.txt", "r") as file:
    res1 = file.readlines()

with open("info2.txt", "r") as file:
    res2 = file.readlines()
print("Different strings found in both files!")
for str1, str2 in zip(res1, res2):
    if str1 == str2:
        res1.remove(str1)
        res2.remove(str2)
    elif str1 != str2:
        print(f"File 1 - {str1.strip()}")
        print(f"File 2 - {str2.strip()}")


print("Task 2: ")
with open("info.txt", "r") as file:
    result = file.read()
char_count = len(result)
line_count = result.count("\n") + 1
vowels = "euioa"
consonants = "qwrtypsdfghjklzxcvbnm"
vowel_count = sum(result.count(char) for char in vowels)
consonant_count = sum(result.count(char) for char in consonants)
digit_count = sum(char.isdigit() for char in result)
print("Character count: ", char_count)
print("Line count: ", line_count)
print("Vowels count: ", vowel_count)
print("Consonant count: ", consonant_count)
print("Digit count: ", digit_count)


print("Task 3: ")
with open("info.txt", "r") as file:
    result = file.readlines()
with open("info3.txt", "w") as file:
    res2 = file.writelines(result[:-1])
print("Last line successfully deleted in the third file!")



print("Task 4: ")
with open("info.txt", "r") as file:
    line_lengths = [len(line.strip()) for line in file]
    max_length = max(line_lengths)
    print("longest line length is: ", max_length)


print("Task 5: ")
search_word = input("Type a word to search: ")
with open("info.txt", "r") as file:
    result = file.read()
count = result.lower().count(search_word.lower())
print(f"The word {search_word} occurs {count} times")

print("Task 6: ")
find_word = input("Type a word to find: ")
replace_word = input("Type a replacement word: ")
with open("info.txt", "r") as file:
    result = file.read()
new_result = result.replace(find_word, replace_word)
with open("info3.txt", "w") as file:
    file.write(new_result)
print("Word successfully replaced in third file!")



print("Task 7: ")

from tkinter import *

W = 400
H = 600

root = Tk()
root.geometry(f"{W}x{H}")
root.resizable(False, False)
background = Frame(root, bg="yellow")
background.grid()

for i in range(3):
    for j in range(6):
        cell = Frame(background, bg="blue", width=W/3, height=H/6)
        cell.grid(row=i, column= j, padx=5, pady= 10)

mainloop()