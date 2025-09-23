class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
    
    def set_width(self, width):
        self._width = width
        return self
    
    def set_height(self, height):
        self._height = height
        return self
    
    def area(self):
        return self._width * self._height
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height

class Square(Rectangle):
    def __init__(self, size=0):
        super().__init__(size, size)

    def set_width(self, width):
        return Square(width)
    
    def set_height(self, height):
        return Square(height)


def rectangle_area_test(rect):
    rect = rect.set_width(20)
    rect = rect.set_height(10)
    return rect.area() == 200.0

rect = Rectangle()
square = Square()

print("Rectangle test:", rectangle_area_test(rect))
print("Square test:", rectangle_area_test(square))

print("Is square a rectangle?", isinstance(square, Rectangle))  # True