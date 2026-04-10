text = input("Enter some text: ")

# Count characters (including spaces)
char_count = len(text)

# Count characters (excluding spaces)
char_no_spaces = len(text.replace(" ", ""))

# Count words
words = text.split()
word_count = len(words)

# Count sentences (rough estimate by counting . ! ?)
sentence_count = text.count('.') + text.count('!') + text.count('?')

print("\n--- Text Statistics ---")
print(f"Characters (with spaces): {char_count}")
print(f"Characters (no spaces): {char_no_spaces}")
print(f"Words: {word_count}")
print(f"Sentences: {sentence_count}")