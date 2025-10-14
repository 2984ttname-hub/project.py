numbers = [0, 1, 0, 12, 3]
not_zero = [number for number in numbers if number != 0]
zero_count = numbers.count(0)
result = not_zero + [0] * zero_count
print(result)
