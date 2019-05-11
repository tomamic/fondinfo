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
import http.server, socketserver, concurrent.futures
from _websocket import WebSocket, SimpleWebSocketServer

_server, _socket, _httpd, _wv = None, None, None, None
_jss = []
_usr_update, _usr_keydown, _usr_keyup = None, None, None
_mouse_pos = (0, 0)
_dialog_ans = None
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
_socket_c, _dialog_c = threading.Condition(), threading.Condition()

class SocketHandler(WebSocket):

    def handleMessage(self):
        #print("message:", self.data)
        _executor.submit(lambda d=self.data: _handle_data(d))

    def handleConnected(self):
        #print("connected")
        global _socket
        with _socket_c:
            _socket = self
            _socket_c.notify_all()

    def handleClose(self):
        #print("close")
        global _socket
        with _socket_c:
            _socket = None
            _socket_c.notify_all()

def _handle_data(data: str):
    global _mouse_pos
    #print(data)
    args = data.split(" ")
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
    elif args[0] == "dialog":
        global _dialog_ans
        with _dialog_c:
            _dialog_ans = data.split(" ", 1)[1]
            _dialog_c.notify_all()

def serve_files() -> None:
    global _httpd
    # minimal web server, for files in current dir
    socketserver.TCPServer.allow_reuse_address = True
    _httpd = socketserver.TCPServer(("", 8008),
        http.server.SimpleHTTPRequestHandler)
    _httpd.serve_forever()

def start_server():
    global _server
    _server = SimpleWebSocketServer("localhost", 7574, SocketHandler)
    while _server:
        _server.serveonce()

def start_webview(w, h):
    try:
        import webview
        global _wv
        _wv = subprocess.Popen([sys.executable, __file__, str(w), str(h)])
    except:
        webbrowser.open("http://localhost:8008/_websocket.html", new=0)

def init_canvas(size: (int, int)) -> None:
    if _server == None:
        _executor.submit(serve_files)
        _executor.submit(start_server)
        _executor.submit(start_webview, *size)
        with _socket_c:
            while _socket == None:
                _socket_c.wait()
    '''
    def close_sig_handler(signal, frame):
        _server.close()
        sys.exit()
    signal.signal(signal.SIGINT, close_sig_handler)
    '''
    _eval_js(f"initCanvas({size[0]}, {size[1]});")

def set_color(c: (int, int, int)) -> None:
    _do_js(f"setColor({c[0]}, {c[1]}, {c[2]})")

def clear_canvas() -> None:
    _do_js(f"clearCanvas()")

def draw_line(pt1: (int, int), pt2: (int, int)) -> None:
    _do_js(f"drawLine({pt1[0]}, {pt1[1]}, {pt2[0]}, {pt2[1]})")

def fill_circle(pt: (int, int), r: int) -> None:
    _do_js(f"fillCircle({pt[0]}, {pt[1]}, {r})")

def fill_rect(r: (int, int, int, int)) -> None:
    _do_js(f"fillRect({r[0]}, {r[1]}, {r[2]}, {r[3]})")

def load_image(src: str) -> str:
    key = hash(src)
    _do_js(f"loadImage('{key}', '{src}')")
    return key

def draw_image(img: str, pt: (int, int)) -> None:
    _do_js(f"drawImage('{img}', {pt[0]}, {pt[1]})")

def draw_image_clip(img: str, clip: (int, int, int, int), r: (int, int, int, int)) -> None:
    _do_js(f"drawImageClip('{img}', {clip[0]}, {clip[1]}, {clip[2]}, {clip[3]}, {r[0]}, {r[1]}, {r[2]}, {r[3]})")

def draw_text(txt: str, pt: (int, int), size: int) -> None:
    _do_js(f"drawText('{txt}', {pt[0]}, {pt[1]}, {size})")

def draw_text_centered(txt: str, pt: (int, int), size: int) -> None:
    _do_js(f"drawTextCentered('{txt}', {pt[0]}, {pt[1]}, {size})")

def load_audio(src: str) -> str:
    key = hash(src)
    _do_js(f"loadAudio('{key}', '{src}')")
    return key

def play_audio(audio: str, loop=False) -> None:
    l = str(loop).lower()
    _do_js(f"playAudio('{audio}', {l})")

def pause_audio(audio: str) -> None:
    _do_js(f"pauseAudio('{audio}')")

def _dialog(js: str) -> str:
    global _dialog_ans
    with _dialog_c:
        _dialog_ans = None
        _do_js(js)
        update_canvas()
        while _dialog_ans == None:
            _dialog_c.wait()
        return _dialog_ans

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
    global _jss
    code = "".join(_jss)
    _eval_js(code)
    _jss = []

def main_loop(fps=30) -> None:
    update_canvas()
    _eval_js(f"mainLoop({fps});")
    wait_done()

def close_canvas():
    handle_events(None, None, None)
    _do_js(f"closeCanvas();")
    update_canvas()

def _do_js(cmd: str, *args) -> None:
    _jss.append(cmd + ";\n" % args)

def _eval_js(code: str) -> None:
    #print("sending:", code)
    _socket.sendMessage(code)

def wait_done():
    with _socket_c:
        while _socket:
            _socket_c.wait()
        _server.close()
        #_httpd.socket.close()
        _httpd.shutdown()
        if _wv:
            _wv.terminate()
