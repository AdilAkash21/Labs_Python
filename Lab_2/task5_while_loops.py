password = input("Enter a password: ")

has_digit = False
has_letter = False

# Use a for loop to check each character
# Update has_digit and has_letter
for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isalpha():
        has_letter = True

# Then use an if statement to print the final result
if len(password) >= 8 and has_digit and has_letter:
    print("Valid password")
else:
    print("Invalid password")
    
# The password is valid if it has at least 8 characters, contains at least one digit, and at least one letter.