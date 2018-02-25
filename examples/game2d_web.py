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
        <canvas style="border: 1px solid silver"></canvas>
    </body>
</html>'''

try:
    from browser import doc, alert, DOMEvent
    from browser.html import CANVAS, IMG, AUDIO
    from browser.timer import set_interval, clear_interval
except:
    # if not in browser...
    import os, sys, urllib.request, webbrowser, http.server, socketserver

    if not os.path.isfile("~brython_dist.js"):
        url = "http://brython.info/src/brython_dist.js"
        #url = "https://raw.githubusercontent.com/brython-dev/brython/3dd0b0e648e75100d0c4806c39fd18edbea927b6/www/src/brython_dist.js"
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
_usr_keydown = None
_usr_keyup = None
_key_pressed = {}

def init_canvas(size: (int, int)) -> None:
    '''Set size of first CANVAS and return it'''
    global _canvas
    _canvas = doc[CANVAS][0]
    _canvas.width, _canvas.height = size

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
    ctx.fillStyle = "rgb" + str(color)
    ctx.font = str(size) + "px sans-serif";
    ctx.textBaseline = "top";
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

def main_loop(update=None, millis=100) -> None:
    if update:
        set_interval(update, millis)

def _g2d_keydown(e: DOMEvent) -> None:
    if e.code in _key_pressed:
        return
    _key_pressed[e.code] = True
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

doc.onkeydown = _g2d_keydown
doc.onkeyup = _g2d_keyup
doc.onfocus = _g2d_focus
