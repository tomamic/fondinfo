#ifndef CANVAS_HPP
#define CANVAS_HPP
#define WEBVIEW_IMPLEMENTATION

#include "webview.hpp"
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

#if defined(WEBVIEW_WINAPI)
int main();
int WINAPI WinMain(HINSTANCE hInt, HINSTANCE hPrevInst, LPSTR lpCmdLine,
                   int nCmdShow) {
    return main();
}
#endif

//using namespace std;
using std::function;
using std::ptr_fun;
using std::string;
using std::to_string;
using namespace std::string_literals;
using std::vector;
using std::cout;
using std::endl;
using std::ios;

static struct webview wv_;
static Point mouse_pos_;
static std::ostringstream jscode_;
static std::function<void()> usr_update_;
static std::function<void(string)> usr_keydown_;
static std::function<void(string)> usr_keyup_;
static vector<string> dialogs_;
static bool inited_ = false;
static int max_w_ = 480, max_h_ = 360;

static string html_ = R"html(
<!doctype html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>G2D Canvas</title>
<style>
    body { margin: 0; padding: 0; }
    canvas { position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%);
             margin: 0; padding: 0; border: 1px solid silver; }
</style>
</head>
<body>
</body>
<script>
window.invokeExternal = function(data) {
    window.external.invoke(data);
}
window.onload = function(e) {
    setTimeout("invokeExternal('load')", 100);
}
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
    invokeExternal("dialog true");
}
function doConfirm(message) {
    ans = confirm(message);
    invokeExternal("dialog " + ans);
}
function doPrompt(message) {
    ans = prompt(message);
    invokeExternal("dialog " + ans);
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
        var rect = canvas.getBoundingClientRect();
        var x = Math.round(e.clientX - rect.left);
        var y = Math.round(e.clientY - rect.top);
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
        clearCanvas();
        /*canvas.parentNode.removeChild(canvas);
        delete canvas;*/
    }
}
</script>
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
    jscode_ << part << ";" << endl;
}

void do_js_(string cmd, vector<int> args) {
    do_js_(cmd, {}, args);
}

void do_js_(string js) {
    jscode_ << js << ";" << endl;
}

void update_canvas() {
    if (inited_) {
        //cout << jscode_.str() << endl;
        webview_eval(&wv_, jscode_.str().c_str());
        jscode_.str("");
        jscode_.clear();
    }
}

void close_canvas() {
    if (inited_) {
        handle_events(nullptr, nullptr, nullptr);
        do_js_("closeCanvas()");
        update_canvas();
        webview_terminate(&wv_);
    }
}

void main_loop(int fps=30) {
    if (!inited_) {
        init_canvas({0, 0});
    }
    do_js_("mainLoop(%)", {fps});
    update_canvas();
    while (webview_loop(&wv_, 1) == 0) { }
    webview_exit(&wv_);
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
    std::ifstream file{src, ios::in|ios::binary|ios::ate};
    if (file.is_open()) {
        file.seekg(0, ios::end);
        auto size = file.tellg();
        file.seekg(0, ios::beg);
        auto data = new char[size];
        file.read(data, size);

        auto ext = src.substr(1 + src.find_last_of('.'));
        auto pre = "data:image/"s + ext + ";base64,"s;
        src = pre + base64_encode((unsigned char *)data, size);
        delete data;
    } else {
        src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/"s + src;
    }
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
    if (!inited_) {
        init_canvas({0, 0});
    }
    do_js_(js);
    update_canvas();
    while (dialogs_.size() == 0) {
        webview_loop(&wv_, false);
    }
    auto ans = dialogs_[0];
    dialogs_.erase(dialogs_.begin());
    return ans;
}

void alert(string message) {
    dialog_("doAlert('"s + message + "')"s);
    /*
    update_canvas();
    #if defined(WEBVIEW_WINAPI)
    system(("powershell -WindowStyle Hidden -Command \"[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic');$answer = [Microsoft.VisualBasic.Interaction]::MsgBox('"s + message + "', [microsoft.visualbasic.msgboxstyle]::Information -bor [microsoft.visualbasic.msgboxstyle]::OkOnly -bor [microsoft.visualbasic.msgboxstyle]::DefaultButton1, '');Write-Output $answer;\""s).c_str());
    #else
    system(("zenity --info --text=\""s + message + "\""s).c_str());
    #endif
    */
}

bool confirm(string message) {
    return dialog_("doConfirm('"s + message + "')"s) == "true";
    /*
    update_canvas();
    #if defined(WEBVIEW_WINAPI)
    system(("powershell -WindowStyle Hidden -Command \"[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic');$answer = [Microsoft.VisualBasic.Interaction]::MsgBox('"s + message + "', [microsoft.visualbasic.msgboxstyle]::Question -bor [microsoft.visualbasic.msgboxstyle]::OkCancel -bor [microsoft.visualbasic.msgboxstyle]::DefaultButton1, '');Write-Output $answer;\" >_dialog.txt"s).c_str());
    #else
    system(("if zenity --question --text=\""s + message + "\"; then echo Ok >_dialog.txt; else echo Cancel >_dialog.txt; fi"s).c_str());
    #endif
    std::ifstream file{"_dialog.txt"}; string answer; std::getline(file, answer);
    return answer.size() >= 2 && tolower(answer[0]) == 'o' && tolower(answer[1]) == 'k';
    */
}

string prompt(string message) {
    return dialog_("doPrompt('"s + message + "')"s);
    /*
    update_canvas();
    #if defined(WEBVIEW_WINAPI)
    system(("powershell -WindowStyle Hidden -Command \"[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic');$answer = [Microsoft.VisualBasic.Interaction]::InputBox('"s + message + "', '', '');Write-Output $answer;\" >_dialog.txt"s).c_str());
    #else
    system(("zenity --entry --title \"\" --text \""s + message + "\" --entry-text \"\" >_dialog.txt"s).c_str());
    #endif
    std::ifstream file{"_dialog.txt"}; string answer; std::getline(file, answer);
    return answer;
    */
}

Point mouse_position() {
    return mouse_pos_;
}

void handle_data_(string data) {
    //cout << data << endl;
    std::istringstream line{data};
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
    } else if (cmd == "dialog") {
        line.ignore();
        string ans; getline(line, ans);
        dialogs_.push_back(ans);
    } else if (cmd == "load") {
        inited_ = true;
    }
}


void external_cb_(struct webview *wv, const char *arg) {
    handle_data_(string{arg});
}

void init_canvas(Size size) {
    if (!inited_) {
        srand(time(nullptr));

        string html_data = "data:text/html,"s + url_encode(html_);

        wv_.title = "G2D WebView";
        #if defined(WEBVIEW_WINAPI)
        wv_.url = html_data.c_str();
        #else
        wv_.url = "about:blank";
        #endif
        wv_.width = size.w > max_w_ ? size.w : max_w_;
        wv_.height = size.h > max_h_ ? size.h : max_h_;
        wv_.resizable = 0;
        wv_.external_invoke_cb = external_cb_;
        webview_init(&wv_);

        #if !defined(WEBVIEW_WINAPI)
        auto js = "document.open('text/html', 'replace');\n"s
            + "document.write(`"s+html_+"`);\n"s
            + "document.close();\n"s;
        webview_eval(&wv_, js.c_str());
        #endif
        while (!inited_) {
            webview_loop(&wv_, true);
        }
    }
    do_js_("initCanvas(%, %)", {size.w, size.h});
    update_canvas();
}

#endif // CANVAS_HPP
