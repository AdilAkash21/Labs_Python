
s = "Walter White (Heisenberg)"

space_index = s.find(' ')   # (1) find the blank space
first_name = s[:space_index]  # (2) cut out the first name

print(space_index)
print(first_name)