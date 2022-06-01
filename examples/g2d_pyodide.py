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
          import pyodide, sys, zipfile
          response = await pyodide.http.pyfetch("_app.zip")
          if response.status == 200:
              with open("_app.zip", "wb") as f:
                  f.write(await response.bytes())
              with zipfile.ZipFile('_app.zip', 'r') as zip_ref:
                  zip_ref.extractall()
              sys.path.append(".")
              import __script__
        `);
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
    import sys
except:
    # if not in browser...
    import os, sys, urllib.request, webbrowser, http.server, socketserver, shutil
    if os.path.exists('_app.zip'): os.remove('_app.zip')
    shutil.make_archive(os.path.expanduser('~/_app'), 'zip')
    os.replace(os.path.expanduser('~/_app.zip'), '_app.zip')
    # prepare a custom html file
    script_name = sys.argv[0].replace("\\", "/").split("/")[-1]
    with open("_tmp.html", "w") as f:
        print(html.replace("__script__", script_name[0:-3]), file=f)

    # open html file in default browser
    webbrowser.open("http://0.0.0.0:8008/_tmp.html")

    # minimal web server, for files in current dir
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", 8008), http.server.SimpleHTTPRequestHandler)
    print("Serving at port", 8008)
    httpd.serve_forever()


K_LEFT, K_UP, K_RIGHT, K_DOWN = 37, 38, 39, 40

_canvas, _ctx, _usr_tick = None, None, None
_mouse_pos, _curr_keys, _prev_keys = (0, 0), set(), set()
_key_codes = {"Up": "ArrowUp", "Down": "ArrowDown",
              "Left": "ArrowLeft", "Right": "ArrowRight",
              "Space": "Spacebar", " ": "Spacebar",
              "Esc": "Escape", "Del": "Delete"}
_mouse_codes = ["LeftButton", "MiddleButton", "RightButton"]
_timer, _delay = None, 1000//30
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

def init_canvas(size: (int, int)) -> None:
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
    set_color((127, 127, 127))
    _canvas.setAttribute('width', size[0])
    _canvas.setAttribute('height', size[1])
    clear_canvas()


def set_color(color: (int, int, int)) -> None:
    _ctx.strokeStyle = "rgb" + str(color)
    _ctx.fillStyle = "rgb" + str(color)

def clear_canvas() -> None:
    _ctx.clearRect(0, 0, _canvas.width, _canvas.height)

def draw_line(pt1: (int, int), pt2: (int, int)) -> None:
    _ctx.moveTo(*pt1)
    _ctx.lineTo(*pt2)
    _ctx.stroke()

def fill_circle(center: (int, int), radius: int) -> None:
    from math import pi
    _ctx.beginPath()
    _ctx.arc(*center, radius, 0, 2 * pi)
    _ctx.closePath()
    _ctx.fill()

def fill_rect(pos: (int, int), size: (int, int)) -> None:
    _ctx.fillRect(*pos, *size)

def draw_text(txt: str, pos: (int, int), size: int) -> None:
    _ctx.font = str(size) + "px sans-serif";

    # clear background rect assuming height of font
    ## width = _ctx.measureText(txt).width;
    ## _ctx.clearRect(x, y, width, size);

    _ctx.textBaseline = "top";
    _ctx.textAlign="left";
    _ctx.fillText(txt, *pos)

def draw_text_centered(txt: str, pos: (int, int), size: int) -> None:
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

def draw_image(src: str, pos: (int, int)) -> None:
    _ctx.drawImage(_loaded[load_image(src)], *pos)

def draw_image_clip(src: str, pos: (int, int), clip: (int, int),
                    size: (int, int)) -> None:
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

def mouse_pos() -> (int, int):
    return _mouse_pos

def update_canvas() -> None:
    global _prev_keys
    _prev_keys = set(_curr_keys)

def main_loop(tick=None, fps=30) -> None:
    global _timer, _delay, _usr_tick
    _delay = 1000 // fps
    _usr_tick = tick
    if _timer:
        js.clearInterval(_timer)
        _timer = None
    if _usr_tick:
        _g2d_tick()  # to solve a Brython issue
        _timer = js.setInterval(pyodide.create_proxy(_g2d_tick), _delay)
    js.document.body.addEventListener("keydown", pyodide.create_proxy(_g2d_keydown))
    js.document.body.addEventListener("keyup", pyodide.create_proxy(_g2d_keyup))
    _canvas.addEventListener("focus", pyodide.create_proxy(_g2d_focus))
    _canvas.addEventListener("mousemove", pyodide.create_proxy(_g2d_mousemove))
    _canvas.addEventListener("mousedown", pyodide.create_proxy(_g2d_mousedown))
    _canvas.addEventListener("mouseup", pyodide.create_proxy(_g2d_mouseup))

def close_canvas() -> None:
    global _canvas, _timer, _usr_tick
    _usr_tick = None
    if _timer:
        js.clearInterval(_timer)
        _timer = None
    if _canvas:
        clear_canvas()
        js.document.body.removeEventListener("keydown", _g2d_keydown)
        js.document.body.removeEventListener("keyup", _g2d_keyup)
        _canvas.parentElement.removeChild(_canvas)
        _canvas = None

def key_pressed(key: str) -> bool:
    return key in _curr_keys - _prev_keys

def key_released(key: str) -> bool:
    return key in _prev_keys - _curr_keys

def current_keys() -> tuple:
    return tuple(_curr_keys)

def previous_keys() -> tuple:
    return tuple(_prev_keys)

def mouse_clicked() -> bool:
    return key_released("LeftButton")

def _g2d_tick() -> None:
    if _usr_tick:
        _usr_tick()
        update_canvas()

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
        _mouse_pos = e.clientX - rect.left, e.clientY - rect.top

def _g2d_mousedown(e: js.event) -> None:
    e.key = _mouse_codes[min(e.button, 2)]
    _g2d_keydown(e)

def _g2d_mouseup(e: js.event) -> None:
    e.key = _mouse_codes[min(e.button, 2)]
    _g2d_keyup(e)

alert = js.alert
confirm = js.confirm
prompt = js.prompt
