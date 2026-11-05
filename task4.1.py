class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        if self.height == self.width:
            return True
        else:
            return False

    def scale(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor

    def describe(self):
        return f"{self.width} * {self.height}, obsah {self.area()}"

    
a = Rectangle(5, 9)
b = Rectangle(10, 4)
c = Rectangle(3, 0)
print(a.describe())
print(b.describe())
print(c.describe())

rectangles = [a, b, c]

largest = rectangles[0]

for rectangle in rectangles:
    if rectangle.area() > largest.area():
        largest = rectangle

print("Прямоугольник с наибольшей площадью:")
print(largest.describe())
