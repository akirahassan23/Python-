n = 3  # example: find 10th fibonacci number

a = 0  # first fibonacci number
b = 1  # second fibonacci number

# If n == 0 or n == 1, directly handle
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2, n + 1):
        c = a + b  # next number is sum of previous two
        a = b  # move b to a
        b = c  # move c to b

    print(b)