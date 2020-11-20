/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef CANVAS_HPP
#define CANVAS_HPP

#include "websocket.hpp"
#include "basic.hpp"
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <sstream>
#include <thread>
#include <vector>

namespace g2d {

using std::string;
using namespace std::string_literals;

static Point mouse_pos_{0, 0};
static Point size_{640, 480};

static std::set<string> pressed_;
static std::set<string> released_;

static std::ostringstream jscode_;
static std::function<void()> usr_tick_;
static string answer_ = "";
static bool inited_ = false;
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

loaded = {};
keyCodes = {"Up": "ArrowUp", "Down": "ArrowDown", "Left": "ArrowLeft", "Right": "ArrowRight",
            " ": "Spacebar", "Space": "Spacebar", "Esc": "Escape", "Del": "Delete"}
mouseCodes = ["LeftButton", "MiddleButton", "RightButton"];

window.addEventListener("load", () => {
    canvas = document.getElementById("g2d-canvas");
    ctx = canvas.getContext("2d");
    ctx.strokeStyle = `rgb(127, 127, 127)`;
    ctx.fillStyle = `(127, 127, 127)`;
    websocket = new WebSocket("ws://localhost:%PORT%/");
    websocket.onopen = (evt) => { };
    websocket.onclose = (evt) => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        open("about:blank", "_self").close();
    };
    websocket.onmessage = (evt) => { eval(evt.data); };
    websocket.onerror = (evt) => { websocket.close(); };
    document.onfocus = (evt) => { };
    document.onkeydown = (evt) => {
        if (evt.repeat) return;
        var k = keyCodes[evt.key] || evt.key;
        websocket.send("keydown " + k);
    };
    document.onkeyup = (evt) => {
        var k = keyCodes[evt.key] || evt.key;
        websocket.send("keyup " + k);
    };
    canvas.onmousemove = (evt) => {
        var rect = canvas.getBoundingClientRect();
        var x = Math.round(evt.clientX - rect.left);
        var y = Math.round(evt.clientY - rect.top);
        websocket.send("mousemove " + x + " " + y);
    };
    canvas.onmousedown = (evt) => {
        websocket.send("keydown " + mouseCodes[Math.min(evt.button, 2)]);
    };
    canvas.onmouseup = (evt) => {
        websocket.send("keyup " + mouseCodes[Math.min(evt.button, 2)]);
    };
});

function loadElement(tag, src) {
    var elem = loaded[src];
    if (elem) return elem;
    elem = document.createElement(tag);
    elem.src = src;
    elem.onerror = () => {
        if (!elem.src.startsWith("https://raw.github")) {
            elem.src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/" + src;
        }
    }
    loaded[src] = elem;
    return elem;
}
</script>
</head>
<body><canvas id="g2d-canvas" width="%WIDTH%" height="%HEIGHT%"></canvas></body>
</html>
)html";

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

void init_canvas(Point size);

bool inited() {
    std::unique_lock<std::mutex> mlock(mut_);
    return inited_;
}

void do_js_(string cmd, std::vector<string> strs, std::vector<int> ints) {
    std::istringstream fmt{cmd};
    string part;
    for (auto s : strs) {
        std::getline(fmt, part, '%');
        std::replace(begin(s), end(s), '`', '\'');
        jscode_ << part << s;
    }
    for (auto a : ints) {
        std::getline(fmt, part, '%');
        jscode_ << part << a;
    }
    std::getline(fmt, part, '\0');
    jscode_ << part << ";\n";
}

void do_js_(string cmd, std::vector<int> args) {
    do_js_(cmd, {}, args);
}

void do_js_(string js) {
    jscode_ << js << ";\n";
}

void update_canvas() {
    {
        std::lock_guard<std::mutex> guard(mut_);
        answer_ = "";
        pressed_.clear();
        released_.clear();
    }
    if (!inited()) { init_canvas(size_); }
    //std::cout << "js: " << jscode_.str() << std::endl;
    ws::ws_send(jscode_.str());
    jscode_.str("");
    jscode_.clear();
}

void close_canvas() {
    if (inited()) {
        usr_tick_ = std::function<void()>(nullptr);
        do_js_("websocket.close()");
        update_canvas();
        /*webview_terminate(&wv_);*/
    }
}

void handle_event_(string evt) {
    std::lock_guard<std::mutex> guard(mut_);
    std::istringstream line{evt};
    string cmd; line >> cmd;
    if (cmd == "answer") {
        answer_ = evt.substr(6);
        cond_.notify_all();
    } else if (cmd == "connect") {
        inited_ = true;
        cond_.notify_all();
    } else if (cmd == "disconnect") {
        inited_ = false;
        cond_.notify_all();
    } else if (cmd == "mousemove") {
        line >> mouse_pos_.x >> mouse_pos_.y;
    } else if (cmd == "keydown" || cmd == "keyup") {
        string key; line >> key;
        if (key == "Spacebar") { key = " "; }
        auto& set_in = (cmd == "keyup") ? released_ : pressed_;
        auto& set_out = (cmd == "keyup") ? pressed_ : released_;
        if (set_out.count(key)) { set_out.erase(key); }
        else { set_in.insert(key); }
    }
}

Point mouse_position() {
    std::unique_lock<std::mutex> mlock(mut_);
    return mouse_pos_;
}

bool key_pressed(string key) {
    std::unique_lock<std::mutex> mlock(mut_);
    return pressed_.count(key);
}

bool key_released(string key) {
    std::unique_lock<std::mutex> mlock(mut_);
    return released_.count(key);
}

std::vector<string> pressed_keys() {
    std::unique_lock<std::mutex> mlock(mut_);
    return {pressed_.begin(), pressed_.end()};
}

std::vector<string> released_keys() {
    std::unique_lock<std::mutex> mlock(mut_);
    return {released_.begin(), released_.end()};
}

void main_loop(int fps=30) {
    update_canvas();
    while (inited()) {
        if (usr_tick_ != nullptr) { usr_tick_(); }
        update_canvas();
        std::this_thread::sleep_for(std::chrono::milliseconds(1000 / fps));
    }
    close_canvas();
}

void main_loop(void (*tick)(), int fps=30) {
    usr_tick_ = std::function<void()>(tick);
    main_loop(fps);
}

void main_loop(std::function<void()> tick, int fps=30) {
    usr_tick_ = tick;
    main_loop(fps);
}

void set_color(Color c) {
    do_js_("ctx.strokeStyle = `rgb(%, %, %)`", {c.r, c.g, c.b});
    do_js_("ctx.fillStyle = `rgb(%, %, %)`", {c.r, c.g, c.b});
}

void clear_canvas() {
    do_js_("ctx.clearRect(0, 0, canvas.width, canvas.height);");
}

void draw_line(Point pt1, Point pt2) {
    do_js_("ctx.beginPath(); ctx.moveTo(%, %); ctx.lineTo(%, %); ctx.stroke()",
        {pt1.x, pt1.y, pt2.x, pt2.y});
}

void fill_circle(Point center, int r) {
    do_js_("ctx.beginPath(); ctx.arc(%, %, %, 0, 2*Math.PI); ctx.closePath(); ctx.fill()",
    {center.x, center.y, r});
}

void fill_rect(Rect r) {
    do_js_("ctx.fillRect(%, %, %, %)", {r.x, r.y, r.w, r.h});
}

string load_image(string src) {
    do_js_("loadElement(`IMG`, `%`)", {src}, {});
    return src;
}

void draw_image(string src, Point p) {
    do_js_("ctx.drawImage(loadElement(`IMG`, `%`), %, %)", {src}, {p.x, p.y});
}

void draw_image_clip(string src, Rect clip, Rect r) {
    do_js_("ctx.drawImage(loadElement(`IMG`, `%`), %, %, %, %, %, %, %, %)",
        {src}, {clip.x, clip.y, clip.w, clip.h, r.x, r.y, r.w, r.h});
}

void draw_text(string txt, Point p, int size, string baseline="top", string align="left") {
    do_js_("ctx.font = `%px sans-serif`", {size});
    do_js_("ctx.textBaseline = `%`; ctx.textAlign = `%`", {baseline, align}, {});
    do_js_("ctx.fillText(`%`, %, %)", {txt}, {p.x, p.y});
}

void draw_text_centered(string txt, Point p, int size) {
   draw_text(txt, p, size, "middle", "center");
}

string load_audio(string src) {
    do_js_("loadElement(`AUDIO`, `%`)", {src}, {});
    return src;
}

void play_audio(string src, bool loop) {
    do_js_("loadElement(`AUDIO`, `%`).loop = %", {src, loop ? "true" : "false"}, {});
    do_js_("loadElement(`AUDIO`, `%`).play()", {src}, {});
}

void pause_audio(string src) {
    do_js_("loadElement(`AUDIO`, `%`)", {src}, {});
    do_js_("loadElement(`AUDIO`, `%`).pause()", {src}, {});
}

string dialog_(string dialog, string message) {
    do_js_("websocket.send(`answer ` + %(`%`))", {dialog, message}, {});
    update_canvas();

    std::unique_lock<std::mutex> mlock(mut_);
    while (answer_ == "") { cond_.wait(mlock); }
    return answer_.substr(1);
}

void alert(string message) {
    dialog_("alert", message);
}

bool confirm(string message) {
    return dialog_("confirm", message) == "true";
}

string prompt(string message) {
    return dialog_("prompt", message);
}

void init_canvas(Point size) {
    size_ = size;
    if (inited()) {
        do_js_("canvas.width = %; canvas.height = %", {size.x, size.y});
    } else {
        auto html = html_;
        html = html.replace(html.find("%PORT%"), 6, std::to_string(g2d::ws::ws_port_));
        html = html.replace(html.find("%WIDTH%"), 7, std::to_string(size.x));
        html = html.replace(html.find("%HEIGHT%"), 8, std::to_string(size.y));
        std::ofstream{"_websocket.html"} << html;
        ws::ws_init(handle_event_);
        std::unique_lock<std::mutex> mlock(mut_);
        while (!inited_) { cond_.wait(mlock); }
    }
}

Point canvas_size() {
    return size_;
}

}  // namespace g2d

#endif // CANVAS_HPP
