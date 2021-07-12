numbers = [23, 5, 89, 123, -56, 93, 24, 11, -9, 52, 685]
valid_numbers = []
for n in numbers:
    if n in range(0, 101):
        valid_numbers.append(n)
print(valid_numbers)
total = sum(valid_numbers)
print('Total: ', total)
average = (total / len(valid_numbers))
print('Average: ', average)
