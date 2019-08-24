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
_keys, _prev_keys = set(), set()
_mouse_codes = ["LeftButton", "MiddleButton", "RightButton"]

def init_canvas(size: (int, int)):
    '''Set size of first CANVAS and return it'''
    global _canvas
    pygame.init()
    _canvas = pygame.display.set_mode(size)
    clear_canvas()

def set_color(color: (int, int, int)) -> None:
    global _color
    _color = color

def clear_canvas() -> None:
    _canvas.fill((255, 255, 255))

def update_canvas() -> None:
    pygame.display.update()

def draw_line(pt1: (int, int), pt2: (int, int)) -> None:
    pygame.draw.line(_canvas, _color, pt1, pt2)

def fill_circle(center: (int, int), radius: int) -> None:
    pygame.draw.circle(_canvas, _color, center, radius)

def fill_rect(rectangle: (int, int, int, int)) -> None:
    pygame.draw.rect(_canvas, _color, rectangle)

def draw_text(txt: str, pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, _color)
    _canvas.blit(surface, pos)

def draw_text_centered(txt: str, pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, _color)
    w, h = surface.get_size()
    _canvas.blit(surface, (pos[0] - w // 2, pos[1] - h // 2))

def load_image(url: str) -> pygame.Surface:
    return pygame.image.load(url)

def draw_image(image: pygame.Surface, pos: (int, int)) -> None:
    _canvas.blit(image, pos)

def draw_image_clip(image: pygame.Surface, src: (int, int, int, int), dst: (int, int, int, int)) -> None:
    x0, y0, w0, h0 = src
    x1, y1, w1, h1 = dst
    if w0 == w1 and h0 == h1:
        _canvas.blit(image, dst, area=src)
    else:
        cropped = pygame.Surface((w0, h0), pygame.SRCALPHA)
        cropped.blit(image, (0, 0), area=src)
        scaled = pygame.transform.smoothscale(cropped, (w1, h1))
        _canvas.blit(scaled, (x1, y1))

def load_audio(url: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(url)

def play_audio(audio: pygame.mixer.Sound, loop=False) -> None:
    audio.play(-1 if loop else 0)

def pause_audio(audio: pygame.mixer.Sound) -> None:
    audio.stop()

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
    word = pygame.key.name(key)
    word = word[0].upper() + word[1:]
    if len(word) == 1 and word.isalpha():
        word = "Key" + word
    elif len(word) == 1 and word.isdigit():
        word = "Digit" + word
    elif word in ("Up", "Down", "Right", "Left"):
        word = "Arrow" + word
    elif word == "Space":
        word = "Spacebar"
    elif word == "Return":
        word = "Enter"
    return word

def key_pressed(key: str) -> bool:
    return key in _keys and key not in _prev_keys

def key_released(key: str) -> bool:
    return key in _prev_keys and key not in _keys

def main_loop(tick=None, fps=30) -> None:
    global _mouse_pos, _tick, _prev_keys
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
            elif e.type == pygame.KEYDOWN:
                _keys.add(web_key(e.key))
            elif e.type == pygame.KEYUP:
                _keys.discard(web_key(e.key))
            elif (e.type == pygame.MOUSEBUTTONDOWN and
                  1 <= e.button <= 3):
                _keys.add(_mouse_codes[e.button - 1])
            elif (e.type == pygame.MOUSEBUTTONUP and
                  1 <= e.button <= 3):
                _keys.discard(_mouse_codes[e.button - 1])
        if _tick:
            _mouse_pos = pygame.mouse.get_pos()
            _tick()
            _prev_keys = _keys.copy()
            update_canvas()
        clock.tick(fps)
    close_canvas()

def close_canvas() -> None:
    pygame.quit()
    sys.exit()
