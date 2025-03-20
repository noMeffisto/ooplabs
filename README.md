Конечно! Вот текст функциональных требований в виде, который легко скопировать. Я убрал лишние отступы и форматирование Markdown, чтобы ты мог просто выделить и скопировать его целиком.

Functional Requirements

The program must be able to draw 3 types of figures: circle, rectangle, triangle; erase, move them, and save/load the canvas. All figures are drawn using ASCII characters on a fixed-size canvas (50x30 by default).

Warning: All numeric input values must be integers. If invalid input is provided (e.g., non-integer values or values outside acceptable ranges), an error message will be displayed on the screen.

Objects may be displayed with altered proportions due to the peculiarities of console output and the discrete nature of the grid.

Menu
0 - Exit: Exit the program without saving the current canvas state.
1 - Draw Shape:
1 - Circle: Draw a circle with a specified radius.
2 - Rectangle: Draw a rectangle with specified width and height.
3 - Triangle: Draw a triangle with specified base and side lengths, filled inside with a contour.
2 - Move Object: Move a selected shape to new coordinates.
3 - Erase Object: Remove a selected shape from the canvas.
4 - Undo Last Action: Revert the last modification (add, move, or erase).
5 - Redo Last Undone Action: Restore the most recently undone action.
6 - Save Canvas to File: Save the current canvas state to a file.
7 - Load Canvas from File: Load a previously saved canvas state.

Drawing
The coordinate system for figures starts from the upper-left corner of the canvas (X=0, Y=0), extending right (increasing X) and downward (increasing Y). Figures must be drawn within the canvas boundaries (X: 0-49, Y: 0-29), and input values are constrained (e.g., X: 1-45, Y: 1-25) to ensure visibility.

To draw, choose a type (1, 2, 3) and then enter:
For a Circle:
x, y, radius (integers).
(x, y) - coordinates of the top-left corner of the bounding box containing the circle.
radius - radius of the circle (defines width and height as 2 * radius).
Drawn using the symbol @, filled inside the circular boundary.
For a Rectangle:
x, y, width, height (integers).
(x, y) - coordinates of the top-left corner.
width, height - dimensions of the rectangle.
Drawn using the symbol #, filled completely.
For a Triangle:
x, y, side_a, side_b, side_c (integers).
(x, y) - coordinates of the top vertex (apex) of the triangle.
side_a - length of the base (bottom side).
side_b, side_c - lengths of the left and right sides, respectively.
Height is calculated using Heron's formula based on the three sides.
Drawn using the symbol *, with the apex at (x + side_a // 2, y) and the base at y + height, filled inside with a visible contour along all three sides.

Selecting and Moving Objects
To move an object, select it from a numbered list of shapes displayed on the screen, then enter new coordinates:
For a Circle:
x, y - new coordinates of the top-left corner of the bounding box.
For a Rectangle:
x, y - new coordinates of the top-left corner.
For a Triangle:
x, y - new coordinates of the top vertex (apex).
The vertices are recalculated relative to the new (x, y) position.

Erasing Objects
Select an object from the numbered list of shapes to erase it from the canvas. If no shapes exist, a message will indicate this.

Saving the Canvas
The canvas state (list of shapes with their properties) is saved to a file named canvas.json in JSON format. Each shape’s type, coordinates, dimensions, and symbol are stored.

Loading the Canvas
Load a previously saved canvas from canvas.json. If the file does not exist, an error message is displayed. Loading replaces the current canvas with the saved state.

Undo/Redo Actions
Undo: Reverts the last modification (adding, moving, or erasing a shape).
Adding a shape: Removes it.
Erasing a shape: Restores it.
Moving a shape: Returns it to its previous position.
Redo: Restores the most recently undone action.
If a new action is performed after undoing, the redo history is cleared.
If there are no actions to undo or redo, the canvas remains unchanged.
