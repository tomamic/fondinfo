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
        <meta charset="UTF-8">
        <script type="text/javascript" src="brython_dist.js"></script>
    </head>
    <body onload="brython(1)">
        <script type="text/python" src="__script__"></script>
        <canvas style="border: 1px solid silver"></canvas>
    </body>
</html>'''

try:
    from browser import doc, alert, timer, DOMEvent
    from browser.html import CANVAS, IMG, AUDIO
    from browser.timer import set_interval, clear_interval
except:
    # if not in browser...
    import sys, webbrowser, http.server as hs, socketserver as ss

    # prepare a custom html file
    script_name = sys.argv[0].replace('\\', '/').split('/')[-1]
    with open("~tmp.html", "w") as f:
        print(html.replace("__script__", script_name), file=f)

    # open html file in default browser
    webbrowser.open("http://127.0.0.1:8000/~tmp.html")    

    # minimal web server, for files in current dir
    ss.TCPServer.allow_reuse_address = True
    httpd = ss.TCPServer(("", 8000), hs.SimpleHTTPRequestHandler)
    print("Serving at port", 8000)
    httpd.serve_forever()


K_LEFT, K_UP, K_RIGHT, K_DOWN = 37, 38, 39, 40

def canvas_init(size: (int, int)) -> CANVAS:
    '''Set size of first CANVAS and return it'''
    canvas = doc[CANVAS][0]
    canvas.width, canvas.height = size
    return canvas

def canvas_fill(canvas: CANVAS, color: (int, int, int)) -> None:
    draw_rect(canvas, color, (0, 0, canvas.width, canvas.height))

def draw_line(canvas: CANVAS, color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None:
    ctx = canvas.getContext("2d")
    x1, y1 = pt1
    x2, y2 = pt2
    ctx.strokeStyle = "rgb" + str(color)
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.stroke()

def draw_circle(canvas: CANVAS, color: (int, int, int), center: (int, int), radius: int) -> None:
    from math import pi
    ctx = canvas.getContext("2d")
    x, y = center
    ctx.fillStyle = "rgb" + str(color)
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, 2 * pi)
    ctx.closePath()
    ctx.fill()

def draw_rect(canvas: CANVAS, color: (int, int, int), rectangle: (int, int, int, int)) -> None:
    ctx = canvas.getContext("2d")
    x, y, w, h = rectangle
    ctx.fillStyle = "rgb" + str(color)
    ctx.fillRect(x, y, w, h)

def draw_text(canvas: CANVAS, txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    ctx = canvas.getContext("2d")
    x, y = pos
    ctx.fillStyle = "rgb" + str(color)
    ctx.font = str(size) + "px sans-serif";
    ctx.textBaseline = "top";
    ctx.fillText(txt, x, y)

def image_load(url: str) -> IMG:
    return IMG(src=url)

def image_blit(canvas: CANVAS, image: IMG, pos: (int, int), area: (int, int, int, int)=None) -> None:
    ctx = canvas.getContext("2d")
    x, y = pos
    if area:
      ax, ay, aw, ah = area
      ctx.drawImage(image, ax, ay, aw, ah, x, y, aw, ah)
    else:
      ctx.drawImage(image, x, y)

def image_blit_scaled(canvas: CANVAS, image: IMG, pos: (int, int, int, int), area: (int, int, int, int)=None) -> None:
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


