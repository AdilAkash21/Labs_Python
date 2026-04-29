# Find the blank space, cut the first name, cut the last name, glue them with a comma.

s = "Adil Akash"
end = s.find(' ')

first = s[:end]
last = s[end+1:]

result = last + ", " + first
print(result)

# end = s.find(' ')

s = "Adil Akash"
end = s.find(' ')
print(end)


# If the number is below 1000, solve it directly. Otherwise split into thousands and remainder.

n = 3456

if n < 1000:
    print("Direct:", n)
else:
    thousands = n // 1000
    remainder = n % 1000
    print("Thousands:", thousands)
    print("Remainder:", remainder)

# return s[:end] 

def get_first_name(s):
    end = s.find(' ')
    return s[:end]

print(get_first_name("Adil Akash"))

