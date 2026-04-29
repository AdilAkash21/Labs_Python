
def reverse_name(s):
    """Returns a name in the form 'last, first'."""
    space_index = s.find(' ')
    first = s[:space_index]
    last = s[space_index + 1:]
    return last + ", " + first


# Take input from user
name = input("Enter your name (first last): ")

# Show result
print(reverse_name(name))


