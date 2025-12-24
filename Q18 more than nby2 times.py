nums = [2, 2, 1, 2, 3, 2, 2]

n = len(nums)

for x in nums:
    if nums.count(x) > n // 2:
        print("Majority element:", x)
        break