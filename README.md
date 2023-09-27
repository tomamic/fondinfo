## Programming lab @ UniPR

http://tomamic.github.io

Python and C++ examples

Copyleft (ɔ) 2008-2020 Michele Tomaiuolo - http://sowide.unipr.it/tomamic <br>
This software is free - License: http://www.gnu.org/licenses/gpl-3.0.txt

---

## g2d

### Installing

- Copy `g2d.py` into the same folder containing your scripts; this will draw into a *PyGame window*
- Alternatively, copy `g2d_pyodide.py` in that location and rename the file as `g2d.py`; this will draw into a *browser window*

### Basic structs

- A `Color` is a tuple `(red, green, blue)`; each value must be in the range `0..255`
- A `Point` is a tuple `(x, y)`, representing a *position* or a *size*

### Canvas functions

- **`init_canvas`** `(size: Point)` : Initialize the drawing canvas
- **`main_loop`** `(tick=None, fps=30)` : Start the event loop, accepting an optional `tick` function, which will be called periodically
- **`clear_canvas`** `()` : Clear the canvas
- **`close_canvas`** `()` : Close the canvas and exit the main loop

### Drawing functions

- **`set_color`** `(color: Color)` : Set the drawing color
- **`draw_line`** `(pt1: Point, pt2: Point)` : Draw a line from `pt1` to `pt2`
- **`draw_circle`** `(center: Point, radius: int)` : Fill a circle, given `center` and `radius`
- **`draw_rect`** `(pos: Point, size: Point)` : Fill a given rectangle, given left-top position and size
- **`draw_polygon`** `(points: list[Point])` : Fill a polygon, given its list of vertices
- **`draw_text`** `(txt: str, pos: Point, size: int)` : Draw a text, given left-top position and font px size
- **`draw_text_centered`** `(txt: str, pos: Point, size: int)` : Draw a centered text, given center and font px size

### Images and sounds

- **`load_image`** `(src: str) -> str` : Load an image and return a name for it
- **`draw_image`** `(src: str, pos: Point)` : Blit a whole image, given its name and the position
- **`draw_image_clip`** `(src: str, pos: Point, clip_pos: Point, clip_size: Point)` : Blit a portion of an image
- **`load_audio`** `(src: str) -> str` : Load a sound and return a name for it
- **`play_audio`** `(src: str, loop: bool)` : Play a sound, possibly in a loop, given its name
- **`pause_audio`** `(src: str)` : Stop playing a sound, given its name

### Input and output

- **`mouse_pos`** `() -> Point` : Get current mouse position
- **`mouse_clicked`** `() -> bool` : Check if left mouse button has been clicked
- **`current_keys`** `() -> list[str]` : Get all keys that are currently held down
- **`previous_keys`** `() -> list[str]` : Get all keys held down at the previous frame
- **`prompt`** `(message: str) -> str` : Show a dialog for entering a line of text
- **`confirm`** `(message: str) -> bool` : Show a dialog for confirming a decision
- **`alert`** `(message: str)` : Show a dialog with a message

[*Key values*](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values) + `"Spacebar", "LeftButton", "RightButton", "MiddleButton"`
