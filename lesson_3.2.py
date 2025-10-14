numbers = [1, 2, 3, 4, 5]
if len(numbers) == 0:
    result = [[], []]
else:
    middle = (len(numbers) + 1) // 2
    first_part = numbers[:middle]
    second_part = numbers[middle:]
    result = [first_part, second_part]
print(result)
