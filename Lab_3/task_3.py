
def initials(name):
    # INPUT name (already given as parameter)

    # FIND the position of the space in the name
    space_index = name.find(' ')

    # TAKE the first letter from the start of the name
    first_initial = name[0]

    # TAKE the first letter after the space
    second_initial = name[space_index + 1]

    # COMBINE both letters
    result = first_initial + second_initial

    # RETURN the result
    return result


# Examples
print(initials("Adil Akash"))   # AA
print(initials("Harry Potter"))   # HP