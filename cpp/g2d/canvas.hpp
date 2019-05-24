#ifndef CANVAS_HPP
#define CANVAS_HPP

#include "websocket.hpp"
#include "actor.hpp"
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <sstream>
#include <thread>
#include <vector>

//using namespace std;
using std::function;
using std::ptr_fun;
using std::string;
using std::to_string;
using namespace std::string_literals;
using std::vector;
using std::ios;

static Point mouse_pos_;
static std::ostringstream jscode_;
static std::function<void()> usr_update_;
static std::function<void(string)> usr_keydown_;
static std::function<void(string)> usr_keyup_;
static vector<string> answers_, events_;
static bool inited_ = false;
static int max_w_ = 480, max_h_ = 360;
std::mutex mut_;
std::condition_variable cond_;

static string html_ = R"html(
<!DOCTYPE html>
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
        /*doSend("connect");*/
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
    /*doSend("disconnect");*/
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
    else if (k==" " || k=="Spacebar") k = "Space";
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
<body></body>
</html>
)html";

int randint(int min, int max) {
    return min + rand() % (1 + max - min);
}

static string url_encode(const string &value) {
  const char hex[] = "0123456789ABCDEF";
  string escaped;
  for (char c : value) {
    if (isalnum(c) || c == '-' || c == '_' || c == '.' || c == '~' ||
        c == '=') {
      escaped = escaped + c;
    } else {
      escaped = escaped + '%' + hex[(c >> 4) & 0xf] + hex[c & 0xf];
    }
  }
  return escaped;
}

string base64_encode(unsigned char* bytes_to_encode, unsigned int in_len) {
  string ret;
  int i = 0;
  int j = 0;
  unsigned char char_array_3[3];
  unsigned char char_array_4[4];

  static const string base64_chars =
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "abcdefghijklmnopqrstuvwxyz"
             "0123456789+/";

  while (in_len--) {
    char_array_3[i++] = *(bytes_to_encode++);
    if (i == 3) {
      char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
      char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
      char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
      char_array_4[3] = char_array_3[2] & 0x3f;

      for (i = 0; (i < 4) ; i++) {
        ret += base64_chars[char_array_4[i]];
      }
      i = 0;
    }
  }
  if (i) {
    for(j = i; j < 3; j++) {
      char_array_3[j] = '\0';
    }
    char_array_4[0] = ( char_array_3[0] & 0xfc) >> 2;
    char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
    char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);

    for (j = 0; (j < i + 1); j++) {
      ret += base64_chars[char_array_4[j]];
    }
    while (i++ < 3) {
      ret += '=';
    }
  }
  return ret;
}

void init_canvas(Size size);

bool inited() {
    std::unique_lock<std::mutex> mlock(mut_);
    return inited_;
}

void wait_inited(bool val) {
    std::unique_lock<std::mutex> mlock(mut_);
    cond_.wait(mlock, [=]() { return inited_ == val; } );
}

void set_inited(bool val) {
    std::lock_guard<std::mutex> guard(mut_);
    inited_ = val;
    cond_.notify_all();
}

void produce_msg(std::string msg, std::vector<string>& msgs) {
    std::lock_guard<std::mutex> guard(mut_);
    msgs.push_back(msg);
    cond_.notify_all();
}

std::string consume_msg(std::vector<string>& msgs) {
    std::unique_lock<std::mutex> mlock(mut_);
    if (msgs.size() == 0) {
        cond_.wait(mlock, [&]() { return msgs.size() > 0; } );
    }
    auto msg = msgs[0];
    msgs.erase(msgs.begin());
    return msg;
}

void handle_events(void (*update)(), void (*keydown)(string), void (*keyup)(string)) {
    usr_update_ = std::function<void()>(update);
    usr_keydown_ = std::function<void(string)>(keydown);
    usr_keyup_ = std::function<void(string)>(keyup);
}

void handle_events(std::function<void()> update, std::function<void(string)> keydown, std::function<void(string)> keyup) {
    usr_update_ = update;
    usr_keydown_ = keydown;
    usr_keyup_ = keyup;
}

void do_js_(string cmd, vector<string> strs, vector<int> ints) {
    std::istringstream fmt{cmd};
    string part;
    for (auto s : strs) {
        std::getline(fmt, part, '%');
        jscode_ << part << s;
    }
    for (auto a : ints) {
        std::getline(fmt, part, '%');
        jscode_ << part << a;
    }
    std::getline(fmt, part, '\0');
    jscode_ << part << ";\n";
}

void do_js_(string cmd, vector<int> args) {
    do_js_(cmd, {}, args);
}

void do_js_(string js) {
    jscode_ << js << ";\n";
}

void update_canvas() {
    if (inited()) {
        std::cout << "js: " << jscode_.str() << std::endl;
        ws_send(jscode_.str());
        jscode_.str("");
        jscode_.clear();
    }
}

void close_canvas() {
    if (inited()) {
        handle_events(nullptr, nullptr, nullptr);
        do_js_("closeCanvas()");
        update_canvas();
        /*webview_terminate(&wv_);*/
    }
}

void handle_event_(string evt) {
    std::cout << "event: " << evt << std::endl;
    auto cmd = evt.substr(0, evt.find(' '));
    if (cmd == "answer") {
        produce_msg(evt.substr(7, evt.npos), answers_);
    } else if (cmd == "connect") {
        set_inited(true);
    } else if (cmd == "disconnect") {
        set_inited(false);
    }
    produce_msg(evt, events_);
}

void main_loop(int fps=30) {
    if (!inited()) {
        init_canvas({480, 360});
    }
    do_js_("mainLoop(%)", {fps});
    update_canvas();

    while (inited()) {
        auto msg = consume_msg(events_);
        std::istringstream line{msg};
        string cmd; line >> cmd;
        if (cmd == "mousemove") {
            line >> mouse_pos_.x >> mouse_pos_.y;
        } else if (cmd == "keydown" && usr_keydown_ != nullptr) {
            string key; line >> key;
            usr_keydown_(key);
            update_canvas();
        } else if (cmd == "keyup" && usr_keyup_ != nullptr) {
            string key; line >> key;
            usr_keyup_(key);
            update_canvas();
        } else if (cmd == "update" && usr_update_ != nullptr) {
            usr_update_();
            update_canvas();
        }
    }
}

void set_color(Color c) {
    do_js_("setColor(%, %, %)", {c.r, c.g, c.b});
}

void clear_canvas() {
    do_js_("clearCanvas()");
}

void draw_line(Point pt1, Point pt2) {
    do_js_("drawLine(%, %, %, %)", {pt1.x, pt1.y, pt2.x, pt2.y});
}

void fill_circle(Point center, int r) {
    do_js_("fillCircle(%, %, %)", {center.x, center.y, r});
}

void fill_rect(Rect r) {
    do_js_("fillRect(%, %, %, %)", {r.x, r.y, r.w, r.h});
}

string load_image(string src) {
    auto key = to_string(std::hash<string>{}(src));
    do_js_("loadImage('%', '%')", {key, src}, {});
    return key;
}

void draw_image(string image, Point p) {
    do_js_("drawImage('%', %, %)", {image}, {p.x, p.y});
}

void draw_image_clip(string image, Rect clip, Rect r) {
    do_js_("drawImageClip('%', %, %, %, %, %, %, %, %)",
        {image}, {clip.x, clip.y, clip.w, clip.h, r.x, r.y, r.w, r.h});
}

void draw_text(string txt, Point p, int size) {
    do_js_("drawText('%', %, %, %)", {txt}, {p.x, p.y, size});
}

void draw_text_centered(string txt, Point p, int size) {
    do_js_("drawTextCentered('%', %, %, %)", {txt}, {p.x, p.y, size});
}

string load_audio(string src) {
    auto key = to_string(std::hash<string>{}(src));
    do_js_("loadAudio('%', '%')", {key, src}, {});
    return key;
}

void play_audio(string audio, bool loop) {
    if (loop) do_js_("pauseAudio('%', true)", {audio}, {});
    else do_js_("pauseAudio('%', false)", {audio}, {});
}

void pause_audio(string audio) {
    do_js_("pauseAudio('%')", {audio}, {});
}

string dialog_(string js) {
    if (!inited()) {
        init_canvas({480, 360});
    }
    do_js_(js);
    update_canvas();
    return consume_msg(answers_);
}

void alert(string message) {
    dialog_("doAlert('"s + message + "')"s);
}

bool confirm(string message) {
    return dialog_("doConfirm('"s + message + "')"s) == "true";
}

string prompt(string message) {
    return dialog_("doPrompt('"s + message + "')"s);
}

Point mouse_position() {
    return mouse_pos_;
}

void init_canvas(Size size) {
    if (!inited()) {
        srand(time(nullptr));
        { std::ofstream{"_websocket.html"} << html_; }
        ws_init(handle_event_);
        wait_inited(true);
    }
    do_js_("initCanvas(%, %)", {size.w, size.h});
    update_canvas();
}

#endif // CANVAS_HPP
