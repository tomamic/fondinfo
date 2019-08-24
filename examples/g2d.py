#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''


#### g2d

import os, signal, subprocess, sys, threading, time
import http.server, socketserver, webbrowser

_ws, _httpd, _wv = None, None, None
_usr_tick = None
_mouse_pos = (0, 0)
_keys, _prev_keys = set(), set()
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

def mouse_position() -> (int, int):
    return _mouse_pos

def key_pressed(key: str) -> bool:
    return key in _keys and key not in _prev_keys

def key_released(key: str) -> bool:
    return key not in _keys and key in _prev_keys

def update_canvas() -> None:
    if _ws:
        _ws.sendMessage(";\n".join(_jss + [""]))
        _jss.clear()

def main_loop(tick=None, fps=30) -> None:
    global _mouse_pos, _usr_tick, _prev_keys
    _usr_tick = tick
    _jss.append(f"mainLoop({fps})")
    update_canvas()
    looping = True
    while looping:
        msg = consume_msg(_events)
        args = msg.split(" ")
        if args[0] == "mousemove":
            _mouse_pos = int(args[1]), int(args[2])
        elif args[0] == "keydown":
            _keys.add(args[1])
        elif args[0] == "keyup":
            _keys.discard(args[1])
        elif args[0] == "update" and _usr_tick != None:
            _usr_tick()
            update_canvas()
            _prev_keys = _keys.copy()
        elif args[0] == "disconnect":
            looping = False
    _httpd.shutdown()
    if _wv:
        _wv.terminate()

def close_canvas():
    global _usr_tick
    _usr_tick = None
    _jss.append(f"closeCanvas()")
    update_canvas()


#### index.html

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />

<title>WebSocket Test</title>
<style>
    body { margin: 0; padding: 0; }
    canvas { position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%);
             margin: 0; padding: 0; border: 1px solid silver; }
</style>
<script language="javascript" type="text/javascript">

function doConnect() {
    websocket = new WebSocket("ws://localhost:7574/");
    websocket.onopen = function(evt) {
        console.log("open");
    };
    websocket.onclose = function(evt) {
        console.log("close");
        closeCanvas();
    };
    websocket.onmessage = function(evt) {
        console.log("message: " + evt.data);
        eval(evt.data);
    };
    websocket.onerror = function(evt) {
        console.log("error");
        websocket.close();
    };
}
function doSend(message) {
    console.log("sending: " + message);
    websocket.send(message);
}
function doDisconnect() {
    console.log("disconnecting");
    websocket.close();
}
window.addEventListener("load", doConnect, false);

invokeExternal = doSend
loaded = {};
keyPressed = {};
mouseCodes = ["LeftButton", "MiddleButton", "RightButton"];

function initCanvas(w, h) {
    canvas = document.getElementById("g2d-canvas");
    if (canvas == null) {
        canvas = document.createElement("CANVAS");
        canvas.id = "g2d-canvas";
        document.getElementsByTagName("body")[0].appendChild(canvas);
    }
    canvas.width = w;
    canvas.height = h;
    ctx = canvas.getContext("2d");
    setColor(127, 127, 127);
    clearCanvas();
}
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
function setColor(r, g, b) {
    ctx.strokeStyle = "rgb("+r+", "+g+", "+b+")";
    ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
}
function drawLine(x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}
function fillCircle(x, y, r) {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, 2*Math.PI);
    ctx.closePath();
    ctx.fill();
}
function fillRect(x, y, w, h) {
    ctx.fillRect(x, y, w, h);
}
function loadImage(key, src) {
    img = document.createElement("IMG");
    img.src = src;
    img.onerror = function() {
        if (img.src.indexOf("githubusercontent") == -1) {
            img.src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/" + src;
        }
    }
    loaded[key] = img;
}
function drawImage(key, x, y) {
    img = loaded[key];
    ctx.drawImage(img, x, y);
}
function drawImageClip(key, x0, y0, w0, h0, x1, y1, w1, h1) {
    img = loaded[key];
    ctx.drawImage(img, x0, y0, w0, h0, x1, y1, w1, h1);
}
function drawText(txt, x, y, size) {
    ctx.font = "" + size + "px sans-serif";
    ctx.textBaseline = "top";
    ctx.textAlign = "left";
    ctx.fillText(txt, x, y);
}
function drawTextCentered(txt, x, y, size) {
    ctx.font = "" + size + "px sans-serif";
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillText(txt, x, y);
}
function loadAudio(key, src) {
    audio = document.createElement("AUDIO");
    audio.src = src;
    audio.onerror = function() {
        if (audio.src.indexOf("githubusercontent") == -1) {
            audio.src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/" + src;
        }
    }
    loaded[key] = audio;
}
function playAudio(key, loop) {
    audio = loaded[key];
    audio.loop = loop;
    audio.play();
}
function pauseAudio(key) {
    audio = loaded[key];
    audio.pause();
}
function doAlert(message) {
    alert(message);
    invokeExternal("answer true");
}
function doConfirm(message) {
    ans = confirm(message);
    invokeExternal("answer " + ans);
}
function doPrompt(message) {
    ans = prompt(message);
    invokeExternal("answer " + ans);
}
function fixKey(k) {
    if (k=="Left" || k=="Up" || k=="Right" || k=="Down") k = "Arrow"+k;
    else if (k==" " || k=="Space") k = "Spacebar";
    else if (k=="Esc") k = "Escape";
    else if (k=="Del") k = "Delete";
    return k;
}
function mainLoop(fps) {
    document.onkeydown = function(e) {
        var k = fixKey(e.key);
        if (keyPressed[k]) return;
        keyPressed[k] = true;
        invokeExternal("keydown " + k);
    };
    document.onkeyup = function(e) {
        var k = fixKey(e.key);
        if (keyPressed[k]) keyPressed[k] = false;
        invokeExternal("keyup " + k);
    };
    document.onmousedown = function(e) {
        if (0 <= e.button && e.button < 3) {
            invokeExternal("keydown " + mouseCodes[e.button]);
        }
    };
    document.onmouseup = function(e) {
        if (0 <= e.button && e.button < 3) {
            invokeExternal("keyup " + mouseCodes[e.button]);
        }
    };
    document.onmousemove = function(e) {
        var rect = canvas.getBoundingClientRect()
        var x = Math.round(e.clientX - rect.left)
        var y = Math.round(e.clientY - rect.top)
        invokeExternal("mousemove " + x + " " + y);
    };
    document.onfocus = function(e) {
        keyPressed = {};
    };

    if (typeof timerId !== "undefined") {
        clearInterval(timerId);
        delete timerId;
    }
    if (fps >= 0) {
        timerId = setInterval(function(e) {
            invokeExternal("update");
        }, 1000/fps);
    }
}
function closeCanvas() {
    if (typeof timerId !== "undefined") {
        clearInterval(timerId);
        delete timerId;
    }
    if (typeof canvas !== "undefined") {
        canvas.parentNode.removeChild(canvas);
        delete canvas;
    }
    doDisconnect();
    /*alert("You can close this window, now.");*/
    open("about:blank", "_self").close();
}
</script>
</head>
<body>
</body>
</html>"""

class FileHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            super().do_GET()

def serve_files() -> None:
    global _httpd
    # minimal web server, for files in current dir
    socketserver.TCPServer.allow_reuse_address = True
    _httpd = socketserver.TCPServer(("", 8008), FileHandler)
    _httpd.serve_forever()


#### webview

if __name__ == "__main__":
    import sys, webview
    webview.create_window(url="http://localhost:8008/",
        width=max(480, int(sys.argv[1])), height=max(360, int(sys.argv[2])),
        title="G2D Canvas", resizable=False, debug=False)
    sys.exit()


def start_webview(w, h):
    global _wv
    try:
        import webview
        _wv = subprocess.Popen([sys.executable, __file__, str(w), str(h)])
    except:
        webbrowser.open("http://localhost:8008/", new=0)


#### websockets

'''
The MIT License (MIT)
Copyright (c) 2013 Dave P.
'''
import sys
VER = sys.version_info[0]
if VER >= 3:
    import socketserver
    from http.server import BaseHTTPRequestHandler
    from io import StringIO, BytesIO
else:
    import SocketServer
    from BaseHTTPServer import BaseHTTPRequestHandler
    from StringIO import StringIO

import hashlib
import base64
import socket
import struct
import ssl
import errno
import codecs
from collections import deque
from select import select

def _check_unicode(val):
    if VER >= 3:
        return isinstance(val, str)
    else:
        return isinstance(val, basestring)

class HTTPRequest(BaseHTTPRequestHandler):
   def __init__(self, request_text):
      if VER >= 3:
          self.rfile = BytesIO(request_text)
      else:
          self.rfile = StringIO(request_text)
      self.raw_requestline = self.rfile.readline()
      self.error_code = self.error_message = None
      self.parse_request()

_VALID_STATUS_CODES = [1000, 1001, 1002, 1003, 1007, 1008,
                        1009, 1010, 1011, 3000, 3999, 4000, 4999]

HANDSHAKE_STR = (
   "HTTP/1.1 101 Switching Protocols\r\n"
   "Upgrade: WebSocket\r\n"
   "Connection: Upgrade\r\n"
   "Sec-WebSocket-Accept: %(acceptstr)s\r\n\r\n"
)

FAILED_HANDSHAKE_STR = (
   "HTTP/1.1 426 Upgrade Required\r\n"
   "Upgrade: WebSocket\r\n"
   "Connection: Upgrade\r\n"
   "Sec-WebSocket-Version: 13\r\n"
   "Content-Type: text/plain\r\n\r\n"
   "This service requires use of the WebSocket protocol\r\n"
)

GUID_STR = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

STREAM = 0x0
TEXT = 0x1
BINARY = 0x2
CLOSE = 0x8
PING = 0x9
PONG = 0xA

HEADERB1 = 1
HEADERB2 = 3
LENGTHSHORT = 4
LENGTHLONG = 5
MASK = 6
PAYLOAD = 7

MAXHEADER = 65536
MAXPAYLOAD = 33554432

class WebSocket(object):

   def __init__(self, server, sock, address):
      self.server = server
      self.client = sock
      self.address = address

      self.handshaked = False
      self.headerbuffer = bytearray()
      self.headertoread = 2048

      self.fin = 0
      self.data = bytearray()
      self.opcode = 0
      self.hasmask = 0
      self.maskarray = None
      self.length = 0
      self.lengtharray = None
      self.index = 0
      self.request = None
      self.usingssl = False

      self.frag_start = False
      self.frag_type = BINARY
      self.frag_buffer = None
      self.frag_decoder = codecs.getincrementaldecoder('utf-8')(errors='strict')
      self.closed = False
      self.sendq = deque()

      self.state = HEADERB1

      # restrict the size of header and payload for security reasons
      self.maxheader = MAXHEADER
      self.maxpayload = MAXPAYLOAD

   def handleMessage(self):
      """
          Called when websocket frame is received.
          To access the frame data call self.data.

          If the frame is Text then self.data is a unicode object.
          If the frame is Binary then self.data is a bytearray object.
      """
      pass

   def handleConnected(self):
      """
          Called when a websocket client connects to the server.
      """
      pass

   def handleClose(self):
      """
          Called when a websocket server gets a Close frame from a client.
      """
      pass

   def _handlePacket(self):
      if self.opcode == CLOSE:
         pass
      elif self.opcode == STREAM:
         pass
      elif self.opcode == TEXT:
         pass
      elif self.opcode == BINARY:
         pass
      elif self.opcode == PONG or self.opcode == PING:
         if len(self.data) > 125:
            raise Exception('control frame length can not be > 125')
      else:
          # unknown or reserved opcode so just close
         raise Exception('unknown opcode')

      if self.opcode == CLOSE:
         status = 1000
         reason = u''
         length = len(self.data)

         if length == 0:
            pass
         elif length >= 2:
            status = struct.unpack_from('!H', self.data[:2])[0]
            reason = self.data[2:]

            if status not in _VALID_STATUS_CODES:
                status = 1002

            if len(reason) > 0:
                try:
                    reason = reason.decode('utf8', errors='strict')
                except:
                    status = 1002
         else:
            status = 1002

         self.close(status, reason)
         return

      elif self.fin == 0:
          if self.opcode != STREAM:
              if self.opcode == PING or self.opcode == PONG:
                  raise Exception('control messages can not be fragmented')

              self.frag_type = self.opcode
              self.frag_start = True
              self.frag_decoder.reset()

              if self.frag_type == TEXT:
                  self.frag_buffer = []
                  utf_str = self.frag_decoder.decode(self.data, final = False)
                  if utf_str:
                      self.frag_buffer.append(utf_str)
              else:
                  self.frag_buffer = bytearray()
                  self.frag_buffer.extend(self.data)

          else:
              if self.frag_start is False:
                  raise Exception('fragmentation protocol error')

              if self.frag_type == TEXT:
                  utf_str = self.frag_decoder.decode(self.data, final = False)
                  if utf_str:
                      self.frag_buffer.append(utf_str)
              else:
                  self.frag_buffer.extend(self.data)

      else:
          if self.opcode == STREAM:
              if self.frag_start is False:
                  raise Exception('fragmentation protocol error')

              if self.frag_type == TEXT:
                  utf_str = self.frag_decoder.decode(self.data, final = True)
                  self.frag_buffer.append(utf_str)
                  self.data = u''.join(self.frag_buffer)
              else:
                  self.frag_buffer.extend(self.data)
                  self.data = self.frag_buffer

              self.handleMessage()

              self.frag_decoder.reset()
              self.frag_type = BINARY
              self.frag_start = False
              self.frag_buffer = None

          elif self.opcode == PING:
              self._sendMessage(False, PONG, self.data)

          elif self.opcode == PONG:
              pass

          else:
              if self.frag_start is True:
                  raise Exception('fragmentation protocol error')

              if self.opcode == TEXT:
                  try:
                      self.data = self.data.decode('utf8', errors='strict')
                  except Exception as exp:
                      raise Exception('invalid utf-8 payload')

              self.handleMessage()


   def _handleData(self):
      # do the HTTP header and handshake
      if self.handshaked is False:

         data = self.client.recv(self.headertoread)
         if not data:
            raise Exception('remote socket closed')

         else:
            # accumulate
            self.headerbuffer.extend(data)

            if len(self.headerbuffer) >= self.maxheader:
               raise Exception('header exceeded allowable size')

            # indicates end of HTTP header
            if b'\r\n\r\n' in self.headerbuffer:
               self.request = HTTPRequest(self.headerbuffer)

               # handshake rfc 6455
               try:
                  key = self.request.headers['Sec-WebSocket-Key']
                  k = key.encode('ascii') + GUID_STR.encode('ascii')
                  k_s = base64.b64encode(hashlib.sha1(k).digest()).decode('ascii')
                  hStr = HANDSHAKE_STR % {'acceptstr': k_s}
                  self.sendq.append((BINARY, hStr.encode('ascii')))
                  self.handshaked = True
                  self.handleConnected()
               except Exception as e:
                  hStr = FAILED_HANDSHAKE_STR
                  self._sendBuffer(hStr.encode('ascii'), True)
                  self.client.close()
                  raise Exception('handshake failed: %s', str(e))

      # else do normal data
      else:
         data = self.client.recv(16384)
         if not data:
            raise Exception("remote socket closed")

         if VER >= 3:
             for d in data:
                 self._parseMessage(d)
         else:
             for d in data:
                 self._parseMessage(ord(d))

   def close(self, status = 1000, reason = u''):
       """
          Send Close frame to the client. The underlying socket is only closed
          when the client acknowledges the Close frame.

          status is the closing identifier.
          reason is the reason for the close.
        """
       try:
          if self.closed is False:
            close_msg = bytearray()
            close_msg.extend(struct.pack("!H", status))
            if _check_unicode(reason):
                close_msg.extend(reason.encode('utf-8'))
            else:
                close_msg.extend(reason)

            self._sendMessage(False, CLOSE, close_msg)

       finally:
            self.closed = True


   def _sendBuffer(self, buff, send_all = False):
      size = len(buff)
      tosend = size
      already_sent = 0

      while tosend > 0:
         try:
            # i should be able to send a bytearray
            sent = self.client.send(buff[already_sent:])
            if sent == 0:
               raise RuntimeError('socket connection broken')

            already_sent += sent
            tosend -= sent

         except socket.error as e:
            # if we have full buffers then wait for them to drain and try again
            if e.errno in [errno.EAGAIN, errno.EWOULDBLOCK]:
               if send_all:
                   continue
               return buff[already_sent:]
            else:
               raise e

      return None

   def sendFragmentStart(self, data):
      """
          Send the start of a data fragment stream to a websocket client.
          Subsequent data should be sent using sendFragment().
          A fragment stream is completed when sendFragmentEnd() is called.

          If data is a unicode object then the frame is sent as Text.
          If the data is a bytearray object then the frame is sent as Binary.
      """
      opcode = BINARY
      if _check_unicode(data):
         opcode = TEXT
      self._sendMessage(True, opcode, data)

   def sendFragment(self, data):
      """
          see sendFragmentStart()

          If data is a unicode object then the frame is sent as Text.
          If the data is a bytearray object then the frame is sent as Binary.
      """
      self._sendMessage(True, STREAM, data)

   def sendFragmentEnd(self, data):
      """
          see sendFragmentEnd()

          If data is a unicode object then the frame is sent as Text.
          If the data is a bytearray object then the frame is sent as Binary.
      """
      self._sendMessage(False, STREAM, data)

   def sendMessage(self, data):
      """
          Send websocket data frame to the client.

          If data is a unicode object then the frame is sent as Text.
          If the data is a bytearray object then the frame is sent as Binary.
      """
      opcode = BINARY
      if _check_unicode(data):
         opcode = TEXT
      self._sendMessage(False, opcode, data)


   def _sendMessage(self, fin, opcode, data):

        payload = bytearray()

        b1 = 0
        b2 = 0
        if fin is False:
           b1 |= 0x80
        b1 |= opcode

        if _check_unicode(data):
           data = data.encode('utf-8')

        length = len(data)
        payload.append(b1)

        if length <= 125:
           b2 |= length
           payload.append(b2)

        elif length >= 126 and length <= 65535:
           b2 |= 126
           payload.append(b2)
           payload.extend(struct.pack("!H", length))

        else:
           b2 |= 127
           payload.append(b2)
           payload.extend(struct.pack("!Q", length))

        if length > 0:
           payload.extend(data)

        self.sendq.append((opcode, payload))


   def _parseMessage(self, byte):
      # read in the header
      if self.state == HEADERB1:

         self.fin = byte & 0x80
         self.opcode = byte & 0x0F
         self.state = HEADERB2

         self.index = 0
         self.length = 0
         self.lengtharray = bytearray()
         self.data = bytearray()

         rsv = byte & 0x70
         if rsv != 0:
            raise Exception('RSV bit must be 0')

      elif self.state == HEADERB2:
         mask = byte & 0x80
         length = byte & 0x7F

         if self.opcode == PING and length > 125:
             raise Exception('ping packet is too large')

         if mask == 128:
            self.hasmask = True
         else:
            self.hasmask = False

         if length <= 125:
            self.length = length

            # if we have a mask we must read it
            if self.hasmask is True:
               self.maskarray = bytearray()
               self.state = MASK
            else:
               # if there is no mask and no payload we are done
               if self.length <= 0:
                  try:
                     self._handlePacket()
                  finally:
                     self.state = HEADERB1
                     self.data = bytearray()

               # we have no mask and some payload
               else:
                  #self.index = 0
                  self.data = bytearray()
                  self.state = PAYLOAD

         elif length == 126:
            self.lengtharray = bytearray()
            self.state = LENGTHSHORT

         elif length == 127:
            self.lengtharray = bytearray()
            self.state = LENGTHLONG


      elif self.state == LENGTHSHORT:
         self.lengtharray.append(byte)

         if len(self.lengtharray) > 2:
            raise Exception('short length exceeded allowable size')

         if len(self.lengtharray) == 2:
            self.length = struct.unpack_from('!H', self.lengtharray)[0]

            if self.hasmask is True:
               self.maskarray = bytearray()
               self.state = MASK
            else:
               # if there is no mask and no payload we are done
               if self.length <= 0:
                  try:
                     self._handlePacket()
                  finally:
                     self.state = HEADERB1
                     self.data = bytearray()

               # we have no mask and some payload
               else:
                  #self.index = 0
                  self.data = bytearray()
                  self.state = PAYLOAD

      elif self.state == LENGTHLONG:

         self.lengtharray.append(byte)

         if len(self.lengtharray) > 8:
            raise Exception('long length exceeded allowable size')

         if len(self.lengtharray) == 8:
            self.length = struct.unpack_from('!Q', self.lengtharray)[0]

            if self.hasmask is True:
               self.maskarray = bytearray()
               self.state = MASK
            else:
               # if there is no mask and no payload we are done
               if self.length <= 0:
                  try:
                     self._handlePacket()
                  finally:
                     self.state = HEADERB1
                     self.data = bytearray()

               # we have no mask and some payload
               else:
                  #self.index = 0
                  self.data = bytearray()
                  self.state = PAYLOAD

      # MASK STATE
      elif self.state == MASK:
         self.maskarray.append(byte)

         if len(self.maskarray) > 4:
            raise Exception('mask exceeded allowable size')

         if len(self.maskarray) == 4:
            # if there is no mask and no payload we are done
            if self.length <= 0:
               try:
                  self._handlePacket()
               finally:
                  self.state = HEADERB1
                  self.data = bytearray()

            # we have no mask and some payload
            else:
               #self.index = 0
               self.data = bytearray()
               self.state = PAYLOAD

      # PAYLOAD STATE
      elif self.state == PAYLOAD:
         if self.hasmask is True:
            self.data.append( byte ^ self.maskarray[self.index % 4] )
         else:
            self.data.append( byte )

         # if length exceeds allowable size then we except and remove the connection
         if len(self.data) >= self.maxpayload:
            raise Exception('payload exceeded allowable size')

         # check if we have processed length bytes; if so we are done
         if (self.index+1) == self.length:
            try:
               self._handlePacket()
            finally:
               #self.index = 0
               self.state = HEADERB1
               self.data = bytearray()
         else:
            self.index += 1


class SimpleWebSocketServer(object):
   def __init__(self, host, port, websocketclass, selectInterval = 0.1):
      self.websocketclass = websocketclass

      if (host == ''):
         host = None

      if host is None:
         fam = socket.AF_INET6
      else:
         fam = 0

      hostInfo = socket.getaddrinfo(host, port, fam, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_PASSIVE)
      self.serversocket = socket.socket(hostInfo[0][0], hostInfo[0][1], hostInfo[0][2])
      self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.serversocket.bind(hostInfo[0][4])
      self.serversocket.listen(5)
      self.selectInterval = selectInterval
      self.connections = {}
      self.listeners = [self.serversocket]

   def _decorateSocket(self, sock):
      return sock

   def _constructWebSocket(self, sock, address):
      return self.websocketclass(self, sock, address)

   def close(self):
      self.serversocket.close()

      for desc, conn in self.connections.items():
         conn.close()
         self._handleClose(conn)

   def _handleClose(self, client):
      client.client.close()
      # only call handleClose when we have a successful websocket connection
      if client.handshaked:
         try:
            client.handleClose()
         except:
            pass

   def serveonce(self):
      writers = []
      for fileno in self.listeners:
         if fileno == self.serversocket:
            continue
         client = self.connections[fileno]
         if client.sendq:
            writers.append(fileno)

      rList, wList, xList = select(self.listeners, writers, self.listeners, self.selectInterval)

      for ready in wList:
         client = self.connections[ready]
         try:
            while client.sendq:
               opcode, payload = client.sendq.popleft()
               remaining = client._sendBuffer(payload)
               if remaining is not None:
                   client.sendq.appendleft((opcode, remaining))
                   break
               else:
                   if opcode == CLOSE:
                      raise Exception('received client close')

         except Exception as n:
            self._handleClose(client)
            del self.connections[ready]
            self.listeners.remove(ready)

      for ready in rList:
         if ready == self.serversocket:
            sock = None
            try:
               sock, address = self.serversocket.accept()
               newsock = self._decorateSocket(sock)
               newsock.setblocking(0)
               fileno = newsock.fileno()
               self.connections[fileno] = self._constructWebSocket(newsock, address)
               self.listeners.append(fileno)
            except Exception as n:
               if sock is not None:
                  sock.close()
         else:
            if ready not in self.connections:
                continue
            client = self.connections[ready]
            try:
               client._handleData()
            except Exception as n:
               self._handleClose(client)
               del self.connections[ready]
               self.listeners.remove(ready)

      for failed in xList:
         if failed == self.serversocket:
            self.close()
            raise Exception('server socket failed')
         else:
            if failed not in self.connections:
               continue
            client = self.connections[failed]
            self._handleClose(client)
            del self.connections[failed]
            self.listeners.remove(failed)

   def serveforever(self):
      while True:
         self.serveonce()

class SimpleSSLWebSocketServer(SimpleWebSocketServer):

   def __init__(self, host, port, websocketclass, certfile = None,
                keyfile = None, version = ssl.PROTOCOL_TLSv1, selectInterval = 0.1, ssl_context = None):

      SimpleWebSocketServer.__init__(self, host, port,
                                        websocketclass, selectInterval)

      if ssl_context is None:
         self.context = ssl.SSLContext(version)
         self.context.load_cert_chain(certfile, keyfile)
      else:
         self.context = ssl_context

   def close(self):
      super(SimpleSSLWebSocketServer, self).close()

   def _decorateSocket(self, sock):
      sslsock = self.context.wrap_socket(sock, server_side=True)
      return sslsock

   def _constructWebSocket(self, sock, address):
      ws = self.websocketclass(self, sock, address)
      ws.usingssl = True
      return ws

   def serveforever(self):
      super(SimpleSSLWebSocketServer, self).serveforever()


#### g2d-ws

class SocketHandler(WebSocket):
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

def start_websocket():
    server = SimpleWebSocketServer("localhost", 7574, SocketHandler)
    server.closing = False
    while not server.closing:
        server.serveonce()
