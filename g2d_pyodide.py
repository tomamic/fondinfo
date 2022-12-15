#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

html = '''<!DOCTYPE html>
<html>
    <head>
        <title>__script__</title>
        <meta charset="UTF-8">
        <script src="https://cdn.jsdelivr.net/pyodide/dev/full/pyodide.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/BrowserFS/2.0.0/browserfs.min.js"></script>
    </head>
    <body>
        <script>
        async function main() {
        window.languagePluginUrl = "./pyodide/";
        let pyodide = await loadPyodide();
        await pyodide.runPythonAsync(`
            import base64, io, os, shutil, sys, zipfile
            app_data = """__data__"""
            with zipfile.ZipFile(io.BytesIO(base64.b64decode(app_data)), 'r') as zip_ref:
                zip_ref.extractall()
            if os.path.exists("g2d_pyodide.py"):
                shutil.copyfile("g2d_pyodide.py", "g2d.py")
            sys.path.append(".")
        `);
        main_py = pyodide.FS.readFile("__script__", { encoding: "utf8" })
        await pyodide.runPythonAsync(main_py)
        };
        main();
        </script>
        <canvas id="g2d-canvas" style="border: 1px solid silver"></canvas>
        <br><textarea id="console" rows="5" cols="50" readonly style="border: 0"></textarea>
    </body>
</html>'''

try:
    import js
    import pyodide
    from pyodide.ffi.wrappers import add_event_listener, remove_event_listener
    import sys
except:
    # if not in browser, zip the whole app folder
    import base64, os, sys, webbrowser, shutil
    tmp_file, app_file = os.path.expanduser("~/_g2dapp.zip"), "_app.html"
    if os.path.exists(app_file): os.remove(app_file)
    shutil.make_archive(tmp_file[:-4], "zip")
    # encode the zip content as Base64
    b64 = ""
    with open(tmp_file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    if os.path.exists(tmp_file): os.remove(tmp_file)
    # prepare a custom html file
    script_name = sys.argv[0].replace("\\", "/").split("/")[-1]
    with open(app_file, "w") as f:
        print(html.replace("__script__", script_name).replace("__data__", b64), file=f)
    # open html file in default browser
    webbrowser.open(app_file)
    sys.exit()

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

try:
    def write(data):
        con = js.document.getElementById("console")
        if con:
            con.value += str(data)
            con.scrollTop = con.scrollHeight
    sys.stdout.write = write
    sys.stderr.write = write
except:
    pass

def init_canvas(size: Point, scale=1) -> None:
    '''Set size of first CANVAS and return it'''
    global _canvas, _ctx, _size
    if js.document.getElementById('g2d-canvas') != None:
        _canvas = js.document.getElementById("g2d-canvas")
    else:
        _canvas = js.document.createElement('canvas')
        _canvas.setAttribute('id', 'g2d-canvas')
        _canvas.setAttribute('style', 'background:white; border: 1px solid silver; position:absolute; z-index:100; right:40px; top:40px' )
        js.document.body.prepend(_canvas)
    _ctx = _canvas.getContext("2d")
    _canvas.setAttribute('width', size[0] * scale)
    _canvas.setAttribute('height', size[1] * scale)
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

def draw_text(txt: str, pos: Point, size: int) -> None:
    _ctx.font = str(size) + "px sans-serif";

    # clear background rect assuming height of font
    ## width = _ctx.measureText(txt).width;
    ## _ctx.clearRect(x, y, width, size);

    _ctx.textBaseline = "top";
    _ctx.textAlign="left";
    _ctx.fillText(txt, *pos)

def draw_text_centered(txt: str, pos: Point, size: int) -> None:
    _ctx.font = str(size) + "px sans-serif";

    # draw background rect assuming height of font
    ## width = _ctx.measureText(txt).width;
    ## _ctx.clearRect(x - width//2, y - size//2, width, size);

    _ctx.textBaseline = "middle";
    _ctx.textAlign="center";
    _ctx.fillText(txt, *pos)

def load_image(src: str) -> str:
    if src not in _loaded:
        img = js.Image.new()
        img.src = src
        _loaded[src] = img
    return src

def draw_image(src: str, pos: Point) -> None:
    _ctx.drawImage(_loaded[load_image(src)], *pos)

def draw_image_clip(src: str, pos: Point, clip: Point,
                    size: Point) -> None:
    _ctx.drawImage(_loaded[load_image(src)], *clip, *size, *pos, *size)

def load_audio(src: str) -> str:
    if src not in _loaded:
        aud = js.Audio.new(src)
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
        clear_canvas()
        remove_event_listener(js.document.body, "keydown", _g2d_keydown)
        remove_event_listener(js.document.body, "keyup", _g2d_keyup)
        _canvas.parentElement.removeChild(_canvas)
        _canvas = None

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
    if _usr_tick:
        if now - _last_frame >= _delay:
            _last_frame = now
            _usr_tick()
            update_canvas()
        js.requestAnimationFrame(_proxy_tick)
        
_proxy_tick = pyodide.ffi.create_proxy(_g2d_tick)

def _g2d_keydown(e: js.event) -> None:
    try:
        if e.repeat: return
    except:
        pass
    if _usr_tick:
        #e.preventDefault()
        e.stopPropagation()
    key = _key_codes.get(e.key, e.key)
    _curr_keys.add(key)
    if key == "Pause":
        close_canvas()

def _g2d_keyup(e: js.event) -> None:
    if _usr_tick:
        #e.preventDefault()
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
