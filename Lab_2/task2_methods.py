word = input("Enter one word: ")
word = input("Output: " + word)

# if / elif / else code below

if len(word) < 5:
    print("Short word")
elif len(word) <= 8:
    print("Medium word")
else:
    print("Long word")