text = input("Enter a short sentence: ")
count = 0

# Check each character one by one
# Count: a, e, i, o, u (both lower and upper case)
for ch in text:
    if ch in 'aeiouAEIOU':
        count += 1

print("Number of vowels:", count)