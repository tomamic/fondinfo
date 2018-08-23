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
        <script type="text/javascript" src="~brython_dist.js"></script>
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

    if not os.path.isfile("~brython_dist.js"):
        url = "https://raw.githubusercontent.com/brython-dev/brython/3.4.0/www/src/brython_dist.js"
        #url = "http://brython.info/src/brython_dist.js"
        with urllib.request.urlopen(url) as response:
            content = response.read()
            with open("~brython_dist.js", "wb") as brython_file:
                brython_file.write(content)

    # prepare a custom html file
    script_name = sys.argv[0].replace("\\", "/").split("/")[-1]
    with open("~tmp.html", "w") as f:
        print(html.replace("__script__", script_name), file=f)

    # open html file in default browser
    webbrowser.open("http://127.0.0.1:8000/~tmp.html")    

    # minimal web server, for files in current dir
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler)
    print("Serving at port", 8000)
    httpd.serve_forever()


K_LEFT, K_UP, K_RIGHT, K_DOWN = 37, 38, 39, 40

_canvas = None
_usr_keydown, _usr_keyup = None, None
_usr_mousedown, _usr_mouseup = None, None
_key_pressed = {}
_timer = None

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
    global _canvas
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

def fill_canvas(color: (int, int, int)) -> None:
    draw_rect(color, (0, 0, _canvas.width, _canvas.height))

def update_canvas() -> None:
    pass

def draw_line(color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None:
    ctx = _canvas.getContext("2d")
    x1, y1 = pt1
    x2, y2 = pt2
    ctx.strokeStyle = "rgb" + str(color)
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.stroke()

def draw_circle(color: (int, int, int), center: (int, int), radius: int) -> None:
    from math import pi
    ctx = _canvas.getContext("2d")
    x, y = center
    ctx.fillStyle = "rgb" + str(color)
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, 2 * pi)
    ctx.closePath()
    ctx.fill()

def draw_rect(color: (int, int, int), rectangle: (int, int, int, int)) -> None:
    ctx = _canvas.getContext("2d")
    x, y, w, h = rectangle
    ctx.fillStyle = "rgb" + str(color)
    ctx.fillRect(x, y, w, h)

def draw_text(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    ctx = _canvas.getContext("2d")
    x, y = pos
    ctx.font = str(size) + "px sans-serif";

    # draw background rect assuming height of font
##    ctx.fillStyle = "rgb(255, 255, 255)"
##    width = ctx.measureText(txt).width;
##    ctx.fillRect(x, y, width, size);

    ctx.fillStyle = "rgb" + str(color)
    ctx.textBaseline = "top";
    ctx.textAlign="left";
    ctx.fillText(txt, x, y)

def draw_text_centered(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    ctx = _canvas.getContext("2d")
    x, y = pos
    ctx.font = str(size) + "px sans-serif";

    # draw background rect assuming height of font
##    ctx.fillStyle = "rgb(255, 255, 255)"
##    width = ctx.measureText(txt).width;
##    ctx.fillRect(x - width//2, y - size//2, width, size);

    ctx.fillStyle = "rgb" + str(color)
    ctx.textBaseline = "middle";
    ctx.textAlign="center";
    ctx.fillText(txt, x, y)

def load_image(url: str) -> IMG:
    return IMG(src=url)

def draw_image(image: IMG, pos: (int, int)) -> None:
    ctx = _canvas.getContext("2d")
    x, y = pos
    ctx.drawImage(image, x, y)

def draw_image_clip(image: IMG, rect: (int, int, int, int), clip: (int, int, int, int)) -> None:
    ctx = _canvas.getContext("2d")
    x, y, w, h = rect
    ax, ay, aw, ah = clip
    ctx.drawImage(image, ax, ay, aw, ah, x, y, w, h)

def load_audio(url: str) -> AUDIO:
    return AUDIO(src=url)
    
def play_audio(audio: AUDIO, loop=False) -> None:
    audio.loop = loop
    audio.play()
    
def pause_audio(audio: AUDIO) -> None:
    audio.pause()

def handle_keyboard(keydown, keyup) -> None:
    global _usr_keydown, _usr_keyup
    _usr_keydown, _usr_keyup = keydown, keyup

def handle_mouse(mousedown, mouseup) -> None:
    global _usr_mousedown, _usr_mouseup
    _usr_mousedown, _usr_mouseup = mousedown, mouseup

def main_loop(update=None, millis=100) -> None:
    global _timer
    if _timer:
        clear_interval(_timer)
        _timer = None
    if update:
        update()  # to solve a Brython issue 
        _timer = set_interval(update, millis)

def exit() -> None:
    handle_keyboard(None, None)
    handle_mouse(None, None)
    main_loop(None, 0)

def _g2d_keydown(e: DOMEvent) -> None:
    if e.code in _key_pressed:
        return
    _key_pressed[e.code] = True
    if e.code == "Pause":
        exit()
    if _usr_keydown:
        _usr_keydown(e.code)

def _g2d_keyup(e: DOMEvent) -> None:
    if e.code in _key_pressed:
        del _key_pressed[e.code]
    if _usr_keyup:
        _usr_keyup(e.code)

def _g2d_focus(e: DOMEvent) -> None:
    global _key_pressed
    _key_pressed = {}

def mouse_pos(e: DOMEvent) -> (int, int):
    rect = _canvas.getBoundingClientRect()
    return e.clientX - rect.left, e.clientY - rect.top

def _g2d_mousedown(e: DOMEvent) -> None:
    if _usr_mousedown:
        _usr_mousedown(mouse_pos(e), e.button)
        e.preventDefault()
        e.stopPropagation()

def _g2d_mouseup(e: DOMEvent) -> None:
    if _usr_mouseup:
        _usr_mouseup(mouse_pos(e), e.button)
        e.preventDefault()
        e.stopPropagation()

doc.onkeydown = _g2d_keydown
doc.onkeyup = _g2d_keyup
doc.onfocus = _g2d_focus

doc.onmousedown = _g2d_mousedown
doc.onmouseup = _g2d_mouseup
