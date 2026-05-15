# Majority Element (Loop Only)


nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]

majority = None

for i in range(len(nums)):

    count = 0

    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1

    if count > len(nums) // 2:
        majority = nums[i]
        break

print(majority)