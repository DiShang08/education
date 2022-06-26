def only_one_positive(*nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    return count == 1


print(only_one_positive(1, 3))
