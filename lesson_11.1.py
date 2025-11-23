def generate_cube_numbers(end):
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            return
        yield cube
        n += 1          
