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
        <script type="text/javascript" src="brython_dist.js"></script>
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

    if not os.path.isfile('brython_dist.js'):
        url = 'http://brython.info/src/brython_dist.js'
        #url = 'https://raw.githubusercontent.com/brython-dev/brython/3dd0b0e648e75100d0c4806c39fd18edbea927b6/www/src/brython_dist.js'
        with urllib.request.urlopen(url) as response:
            content = response.read()
            with open('brython_dist.js', 'wb') as brython_file:
                brython_file.write(content)

    # prepare a custom html file
    script_name = sys.argv[0].replace('\\', '/').split('/')[-1]
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

canvas = None
onkeydown = None
onkeyup = None
key_pressed = {}

def canvas_init(size: (int, int)) -> None:
    '''Set size of first CANVAS and return it'''
    global canvas
    canvas = doc[CANVAS][0]
    canvas.width, canvas.height = size

def canvas_fill(color: (int, int, int)) -> None:
    draw_rect(color, (0, 0, canvas.width, canvas.height))

def draw_line(color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None:
    ctx = canvas.getContext("2d")
    x1, y1 = pt1
    x2, y2 = pt2
    ctx.strokeStyle = "rgb" + str(color)
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.stroke()

def draw_circle(color: (int, int, int), center: (int, int), radius: int) -> None:
    from math import pi
    ctx = canvas.getContext("2d")
    x, y = center
    ctx.fillStyle = "rgb" + str(color)
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, 2 * pi)
    ctx.closePath()
    ctx.fill()

def draw_rect(color: (int, int, int), rectangle: (int, int, int, int)) -> None:
    ctx = canvas.getContext("2d")
    x, y, w, h = rectangle
    ctx.fillStyle = "rgb" + str(color)
    ctx.fillRect(x, y, w, h)

def draw_text(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    ctx = canvas.getContext("2d")
    x, y = pos
    ctx.fillStyle = "rgb" + str(color)
    ctx.font = str(size) + "px sans-serif";
    ctx.textBaseline = "top";
    ctx.fillText(txt, x, y)

def image_load(url: str) -> IMG:
    return IMG(src=url)

def image_blit(image: IMG, pos: (int, int), area: (int, int, int, int)=None) -> None:
    ctx = canvas.getContext("2d")
    x, y = pos
    if area:
      ax, ay, aw, ah = area
      ctx.drawImage(image, ax, ay, aw, ah, x, y, aw, ah)
    else:
      ctx.drawImage(image, x, y)

def image_blit_scaled(image: IMG, pos: (int, int, int, int), area: (int, int, int, int)=None) -> None:
    ctx = canvas.getContext("2d")
    x, y, w, h = pos
    if area:
      ax, ay, aw, ah = area
      ctx.drawImage(image, ax, ay, aw, ah, x, y, w, h)
    else:
      ctx.drawImage(image, x, y, w, h)

def audio_load(url: str) -> AUDIO:
    return AUDIO(src=url)
    
def audio_play(audio: AUDIO, loop=False) -> None:
    audio.loop = loop
    audio.play()
    
def audio_pause(audio: AUDIO) -> None:
    audio.pause()

def handle_keyboard(keydown, keyup):
    global onkeydown, onkeyup
    onkeydown, onkeyup = keydown, keyup

def _keydown(e: DOMEvent):
    if e.code in key_pressed:
        return
    key_pressed[e.code] = True
    if onkeydown:
        onkeydown(e.code)

def _keyup(e: DOMEvent):
    if e.code in key_pressed:
        del key_pressed[e.code]
    if onkeyup:
        onkeyup(e.code)

def _focus(e: DOMEvent):
    global key_pressed
    key_pressed = {}

doc.onkeydown = _keydown
doc.onkeyup = _keyup
doc.onfocus = _focus
