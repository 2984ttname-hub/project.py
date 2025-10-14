numbers = [0, 1, 7, 2, 4, 8]
if not numbers:
    result = 0
else:
    even_index_sum = sum(numbers[::2])
    last_element = numbers[-1]
    result = even_index_sum * last_element
print(result)
