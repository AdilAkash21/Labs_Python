# Rotate a List (Without Slicing)


lst = [1, 2, 3, 4, 5]
k = 2

length = len(lst)

for i in range(k):
    last = lst[length - 1]

    for j in range(length - 1, 0, -1):
        lst[j] = lst[j - 1]

    lst[0] = last

print(lst)