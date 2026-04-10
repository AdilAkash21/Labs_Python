text = input("Enter a sentence: ")
letters_only = ""

# Add only alphabet letters to letters_only
for ch in text:
    if ch.isalpha():
        letters_only += ch

print("Result:", letters_only)