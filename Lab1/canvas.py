import os
import json
from shapes import Circle, Rectangle, Triangle

class Canvas:
    def __init__(self, width=50, height=30):
        self.shapes = []
        self.width = width
        self.height = height
        self.history = []
        self.redo_stack = []

    def add_shape(self, shape):
        self.shapes.append(shape)
        self.history.append(("add", shape))
        self.redo_stack.clear()

    def erase_shape(self, shape):
        if shape in self.shapes:
            self.shapes.remove(shape)
            self.history.append(("erase", shape))
            self.redo_stack.clear()

    def move_shape(self, shape, x, y):
        if shape in self.shapes:
            old_x, old_y = shape.x, shape.y
            shape.move(x, y)
            self.history.append(("move", shape, old_x, old_y))
            self.redo_stack.clear()

    def undo(self):
        if self.history:
            action = self.history.pop()
            if action[0] == "add":
                self.shapes.remove(action[1])
            elif action[0] == "erase":
                self.shapes.append(action[1])
            elif action[0] == "move":
                shape, old_x, old_y = action[1], action[2], action[3]
                shape.move(old_x, old_y)
            self.redo_stack.append(action)

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            if action[0] == "add":
                self.shapes.append(action[1])
            elif action[0] == "erase":
                self.shapes.remove(action[1])
            elif action[0] == "move":
                shape, new_x, new_y = action[1], action[2], action[3]
                shape.move(new_x, new_y)
            self.history.append(action)

    def save_to_file(self, filename="canvas.json"):
        data = []
        for shape in self.shapes:
            shape_data = {
                "type": shape.__class__.__name__,
                "x": shape.x,
                "y": shape.y,
                "symbol": shape.symbol
            }
            if isinstance(shape, Circle):
                shape_data["radius"] = shape.radius
            elif isinstance(shape, Rectangle):
                shape_data["width"] = shape.width
                shape_data["height"] = shape.height
            elif isinstance(shape, Triangle):
                shape_data["side_a"] = shape.side_a
                shape_data["side_b"] = shape.side_b
                shape_data["side_c"] = shape.side_c
            data.append(shape_data)
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Canvas saved successfully!")

    def load_from_file(self, filename="canvas.json"):
        if not os.path.exists(filename):
            print("No saved canvas found.")
            return
        with open(filename, "r") as f:
            data = json.load(f)
        self.shapes.clear()
        for item in data:
            if item["type"] == "Circle":
                shape = Circle(item["x"], item["y"], item["radius"])
            elif item["type"] == "Rectangle":
                shape = Rectangle(item["x"], item["y"], item["width"], item["height"])
            elif item["type"] == "Triangle":
                shape = Triangle(item["x"], item["y"], item["side_a"], item["side_b"], item["side_c"])
            else:
                continue
        self.shapes.append(shape)
        print("Canvas loaded successfully!")

    def show(self):
        canvas = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for shape in self.shapes:
            shape.draw(canvas)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nCanvas:")
        print("-" * (self.width + 2))
        for row in canvas:
            print("|" + "".join(row) + "|")
        print("-" * (self.width + 2))