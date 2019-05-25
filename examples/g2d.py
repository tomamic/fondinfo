if __name__ == "__main__":
    import sys, webview
    webview.create_window(url="http://localhost:8008/_websocket.html",
        width=max(480, int(sys.argv[1])), height=max(360, int(sys.argv[2])),
        title="G2D Canvas", resizable=False, debug=False)
    sys.exit()

def ensure_file(name, url):
    import os, urllib.request
    if not os.path.isfile(name):
        with urllib.request.urlopen(url) as reader, open(name, "wb") as writer:
            writer.write(reader.read())

ensure_file("_websocket.py", "https://raw.githubusercontent.com/dpallot/simple-websocket-server/master/SimpleWebSocketServer/SimpleWebSocketServer.py")
ensure_file("_websocket.html", "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/websocket.html")

import os, signal, subprocess, sys, threading, time, webbrowser
import http.server, socketserver, _websocket

_ws, _httpd, _wv = None, None, None
_usr_update, _usr_keydown, _usr_keyup = None, None, None
_mouse_pos = (0, 0)
_jss, _answers, _events = [], [], []
_cond = threading.Condition()

def produce_msg(msg: str, msgs: list) -> None:
    with _cond:
        msgs.append(msg)
        _cond.notify_all()

def consume_msg(msgs: list) -> str:
    with _cond:
        while len(msgs) == 0:
            _cond.wait()
        return msgs.pop(0)

class SocketHandler(_websocket.WebSocket):
    def handleMessage(self):
        #print(self.data)
        args = self.data.split(" ", 1)
        if args[0] == "answer":
            produce_msg(args[1], _answers)
        produce_msg(self.data, _events)

    def handleConnected(self):
        global _ws
        _ws = self
        produce_msg("connect", _events)

    def handleClose(self):
        produce_msg("disconnect", _events)
        self.server.closing = True
        self.server.close()

def serve_files() -> None:
    global _httpd
    # minimal web server, for files in current dir
    socketserver.TCPServer.allow_reuse_address = True
    _httpd = socketserver.TCPServer(("", 8008),
        http.server.SimpleHTTPRequestHandler)
    _httpd.serve_forever()

def start_websocket():
    server = _websocket.SimpleWebSocketServer("localhost", 7574, SocketHandler)
    server.closing = False
    while not server.closing:
        server.serveonce()

def start_webview(w, h):
    global _wv
    try:
        import webview
        _wv = subprocess.Popen([sys.executable, __file__, str(w), str(h)])
    except:
        webbrowser.open("http://localhost:8008/_websocket.html", new=0)

def init_canvas(size: (int, int)) -> None:
    if not _ws:
        threading.Thread(target=serve_files).start()
        threading.Thread(target=start_websocket).start()
        threading.Thread(target=start_webview, args=size).start()
        consume_msg(_events)
    _jss.append(f"initCanvas({size[0]}, {size[1]})")
    update_canvas()

def set_color(c: (int, int, int)) -> None:
    _jss.append(f"setColor({c[0]}, {c[1]}, {c[2]})")

def clear_canvas() -> None:
    _jss.append(f"clearCanvas()")

def draw_line(pt1: (int, int), pt2: (int, int)) -> None:
    _jss.append(f"drawLine({pt1[0]}, {pt1[1]}, {pt2[0]}, {pt2[1]})")

def fill_circle(pt: (int, int), r: int) -> None:
    _jss.append(f"fillCircle({pt[0]}, {pt[1]}, {r})")

def fill_rect(r: (int, int, int, int)) -> None:
    _jss.append(f"fillRect({r[0]}, {r[1]}, {r[2]}, {r[3]})")

def load_image(src: str) -> str:
    key = hash(src)
    _jss.append(f"loadImage('{key}', '{src}')")
    return key

def draw_image(img: str, pt: (int, int)) -> None:
    _jss.append(f"drawImage('{img}', {pt[0]}, {pt[1]})")

def draw_image_clip(img: str, clip: (int, int, int, int), r: (int, int, int, int)) -> None:
    _jss.append(f"drawImageClip('{img}', {clip[0]}, {clip[1]}, {clip[2]}, {clip[3]}, {r[0]}, {r[1]}, {r[2]}, {r[3]})")

def draw_text(txt: str, pt: (int, int), size: int) -> None:
    _jss.append(f"drawText('{txt}', {pt[0]}, {pt[1]}, {size})")

def draw_text_centered(txt: str, pt: (int, int), size: int) -> None:
    _jss.append(f"drawTextCentered('{txt}', {pt[0]}, {pt[1]}, {size})")

def load_audio(src: str) -> str:
    key = hash(src)
    _jss.append(f"loadAudio('{key}', '{src}')")
    return key

def play_audio(audio: str, loop=False) -> None:
    l = str(loop).lower()
    _jss.append(f"playAudio('{audio}', {l})")

def pause_audio(audio: str) -> None:
    _jss.append(f"pauseAudio('{audio}')")

def _dialog(js: str) -> str:
    _jss.append(js)
    update_canvas()
    return consume_msg(_answers)

def alert(message: str) -> None:
    _dialog(f"doAlert('{message}')")

def confirm(message: str) -> bool:
    return _dialog(f"doConfirm('{message}')") == "true"

def prompt(message: str) -> str:
    return _dialog(f"doPrompt('{message}')")

def handle_events(update=None, keydown=None, keyup=None) -> None:
    global _usr_update, _usr_keydown, _usr_keyup
    _usr_update, _usr_keydown, _usr_keyup = update, keydown, keyup

def mouse_position() -> (int, int):
    return _mouse_pos

def update_canvas() -> None:
    if _ws:
        _ws.sendMessage(";\n".join(_jss + [""]))
        _jss.clear()

def main_loop(fps=30) -> None:
    global _mouse_pos
    _jss.append(f"mainLoop({fps})")
    update_canvas()
    looping = True
    while looping:
        msg = consume_msg(_events)
        args = msg.split(" ")
        if args[0] == "mousemove":
            _mouse_pos = int(args[1]), int(args[2])
        elif args[0] == "keydown" and _usr_keydown != None:
            _usr_keydown(args[1])
            update_canvas()
        elif args[0] == "keyup" and _usr_keyup != None:
            _usr_keyup(args[1])
            update_canvas()
        elif args[0] == "update" and _usr_update != None:
            _usr_update()
            update_canvas()
        elif args[0] == "disconnect":
            looping = False
    _httpd.shutdown()
    if _wv:
        _wv.terminate()

def close_canvas():
    handle_events(None, None, None)
    _jss.append(f"closeCanvas()")
    update_canvas()
