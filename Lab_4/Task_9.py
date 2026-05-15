# Three-Sum (Find Unique Triplets)


nums = [-1, 0, 1, 2, -1, -4]

found = []

for i in range(len(nums)):

    for j in range(i + 1, len(nums)):

        for k in range(j + 1, len(nums)):

            if nums[i] + nums[j] + nums[k] == 0:

                triplet = [nums[i], nums[j], nums[k]]

                # manual sort of triplet
                for x in range(3):
                    for y in range(x + 1, 3):
                        if triplet[x] > triplet[y]:
                            temp = triplet[x]
                            triplet[x] = triplet[y]
                            triplet[y] = temp

                exists = False

                for item in found:
                    if item == triplet:
                        exists = True
                        break

                if not exists:
                    found.append(triplet)

for item in found:
    print(item)
    
