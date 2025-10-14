numbers = [12, 3, 4, 10]
if len(numbers) <= 1:
    result = numbers
else:
    last = numbers[-1]
    rest = numbers[:-1]
    result = [last] + rest
print(result) 
