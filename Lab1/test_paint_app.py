import unittest
import os
import json
from shapes import Circle, Rectangle, Triangle
from canvas import Canvas

class TestShapes(unittest.TestCase):
    def test_circle_creation(self):
        c = Circle(10, 5, 3)
        self.assertEqual(c.x, 10)
        self.assertEqual(c.y, 5)
        self.assertEqual(c.radius, 3)
        self.assertEqual(c.width, 6)
        self.assertEqual(c.height, 6)
        self.assertEqual(c.symbol, "@")

    def test_rectangle_creation(self):
        r = Rectangle(4, 3, 6, 2)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.symbol, "#")

    def test_triangle_creation(self):
        t = Triangle(1, 1, 4)
        self.assertEqual(t.x, 1)
        self.assertEqual(t.y, 1)
        self.assertEqual(t.height, 4)
        self.assertEqual(t.symbol, "*")

    def test_move_shape(self):
        r = Rectangle(0, 0, 3, 3)
        r.move(5, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)


class TestCanvas(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(20, 10)

    def test_add_shape(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.assertIn(r, self.canvas.shapes)

    def test_erase_shape(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.erase_shape(r)
        self.assertNotIn(r, self.canvas.shapes)

    def test_move_shape(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.move_shape(r, 5, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_undo_add(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.undo()
        self.assertNotIn(r, self.canvas.shapes)

    def test_undo_erase(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.erase_shape(r)
        self.canvas.undo()
        self.assertIn(r, self.canvas.shapes)

    def test_undo_move(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.move_shape(r, 5, 5)
        self.canvas.undo()
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_redo_add(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.undo()
        self.canvas.redo()
        self.assertIn(r, self.canvas.shapes)

    def test_redo_erase(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.erase_shape(r)
        self.canvas.undo()
        self.canvas.redo()
        self.assertNotIn(r, self.canvas.shapes)

    def test_redo_move(self):
        r = Rectangle(1, 1, 2, 2)
        self.canvas.add_shape(r)
        self.canvas.move_shape(r, 5, 5)
        self.canvas.undo()
        self.canvas.redo()
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_save_and_load(self):
        r = Rectangle(2, 2, 3, 3)
        self.canvas.add_shape(r)
        self.canvas.save_to_file("test_canvas.json")

        new_canvas = Canvas()
        new_canvas.load_from_file("test_canvas.json")

        self.assertEqual(len(new_canvas.shapes), 1)
        loaded_shape = new_canvas.shapes[0]
        self.assertEqual(loaded_shape.x, 2)
        self.assertEqual(loaded_shape.y, 2)
        self.assertEqual(loaded_shape.width, 3)
        self.assertEqual(loaded_shape.height, 3)

        os.remove("test_canvas.json")  # clean up

    def test_save_file_exists(self):
        r = Circle(5, 5, 3)
        self.canvas.add_shape(r)
        self.canvas.save_to_file("canvas_test.json")
        self.assertTrue(os.path.exists("canvas_test.json"))
        os.remove("canvas_test.json")

    def test_clear_shapes_on_load(self):
        r1 = Circle(1, 1, 2)
        r2 = Rectangle(2, 2, 3, 3)
        self.canvas.add_shape(r1)
        self.canvas.save_to_file("temp.json")

        self.canvas.add_shape(r2)
        self.canvas.load_from_file("temp.json")

        self.assertEqual(len(self.canvas.shapes), 1)  # only r1 should remain
        os.remove("temp.json")


if __name__ == "__main__":
    unittest.main()
