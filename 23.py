
numbers = [10, 25, 5, 30, 15]

avg = sum(numbers) / len(numbers)

greater_than_avg = [x for x in numbers if x > avg]

print("Average:", avg)
print("Elements greater than average:", greater_than_avg)
