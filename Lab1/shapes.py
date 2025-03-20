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
    def __init__(self, x, y, side_a, side_b, side_c):
        self.side_a = side_a  # основание
        self.side_b = side_b  # левая сторона
        self.side_c = side_c  # правая сторона
        # Полупериметр и площадь для вычисления высоты
        s = (side_a + side_b + side_c) / 2
        area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
        height = int(2 * area / side_a)  # высота треугольника
        width = side_a  # ширина равна основанию
        super().__init__(x, y, width, height, symbol="*")
        # Переворачиваем координаты: вершина сверху, основание снизу
        self.vertices = [
            (x + side_a // 2, y),         # верхняя вершина (смещена к центру основания)
            (x, y + height),              # левая вершина основания
            (x + side_a, y + height)      # правая вершина основания
        ]

    def _draw_line(self, canvas, x0, y0, x1, y1):
        """Алгоритм Брезенхема для рисования линии"""
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        points = []
        while True:
            if 0 <= y0 < len(canvas) and 0 <= x0 < len(canvas[y0]):
                points.append((x0, y0))
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        return points

    def draw(self, canvas):
        """Рисуем треугольник с контуром и заливкой"""
        v0, v1, v2 = self.vertices

        # 1. Рисуем контур (три линии)
        edges = []
        edges.extend(self._draw_line(canvas, v0[0], v0[1], v1[0], v1[1]))  # верх -> левая
        edges.extend(self._draw_line(canvas, v0[0], v0[1], v2[0], v2[1]))  # верх -> правая
        edges.extend(self._draw_line(canvas, v1[0], v1[1], v2[0], v2[1]))  # левая -> правая

        for x, y in edges:
            if 0 <= y < len(canvas) and 0 <= x < len(canvas[y]):
                canvas[y][x] = self.symbol

        # 2. Заливка внутри треугольника
        min_y = min(v0[1], v1[1], v2[1])
        max_y = max(v0[1], v1[1], v2[1])
        min_x = min(v0[0], v1[0], v2[0])
        max_x = max(v0[0], v1[0], v2[0])

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if self._is_point_inside(x, y, v0, v1, v2):
                    if 0 <= y < len(canvas) and 0 <= x < len(canvas[y]):
                        canvas[y][x] = self.symbol

    def _is_point_inside(self, x, y, v0, v1, v2):
        """Проверка, находится ли точка внутри треугольника (барицентрические координаты)"""
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

        d1 = sign((x, y), v0, v1)
        d2 = sign((x, y), v1, v2)
        d3 = sign((x, y), v2, v0)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)

    def move(self, x, y):
        """Перемещаем треугольник, обновляя координаты вершин"""
        dx = x - self.x
        dy = y - self.y
        self.x = x
        self.y = y
        self.vertices = [
            (v[0] + dx, v[1] + dy) for v in self.vertices
        ]