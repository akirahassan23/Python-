
numbers = [10, 20, 5, 40, 30]

avg = sum(numbers) / len(numbers)

print("Average =", avg)

print("Elements greater than average:")
for n in numbers:
    if n > avg:
        print(n)
        