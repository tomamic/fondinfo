#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from tkinter import Tk, messagebox, simpledialog
import subprocess, sys
try:
    import pygame
except:
    subprocess.call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

_tkmain = Tk()
_tkmain.wm_withdraw() #to hide the main window
_ws, _hs = _tkmain.winfo_screenwidth(), _tkmain.winfo_screenheight()
_tkmain.geometry("100x100+%d+%d" % (_ws//2, _hs//2))

_canvas = None
_tick = None
_color = (127, 127, 127)
_mouse_pos = (0, 0)
_pressed, _released = set(), set()
_mouse_codes = ["LeftButton", "MiddleButton", "RightButton"]
_loaded = {}

def _tup(t: tuple) -> tuple:
    return tuple(map(int, t))

def init_canvas(size: (int, int)):
    '''Set size of first CANVAS and return it'''
    global _canvas
    pygame.init()
    _canvas = pygame.display.set_mode(_tup(size))
    clear_canvas()

def set_color(color: (int, int, int)) -> None:
    global _color
    _color = _tup(color)

def clear_canvas() -> None:
    _canvas.fill((255, 255, 255))

def update_canvas() -> None:
    _pressed.clear()
    _released.clear()
    pygame.display.update()

def draw_line(pt1: (int, int), pt2: (int, int)) -> None:
    pygame.draw.line(_canvas, _color, _tup(pt1), _tup(pt2))

def fill_circle(center: (int, int), radius: int) -> None:
    pygame.draw.circle(_canvas, _color, _tup(center), int(radius))

def fill_rect(rectangle: (int, int, int, int)) -> None:
    pygame.draw.rect(_canvas, _color, _tup(rectangle))

def draw_text(txt: str, pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('freesansbold', int(size))
    surface = font.render(txt, True, _color)
    _canvas.blit(surface, _tup(pos))

def draw_text_centered(txt: str, pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('freesansbold', int(size))
    surface = font.render(txt, True, _color)
    w, h = surface.get_size()
    _canvas.blit(surface, (int(pos[0]) - w//2, int(pos[1]) - h//2))

def load_image(src: str) -> str:
    if src not in _loaded:
        _loaded[src] = pygame.image.load(src)
    return src

def draw_image(src: str, pos: (int, int)) -> None:
    _canvas.blit(_loaded[load_image(src)], _tup(pos))

def draw_image_clip(src: str, clip: (int, int, int, int), pos: (int, int, int, int)) -> None:
    image = _loaded[load_image(src)]
    clip, pos = _tup(clip), _tup(pos)
    x0, y0, w0, h0 = clip
    x1, y1, w1, h1 = pos
    if w0 == w1 and h0 == h1:
        _canvas.blit(image, pos, area=clip)
    else:
        cropped = pygame.Surface((w0, h0), pygame.SRCALPHA)
        cropped.blit(image, (0, 0), area=clip)
        scaled = pygame.transform.smoothscale(cropped, (w1, h1))
        _canvas.blit(scaled, (x1, y1))

def load_audio(url: str) -> str:
    if src not in _loaded:
        _loaded[src] = pygame.mixer.Sound(url)
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
    return simpledialog.askstring("", message, parent=_tkmain)

def mouse_position() -> (int, int):
    return _mouse_pos

def web_key(key: int) -> str:
    fixes = {"up" : "ArrowUp", "down" : "ArrowDown",
             "right" : "ArrowRight", "left" : "ArrowLeft",
             "space": "Spacebar", "return": "Enter"}
    name = pygame.key.name(key)
    if name in fixes:
        name = fixes[name]
    elif len(name) > 1:
        name = "".join(w.capitalize() for w in name.split())
    return name

def key_pressed(key: str) -> bool:
    return key in _pressed

def key_released(key: str) -> bool:
    return key in _released

def pressed_keys() -> tuple:
    return tuple(_pressed)

def released_keys() -> tuple:
    return tuple(_released)

def main_loop(tick=None, fps=30) -> None:
    global _mouse_pos, _tick
    _tick = tick
    clock = pygame.time.Clock()
    update_canvas()
    running = True
    while running:
        for e in pygame.event.get():
            # print(e)
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type in (pygame.KEYDOWN, pygame.KEYUP):
                key = web_key(e.key)
                set_in = _released if e.type == pygame.KEYUP else _pressed
                set_out = _pressed if e.type == pygame.KEYUP else _released
                if key in set_out: set_out.discard(key)
                else: set_in.add(key)
            elif (e.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP) and
                  1 <= e.button <= 3):
                key = _mouse_codes[e.button - 1]
                set_in = _released if e.type == pygame.MOUSEBUTTONUP else _pressed
                set_out = _pressed if e.type == pygame.MOUSEBUTTONUP else _released
                if key in set_out: set_out.discard(key)
                else: set_in.add(key)
        if _tick:
            _mouse_pos = pygame.mouse.get_pos()
            _tick()
            update_canvas()
        clock.tick(fps)
    close_canvas()

def close_canvas() -> None:
    pygame.quit()
    sys.exit()
