from canvas import Canvas
from shapes import Circle, Rectangle, Triangle

class PaintApp:
    def __init__(self):
        self.canvas = Canvas()

    def input_int(self, prompt, min_val, max_val):
        while True:
            try:
                value = int(input(f"{prompt} ({min_val}-{max_val}): "))
                if min_val <= value <= max_val:
                    return value
                print(f"Value must be between {min_val}-{max_val}!")
            except ValueError:
                print("Enter a valid number!")

    def input_shape(self, prompt):
        if not self.canvas.shapes:
            print("No shapes to select!")
            return None
        print("\nSelect a shape by number:")
        for i, shape in enumerate(self.canvas.shapes, 1):
            print(f"{i}. {shape.__class__.__name__} at ({shape.x}, {shape.y})")
        choice = self.input_int(prompt, 1, len(self.canvas.shapes))
        return self.canvas.shapes[choice - 1]

    def run(self):
        while True:
            self.canvas.show()
            print("\n1. Draw Circle")
            print("2. Draw Rectangle")
            print("3. Draw Triangle")
            print("4. Move Object")
            print("5. Erase Object")
            print("6. Undo")
            print("7. Redo")
            print("8. Save Canvas")
            print("9. Load Canvas")
            print("0. Exit")
            choice = input("Choice: ")

            if choice == "1":
                x = self.input_int("X", 1, 49)
                y = self.input_int("Y", 1, 29)
                radius = self.input_int("Radius", 1, 10)
                self.canvas.add_shape(Circle(x, y, radius))
            elif choice == "2":
                x = self.input_int("X", 1, 49)
                y = self.input_int("Y", 1, 29)
                w = self.input_int("Width", 1, 20)
                h = self.input_int("Height", 1, 10)
                self.canvas.add_shape(Rectangle(x, y, w, h))
            elif choice == "3":
                x = self.input_int("X", 1, 49)
                y = self.input_int("Y", 1, 29)
                side_a = self.input_int("Base length (side_a)", 1, 20)
                side_b = self.input_int("Left side (side_b)", 1, 20)
                side_c = self.input_int("Right side (side_c)", 1, 20)
                if (side_a + side_b <= side_c) or (side_b + side_c <= side_a) or (side_a + side_c <= side_b):
                    print("These sides cannot form a triangle!")
                else:
                    self.canvas.add_shape(Triangle(x, y, side_a, side_b, side_c))
            elif choice == "4":
                shape = self.input_shape("Move which shape?")
                if shape:
                    x = self.input_int("New X", 1, 45)
                    y = self.input_int("New Y", 1, 25)
                    self.canvas.move_shape(shape, x, y)
            elif choice == "5":
                shape = self.input_shape("Erase which shape?")
                if shape:
                    self.canvas.erase_shape(shape)
            elif choice == "6":
                self.canvas.undo()
            elif choice == "7":
                self.canvas.redo()
            elif choice == "8":
                self.canvas.save_to_file()
            elif choice == "9":
                self.canvas.load_from_file()
            elif choice == "0":
                break
            else:
                print("Invalid choice! Please select a number from 0 to 9.")

if __name__ == "__main__":
    app = PaintApp()
    app.run()