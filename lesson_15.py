class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height


    def __eq__(self, other):
        return self.get_square() == other.get_square()


    def __add__(self, other):
        new_area = self.get_square() + other.get_square()
        return Rectangle(new_area, 1)

    def __mul__(self, n):
        new_area = self.get_square() * n
        return Rectangle(new_area, 1)

    __rmul__ = __mul__

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


