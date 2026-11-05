class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def add(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)
    
    def scale(self,k):
        return Vector2D(self.x*k, self.y*k)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle_to(self, other):
        length = self.length() * other.length()

        if length == 0:
            return ValueError("Угол с нулевым вектором не определён")

        cosine = self.dot(other) / length
        cosine = max(-1, min(1, cosine))

        x = ((1 - abs(cosine)) / 2) ** 0.5

        term = x
        angle = x

        for n in range(1, 30):
            term *= (2 * n - 1) ** 2 * x ** 2 / (2 * n * (2 * n + 1))
            angle += term

        degrees = 2 * angle * 180 / 3.14

        if cosine < 0:
            return 180 - degrees

        return degrees
    def __str__(self):
        return f"({self.x}, {self.y})"
u = Vector2D(3, 4)
v = Vector2D(1, 0)
print(u, u.length())                   
print(u.add(v))                         
print(v.angle_to(Vector2D(0, 1)))