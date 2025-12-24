nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

n = len(nums)
k = k % n   # make sure k is within range

# Rotate k times (right rotation)
for _ in range(k):
    last = nums[-1]            # take last element
    for i in range(n - 1, 0, -1):
        nums[i] = nums[i - 1]  # shift every element right
    nums[0] = last             # place last element at front

print(nums)