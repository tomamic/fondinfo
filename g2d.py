#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from tkinter import Tk, messagebox, simpledialog
import io
from urllib.request import urlopen
import subprocess, sys
try:
    import pygame as pg
except:
    subprocess.call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame as pg

Point = "tuple[int, int]"
Color = "tuple[int, int, int]"

_tkmain = Tk()
_tkmain.wm_withdraw() #to hide the main window
_ws, _hs = _tkmain.winfo_screenwidth(), _tkmain.winfo_screenheight()
_tkmain.geometry("100x100+%d+%d" % (_ws//2, _hs//2))

_canvas, _tick = None, None
_size, _color = (640, 480), (127, 127, 127)
_mouse_pos, _mouse_down = (0, 0), 0
_curr_keys, _prev_keys = set(), set()
_loaded = {}

def _tup(t: tuple) -> tuple:
    return tuple(map(int, t))

def init_canvas(size: Point):
    '''Set size of first CANVAS and return it'''
    global _canvas, _size
    pg.init()
    _size = size
    _canvas = pg.display.set_mode(_tup(size))
    clear_canvas()

def canvas_size() -> Point:
    return _size

def set_color(color: Color) -> None:
    global _color
    _color = _tup(color)

def clear_canvas() -> None:
    _canvas.fill((255, 255, 255))

def update_canvas() -> None:
    global _prev_keys
    _prev_keys = set(_curr_keys)
    pg.display.update()

def draw_line(pt1: Point, pt2: Point, width=1) -> None:
    pg.draw.line(_canvas, _color, _tup(pt1), _tup(pt2), int(width))

def draw_circle(center: Point, radius: int) -> None:
    pg.draw.circle(_canvas, _color, _tup(center), int(radius))

def draw_rect(pos: Point, size: Point) -> None:
    pg.draw.rect(_canvas, _color, _tup(pos + size))

def draw_text(txt: str, pos: Point, size: int) -> None:
    font = pg.font.SysFont('freesansbold', int(size))
    surface = font.render(txt, True, _color)
    _canvas.blit(surface, _tup(pos))

def draw_text_centered(txt: str, pos: Point, size: int) -> None:
    font = pg.font.SysFont('freesansbold', int(size))
    surface = font.render(txt, True, _color)
    w, h = surface.get_size()
    _canvas.blit(surface, (int(pos[0]) - w//2, int(pos[1]) - h//2))

def load_image(src: str) -> str:
    gh = "https://raw.githubusercontent.com/tomamic/fondinfo/master/"
    if src not in _loaded:
        try:
            _loaded[src] = pg.image.load(src)
        except:
            url = src if src.startswith("http") else gh + src
            image = io.BytesIO(urlopen(url).read())
            _loaded[src] = pg.image.load(image)
    return src

def draw_image(src: str, pos: Point) -> None:
    _canvas.blit(_loaded[load_image(src)], _tup(pos))

def draw_image_clip(src: str, pos: Point, clip_pos: Point, clip_size: Point) -> None:
    image = _loaded[load_image(src)]
    _canvas.blit(image, _tup(pos), area=_tup(clip_pos) + _tup(clip_size))

def load_audio(src: str) -> str:
    if src not in _loaded:
        try:
            _loaded[src] = pg.mixer.Sound(src)
        except:
            audio = io.BytesIO(urlopen(src).read())
            _loaded[src] = pg.mixer.Sound(audio)
    return src

def play_audio(src: str, loop=False) -> None:
    _loaded[load_audio(src)].play(-1 if loop else 0)

def pause_audio(src: str) -> None:
    _loaded[load_audio(src)].stop()

def alert(message: str) -> None:
    if _canvas:
        update_canvas()
    messagebox.showinfo("", message)

def confirm(message: str) -> bool:
    if _canvas:
        update_canvas()
    return messagebox.askokcancel("", message)

def prompt(message: str) -> str:
    if _canvas:
        update_canvas()
    return simpledialog.askstring("", message, parent=_tkmain) or ""

def mouse_pos() -> Point:
    return _mouse_pos

def _mb_name(key: int) -> str:
    return ["LeftButton", "MiddleButton", "RightButton"][min(key - 1, 2)]

def _kb_name(key: int) -> str:
    fixes = {"up" : "ArrowUp", "down" : "ArrowDown",
             "right" : "ArrowRight", "left" : "ArrowLeft",
             "space": "Spacebar", "return": "Enter"}
    name = pg.key.name(key)
    if name in fixes:
        name = fixes[name]
    elif len(name) > 1:
        name = "".join(w.capitalize() for w in name.split())
    return name

def current_keys() -> tuple:
    return list(_curr_keys)

def previous_keys() -> tuple:
    return list(_prev_keys)

def mouse_clicked() -> bool:
    return key_released("LeftButton")

def mouse_right_clicked() -> bool:
    return key_released("RightButton")

def key_pressed(key: str) -> bool:
    return key in _curr_keys and key not in _prev_keys

def key_released(key: str) -> bool:
    return key in _prev_keys and key not in _curr_keys

def main_loop(tick=None, fps=30) -> None:
    global _mouse_pos, _tick
    _tick = tick
    clock = pg.time.Clock()
    update_canvas()
    running = True
    while running:
        for e in pg.event.get():
            # print(e)
            if e.type == pg.QUIT:
                running = False
                # break
            elif e.type == pg.KEYDOWN:
                _curr_keys.add(_kb_name(e.key))
            elif e.type == pg.KEYUP:
                _curr_keys.discard(_kb_name(e.key))
            elif e.type == pg.MOUSEBUTTONDOWN:
                _curr_keys.add(_mb_name(e.button))
            elif e.type == pg.MOUSEBUTTONUP:
                _curr_keys.discard(_mb_name(e.button))
        if _tick:
            _mouse_pos = pg.mouse.get_pos()
            _tick()
            update_canvas()
        clock.tick(fps)
    close_canvas()

def close_canvas() -> None:
    pg.quit()
    sys.exit()
