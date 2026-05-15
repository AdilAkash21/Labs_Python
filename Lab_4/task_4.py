# Longest Consecutive Increasing Subsequence


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

max_length = 1
current_length = 1

start = 0
best_start = 0

for i in range(1, len(nums)):

    if nums[i] > nums[i - 1]:
        current_length += 1
    else:
        current_length = 1
        start = i

    if current_length > max_length:
        max_length = current_length
        best_start = start

sublist = []

for i in range(best_start, best_start + max_length):
    sublist.append(nums[i])

print("Length =", max_length)
print("Sublist =", sublist)

