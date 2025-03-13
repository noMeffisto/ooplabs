class Shape:
    def __init__(self, x, y, width, height, symbol):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.symbol = symbol

    def draw(self, canvas):
        pass

    def move(self, x, y):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, x, y, radius):
        width = height = radius * 2
        super().__init__(x, y, width, height, symbol="@")
        self.radius = radius

    def draw(self, canvas):
        for i in range(self.y, self.y + self.height):
            for j in range(self.x, self.x + self.width):
                if (i - self.y - self.radius) ** 2 + (j - self.x - self.radius) ** 2 <= self.radius ** 2:
                    if 0 <= i < len(canvas) and 0 <= j < len(canvas[i]):
                        canvas[i][j] = self.symbol

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, symbol="#")

    def draw(self, canvas):
        for i in range(self.y, self.y + self.height):
            for j in range(self.x, self.x + self.width):
                if 0 <= i < len(canvas) and 0 <= j < len(canvas[i]):
                    canvas[i][j] = self.symbol

class Triangle(Shape):
    def __init__(self, x, y, height):
        super().__init__(x, y, height, height, symbol="*")
        self.height = height

    def draw(self, canvas):
        for i in range(self.height):
            for j in range(i + 1):
                cx, cy = self.x + j, self.y + i
                if 0 <= cy < len(canvas) and 0 <= cx < len(canvas[cy]):
                    canvas[cy][cx] = self.symbol