# Selection Sort


arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):

    min_index = i

    for j in range(i + 1, len(arr)):

        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

    print("Pass", i + 1, ":", arr)

print("Sorted list:", arr)

