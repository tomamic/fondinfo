## Basic structs

- A `point` or a `size` is a tuple `(x, y)`
- A `rect` is a tuple `(x, y, w, h)`
- A `color` is a tuple `(r, g, b)`

## Canvas functions

- `init_canvas(size: (int, int))` : Initialize the drawing canvas
- `main_loop(tick=None, fps=30)` : Start the event loop, accepting an optional `tick` function, which will be called periodically
- `clear_canvas()` : Clear the canvas
- `update_canvas()` : Draw all pending graphics on the canvas, it is called automaticall after each `tick`
- `close_canvas()` : Close the canvas and exit the main loop

## Drawing functions

- `set_color(color: (int, int, int))` : Set the drawing color
- `draw_line(pt1: (int, int), pt2: (int, int))` : Draw a line from `pt1` to `pt2`
- `fill_circle(center: (int, int), radius: int)` : Fill a circle, given `center` and `radius`
- `fill_rect(rect: (int, int, int, int))` : Fill a given rectangle
- `draw_text(txt: str, pos: (int, int), size: int)` : Draw a text, given the left-top position and the font px size
- `draw_text_centered(txt: str, pos: (int, int), size: int)` : Draw a centered text, given the position and the font px size

## Images and sounds

- `load_image(src: str) -> str` : Load an image and return a name for it
- `draw_image(image: str, pos: (int, int))` : Blit a whole image, given its name and the position
- `draw_image_clip(image: str, clip: (int, int, int, int), rect: (int, int, int, int))` : Blit a portion of an image
- `load_audio(src: str) -> str` : Load a sound and return a name for it
- `play_audio(audio: str, loop: bool)` : Play a sound, possibly in a loop, given its name
- `pause_audio(audio: str)` : Stop playing a sound, given its name

## Input and output

- `mouse_position() -> (int, int)` : Get current mouse position
- `key_pressed(key: string) -> bool` : Check if a key has been pressed after last `tick`
- `key_released(key: string) -> bool` : Check if a key has been released after last `tick`
- `prompt(message: str) -> str` : Show a dialog for entering a line of text
- `confirm(message: str) -> bool` : Show a dialog for confirming a decision
- `alert(message: str)` : Show a dialog with a message

## Installing

- Copy `g2d.py` into the same folder containing your scripts; this will draw into a *browser window*
- Alternatively, copy `g2d_pyg.py` in that location and rename the file as `g2d.py`; this will use *PyGame*
