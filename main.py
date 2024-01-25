def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def main():
    row = input("Enter a string: ")
    if is_palindrome(row):
        print(f"{row} is a palindrome!")
    else:
        print(f"No, {row} not a palindrome.")


if __name__ == "__main__":
    main()

print("\n Task 2: ")
def find_and_replace(text, reserved_words):
    for word in reserved_words:
        text = text.replace(word, word.upper())
    return text

def main():
    text = input("Enter some text: ")
    reserved_words = input("Enter a list of reserved words separated by spaces: ")
    reserved_words = reserved_words.split()

    modified_text = find_and_replace(text, reserved_words)
    print(modified_text)

if __name__ == "__main__":
    main()

print("\n Task 3: ")
text = input("Enter some text: ")
sentence_end = "." or "?" or "!"
count = 0
for elem in text:
    if elem == sentence_end:
        count += 1

print(f"\n There are {count} sentences in the text ")
