#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

@link    https://www.brython.info/static_doc/en/intro.html
@link    https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
'''

html = '''<!DOCTYPE html>
<html>
    <head>
        <title>__script__</title>
        <meta charset="UTF-8">
        <script type="text/javascript" src="_brython_dist.js"></script>
    </head>
    <body onload="brython(1)">
        <script type="text/python" src="__script__"></script>
        <canvas id="g2d-canvas" style="border: 1px solid silver"></canvas>
        <br><textarea id="console" rows="5" cols="50" readonly></textarea>
    </body>
</html>'''

try:
    from browser import doc, alert, prompt, confirm, DOMEvent
    from browser.html import CANVAS, IMG, AUDIO
    from browser.timer import set_interval, clear_interval
    import sys
except:
    # if not in browser...
    import os, sys, urllib.request, webbrowser, http.server, socketserver

    if not os.path.isfile("_brython_dist.js"):
        url = "https://raw.githubusercontent.com/brython-dev/brython/3.4.0/www/src/brython_dist.js"
        #url = "http://brython.info/src/brython_dist.js"
        with urllib.request.urlopen(url) as response:
            content = response.read()
            with open("_brython_dist.js", "wb") as brython_file:
                brython_file.write(content)

    # prepare a custom html file
    script_name = sys.argv[0].replace("\\", "/").split("/")[-1]
    with open("_tmp.html", "w") as f:
        print(html.replace("__script__", script_name), file=f)

    # open html file in default browser
    webbrowser.open("http://127.0.0.1:8000/_tmp.html")

    # minimal web server, for files in current dir
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler)
    print("Serving at port", 8000)
    httpd.serve_forever()


K_LEFT, K_UP, K_RIGHT, K_DOWN = 37, 38, 39, 40

_canvas, _ctx = None, None
_usr_update, _usr_keydown, _usr_keyup = None, None, None
_key_pressed = {}
_mouse_pos = (0, 0)
_mouse_codes = ["LeftButton", "MiddleButton", "RightButton"]
_timer, _delay = None, 1000//30

try:
    con = doc["console"]
    def write(data):
        con.value += str(data)
        con.scrollTop = con.scrollHeight
    sys.stdout.write = write
    sys.stderr.write = write
except:
    pass

def init_canvas(size: (int, int)) -> None:
    '''Set size of first CANVAS and return it'''
    global _canvas, _ctx
    try:
        _canvas = doc["g2d-canvas"]
    except:
        _canvas = CANVAS(id="g2d-canvas")
        _canvas.style = {"background": "white", "border": "1px solid silver",
                         "position": "absolute", "z-index": "100",
                         "right": "40px", "top": "40px"}
        doc.select("body")[0] <= _canvas
    _canvas.width, _canvas.height = size
    _canvas.style.width, _canvas.style.height = size
    _ctx = _canvas.getContext("2d")
    set_color((127, 127, 127))
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

def fill_rect(rect: (int, int, int, int)) -> None:
    _ctx.fillRect(*rect)

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

def load_image(url: str) -> IMG:
    return IMG(src=url)

def draw_image(image: IMG, pos: (int, int)) -> None:
    _ctx.drawImage(image, *pos)

def draw_image_clip(image: IMG, src: (int, int, int, int), dst: (int, int, int, int)) -> None:
    _ctx.drawImage(image, *src, *dst)

def load_audio(url: str) -> AUDIO:
    return AUDIO(src=url)

def play_audio(audio: AUDIO, loop=False) -> None:
    audio.loop = loop
    audio.play()

def pause_audio(audio: AUDIO) -> None:
    audio.pause()

def handle_events(update=None, keydown=None, keyup=None) -> None:
    global _usr_update, _usr_keydown, _usr_keyup
    _usr_update, _usr_keydown, _usr_keyup = update, keydown, keyup

def mouse_position() -> (int, int):
    return _mouse_pos

def update_canvas() -> None:
    pass

def main_loop(fps=30) -> None:
    global _timer, _delay
    _delay = 1000//fps
    if _timer:
        clear_interval(_timer)
        _timer = None
    if _usr_update:
        _usr_update()  # to solve a Brython issue
        _timer = set_interval(_usr_update, _delay)
    doc.onkeydown = _g2d_keydown
    doc.onkeyup = _g2d_keyup
    doc.onfocus = _g2d_focus

    doc.onmousemove = _g2d_mousemove
    doc.onmousedown = _g2d_mousedown
    doc.onmouseup = _g2d_mouseup

def close_canvas() -> None:
    handle_events()
    main_loop()

def _g2d_keydown(e: DOMEvent) -> None:
    if e.code in _key_pressed:
        return
    _key_pressed[e.code] = True
    if e.code == "Pause":
        close_canvas()
    if _usr_keydown:
        _usr_keydown(e.code)
        e.preventDefault()
        e.stopPropagation()

def _g2d_keyup(e: DOMEvent) -> None:
    if e.code in _key_pressed:
        del _key_pressed[e.code]
    if _usr_keyup:
        _usr_keyup(e.code)

def _g2d_focus(e: DOMEvent) -> None:
    global _key_pressed
    _key_pressed = {}

def _g2d_mousemove(e: DOMEvent) -> None:
    global _mouse_pos
    rect = _canvas.getBoundingClientRect()
    _mouse_pos = e.clientX - rect.left, e.clientY - rect.top

def _g2d_mousedown(e: DOMEvent) -> None:
    if 0 <= e.button < 3:
        e.code = _mouse_codes[e.button]
        _g2d_keydown(e)
        e.preventDefault()
        e.stopPropagation()

def _g2d_mouseup(e: DOMEvent) -> None:
    if 0 <= e.button < 3:
        e.code = _mouse_codes[e.button]
        _g2d_keyup(e)
        e.preventDefault()
        e.stopPropagation()

