from browser import doc, alert, timer
from browser.html import CANVAS, IMG, AUDIO
from math import pi

K_LEFT = 37
K_UP = 38
K_RIGHT = 39
K_DOWN = 40
		
def screen_set_mode(size: (int, int)) -> CANVAS:
    w, h = size
    canvas = CANVAS(width=w, height=h, style={"border": "1px solid black"})
    for old in doc[CANVAS]:
        doc.remove(old)
    doc <= canvas
    return canvas

def screen_fill(canvas: CANVAS, color: (int, int, int)) -> None:
    ctx = canvas.getContext("2d")
    ctx.fillStyle = "rgb" + str(color)
    ctx.fillRect(0, 0, canvas.width, canvas.height)

def draw_circle(canvas: CANVAS, color: (int, int, int), center: (int, int), radius: int) -> None:
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

def image_blit(canvas: CANVAS, image: IMG, pos: (int, int), area=None: (int, int, int, int)) -> None:
    ctx = canvas.getContext("2d")
    x, y = pos
    if area:
      xa, ya, w, h = area
      ctx.drawImage(image, xa, ya, w, h, x, y, w, h)
    else:
      ctx.drawImage(image, x, y)

def audio_load(url: str) -> AUDIO:
    return AUDIO(src=url)
    
def audio_play(audio: AUDIO, loop=False) -> None:
    audio.loop = loop
    audio.play()
    
def audio_pause(audio: AUDIO):
    audio.pause()
    

