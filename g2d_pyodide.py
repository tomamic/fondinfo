#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

html = '''<!DOCTYPE html>
<html>
    <head>
        <title>%%SCRIPT%%</title>
        <meta charset="UTF-8">
        <script src="https://cdn.jsdelivr.net/pyodide/dev/full/pyodide.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/BrowserFS/2.0.0/browserfs.min.js"></script>
    </head>
    <body>
        <canvas id="g2d-canvas" style="border: 1px solid silver"></canvas>
        <br><textarea id="console" rows="5" cols="50" readonly style="border: 0"></textarea>
        <script>
        async function main() {
        window.languagePluginUrl = "./pyodide/";
        let pyodide = await loadPyodide();
        pyodide.runPython(`
            import base64, io, js, os, shutil, sys, zipfile
            app_data = """%%DATA%%"""
            with zipfile.ZipFile(io.BytesIO(base64.b64decode(app_data)), 'r') as zip_ref:
                zip_ref.extractall()
            if os.path.exists("g2d_pyodide.py"):
                shutil.copyfile("g2d_pyodide.py", "g2d.py")
            sys.path.append(".")

            def write(data):
                console = js.document.getElementById("console")
                console.value += str(data)
                console.scrollTop = console.scrollHeight
            sys.stdout.write = sys.stderr.write = write
        `, { globals: pyodide.globals.get("dict")() } );
        main_py = pyodide.FS.readFile("%%SCRIPT%%", { encoding: "utf8" });
        pyodide.runPython(main_py);
        };
        main();
        </script>
    </body>
</html>'''

def _archive_project():
    # if not in browser, zip the whole app folder
    import base64, io, os, sys, webbrowser, zipfile
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for dirname, subdirs, files in os.walk("."):
            subdirs[:] = (n for n in subdirs if n[0:1].isalnum())
            for n in files:
                if n[0:1].isalnum():
                    zf.write(os.path.join(dirname, n))
    # encode the zip content as Base64
    b64 = base64.b64encode(zip_buffer.getvalue()).decode("ascii")
    if __name__ != "__main__":
        # prepare a custom html file, open in default browser
        app_file = "_g2dapp.html"
        with open(app_file, "w") as f:
            script_name = sys.argv[0].replace("\\", "/").split("/")[-1]
            print(html.replace("%%SCRIPT%%", script_name).replace("%%DATA%%", b64), file=f)
        webbrowser.open(app_file)
    else:
        print(b64)
    sys.exit()

try:
    import base64, js, pyodide, sys
    import traceback
    from pyodide.ffi.wrappers import add_event_listener, remove_event_listener
except:
    _archive_project()

Point = "tuple[int, int]"
Color = "tuple[int, int, int]"

_canvas, _ctx, _usr_tick = None, None, None
_mouse_pos, _curr_keys, _prev_keys = (0, 0), set(), set()
_key_codes = {"Up": "ArrowUp", "Down": "ArrowDown",
              "Left": "ArrowLeft", "Right": "ArrowRight",
              "Space": "Spacebar", " ": "Spacebar",
              "Esc": "Escape", "Del": "Delete"}
_mouse_codes = ["LeftButton", "MiddleButton", "RightButton"]
_lclick, _rclick = False, False
_delay, _last_frame = 1000 / 30, 0
_loaded = {}

def init_canvas(size: Point, scale=1) -> None:
    global _canvas, _ctx, _size
    if not (_canvas := js.document.getElementById("g2d-canvas")):
        _canvas = js.document.createElement("canvas")
        _canvas.setAttribute("id", "g2d-canvas")
        _canvas.setAttribute("style", "background:white; border: 1px solid silver; position:absolute; z-index:100; right:40px; top:40px")
        js.document.body.prepend(_canvas)
    _ctx = _canvas.getContext("2d")
    _canvas.setAttribute("width", size[0] * scale)
    _canvas.setAttribute("height", size[1] * scale)
    _ctx.scale(scale, scale)
    clear_canvas()
    set_color((127, 127, 127))

def set_color(color: Color) -> None:
    _ctx.strokeStyle = "rgb" + str(color)
    _ctx.fillStyle = "rgb" + str(color)

def clear_canvas() -> None:
    _ctx.clearRect(0, 0, _canvas.width, _canvas.height)

def draw_line(pt1: Point, pt2: Point, width=1) -> None:
    _ctx.lineWidth = width
    _ctx.beginPath()
    _ctx.moveTo(*pt1)
    _ctx.lineTo(*pt2)
    _ctx.closePath()
    _ctx.stroke()
    _ctx.lineWidth = 1

def draw_circle(center: Point, radius: int) -> None:
    from math import pi
    _ctx.beginPath()
    _ctx.arc(*center, radius, 0, 2 * pi)
    _ctx.closePath()
    _ctx.fill()

def draw_rect(pos: Point, size: Point) -> None:
    _ctx.fillRect(*pos, *size)

def draw_text(txt: str, pos: Point, size: int, centered=False) -> None:
    _ctx.font = str(size) + "px sans-serif";

    # clear background rect assuming height of font
    ## width = _ctx.measureText(txt).width;
    ## _ctx.clearRect(x, y, width, size);

    _ctx.textBaseline = "middle" if centered else "top";
    _ctx.textAlign = "center" if centered else "left";
    _ctx.fillText(txt, *pos)

def draw_text_centered(txt: str, pos: Point, size: int) -> None:
   draw_text(txt, pos, size, True)

def load_image(src: str) -> str:
    if src not in _loaded:
        img = js.Image.new()
        img.src = src
        if not src.startswith("http"):
            with open(src, "rb") as f:
                img.src = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
        _loaded[src] = img
    return src

def draw_image(src: str, pos: Point) -> None:
    _ctx.drawImage(_loaded[load_image(src)], *pos)

def draw_image_clip(src: str, pos: Point, clip: Point,
                    size: Point) -> None:
    _ctx.drawImage(_loaded[load_image(src)], *clip, *size, *pos, *size)

def load_audio(src: str) -> str:
    if src not in _loaded:
        aud = js.Audio.new()
        aud.src = src
        if not src.startswith("http"):
            with open(src, "rb") as f:
                aud.src = "data:audio/mpeg;base64," + base64.b64encode(f.read()).decode("ascii")
        _loaded[src] = aud
    return src

def play_audio(src: str, loop=False) -> None:
    audio = _loaded[load_audio(src)]
    audio.loop = loop
    audio.play()

def pause_audio(src: str) -> None:
    audio = _loaded[load_audio(src)]
    audio.pause()

def mouse_pos() -> Point:
    return _mouse_pos

def update_canvas() -> None:
    global _prev_keys, _lclick, _rclick
    _prev_keys = set(_curr_keys)
    if _lclick:
        _curr_keys.discard(_mouse_codes[0])
        _lclick = False
    if _rclick:
        _curr_keys.discard(_mouse_codes[2])
        _rclick = False

def main_loop(tick=None, fps=30) -> None:
    global _delay, _usr_tick
    _delay = 1000 / fps
    _usr_tick = tick
    js.requestAnimationFrame(_proxy_tick)
    if _canvas:
        add_event_listener(js.document.body, "keydown", _g2d_keydown)
        add_event_listener(js.document.body, "keyup", _g2d_keyup)
        add_event_listener(_canvas, "focus", _g2d_focus)
        add_event_listener(_canvas, "mousemove", _g2d_mousemove)
        add_event_listener(_canvas, "mousedown", _g2d_mousedown)
        add_event_listener(_canvas, "mouseup", _g2d_mouseup)
        add_event_listener(_canvas, "click", _g2d_lclick)
        add_event_listener(_canvas, "contextmenu", _g2d_rclick)

def close_canvas() -> None:
    global _canvas, _usr_tick
    _usr_tick = None
    if _canvas:
        _canvas.parentElement.removeChild(_canvas)
        _canvas = None
        try:
            remove_event_listener(js.document.body, "keydown", _g2d_keydown)
            remove_event_listener(js.document.body, "keyup", _g2d_keyup)
        except:
            pass

def key_pressed(key: str) -> bool:
    return key in _curr_keys - _prev_keys

def key_released(key: str) -> bool:
    return key in _prev_keys - _curr_keys

def current_keys() -> list:
    return list(_curr_keys)

def previous_keys() -> list:
    return list(_prev_keys)

def mouse_clicked() -> bool:
    return key_released(_mouse_codes[0])

def mouse_right_clicked() -> bool:
    return key_released(_mouse_codes[2])

def _g2d_tick(now: float) -> None:
    global _last_frame
    try:
        if _usr_tick:
            if now - _last_frame >= _delay:
                _last_frame = now
                _usr_tick()
                update_canvas()
            js.requestAnimationFrame(_proxy_tick)
    except:
        traceback.print_exc()

_proxy_tick = pyodide.ffi.create_proxy(_g2d_tick)

def _g2d_keydown(e: js.event) -> None:
    try:
        if e.repeat: return
    except:
        pass
    if _usr_tick:
        e.preventDefault() #
        e.stopPropagation()
    key = _key_codes.get(e.key, e.key)
    _curr_keys.add(key)
    if key == "Pause":
        close_canvas()

def _g2d_keyup(e: js.event) -> None:
    if _usr_tick:
        e.preventDefault() #
        e.stopPropagation()
    key = _key_codes.get(e.key, e.key)
    _curr_keys.discard(key)

def _g2d_focus(e: js.event) -> None:
    return

def _g2d_mousemove(e: js.event) -> None:
    global _mouse_pos
    canvas = js.document.getElementById('g2d-canvas')
    if canvas != None:
        rect = canvas.getBoundingClientRect()
        _mouse_pos = int(e.clientX - rect.left), int(e.clientY - rect.top)

def _g2d_mousedown(e: js.event) -> None:
    e.key = _mouse_codes[min(e.button, 2)]
    _g2d_keydown(e)

def _g2d_mouseup(e: js.event) -> None:
    e.key = _mouse_codes[min(e.button, 2)]
    _g2d_keyup(e)

def _g2d_lclick(e: js.event) -> None:
    global _lclick
    _curr_keys.add(_mouse_codes[0])
    _lclick = True
    #e.preventDefault()
    e.stopPropagation()

def _g2d_rclick(e: js.event) -> None:
    global _rclick
    _curr_keys.add(_mouse_codes[2])
    _rclick = True
    e.preventDefault()
    e.stopPropagation()

alert = js.alert
confirm = js.confirm
prompt = js.prompt
