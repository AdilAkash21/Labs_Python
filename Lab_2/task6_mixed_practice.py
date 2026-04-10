word = input("Enter a word: ")

for ch in word:
    if ch in 'aeiouAEIOU':
        print(ch, "-> VOWEL")
    else:
        print(ch)