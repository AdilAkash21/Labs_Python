
def first_name(s):
    """Returns the first name from a two-word name."""
    space_index = s.find(' ')
    return s[:space_index]


def first_initial(s):
    """Returns the first initial of a two-word name."""
    return first_name(s)[0]


# Test
print(first_name("Harry Potter"))    # Harry
print(first_initial("Harry Potter")) # H