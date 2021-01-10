import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload operators
    def __repr__(self):
        return self

    def __str__(self):
        return "Vector" + str((self.x, self.y))

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other):
        if other != 0:
            return Vector2D(self.x / other, self.y / other)
        else:
            return self

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __lt__(self, other):
        return self.length() < other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def get_angle(self):
        result = math.asin(self.sin())
        if(self.cos() < 0):
            result = math.pi - result
        return result

    def set_angle(self, angle):
        length = self.length()

        self.x = length * math.cos(angle)
        self.y = length * math.sin(angle)

    def length(self):
        return math.hypot(self.x , self.y)
    
    def normalized(self):
        return self/self.length()

    def sin(self):
        if self.length() == 0:
            return 0

        return self.y / self.length()

    def cos(self):
        if self.length() == 0:
            return 0

        return self.x / self.length()

    # Static functions
    @staticmethod
    def minimal(vector1, vector2):
        if vector1 < vector2:
            return vector1
        else:
            return vector2

    @staticmethod
    def maximal(vector1, vector2):
        if vector1 > vector2:
            return vector1
        else:
            return vector2

    @staticmethod
    def distance(vector1, vector2):
        return (vector2-vector2).length()

    @staticmethod
    def perpendicular(vector):
        return Vector2D(-vector.sin(), vector.cos())

    @staticmethod
    def list(vector):
        return [vector.x, vector.y]