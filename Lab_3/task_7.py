
def first_name_only(s):
    """Returns the first name from a two-word name."""
    end = s.find(' ')
    first = s[:end]
    return first


# Test with three names
print(first_name_only("Walter White (Heisenberg)"))
print(first_name_only("Harry Potter (The Boy who lived)"))
print(first_name_only("Tony Stark (I AM IRON MAN )"))