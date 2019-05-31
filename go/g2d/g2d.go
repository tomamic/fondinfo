package g2d

import (
    "crypto/sha1"
    "fmt"
    "math/rand"
    "strings"
    "time"
)

type Point struct{ X, Y int }
type Size struct{ W, H int }
type Rect struct{ X, Y, W, H int }
type Color struct{ R, G, B int }

var frameRate = 30.0
var usrTick func()
var mousePos = Point{0, 0}
var keys = make(map[string]bool)
var prevKeys = make(map[string]bool)
var jss = make([]string, 0)
var answers = make([]string, 0)
var inited, done = false, false
var script = `
window.onload = function(e) { setTimeout("invokeExternal('connect')", 100); }
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
    ans = prompt(message, "");
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
            invokeExternal("tick");
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
`

func init() {
    rand.Seed(time.Now().UnixNano())
}

func ToInt(text string) int {
    val := 0
    fmt.Sscan(text, &val)
    return val
}

func ToFloat(text string) float64 {
    val := 0.0
    fmt.Sscan(text, &val)
    return val
}

func RandInt(min, max int) int {
    return rand.Intn(max-min+1) + min
}

func SetColor(c Color) {
    doJs("setColor(%d, %d, %d)", c.R, c.G, c.B)
}

func ClearCanvas() {
    doJs("clearCanvas()")
}

func DrawLine(pt1, pt2 Point) {
    doJs("drawLine(%d, %d, %d, %d)", pt1.X, pt1.Y, pt2.X, pt2.Y)
}

func FillCircle(center Point, r int) {
    doJs("fillCircle(%d, %d, %d)", center.X, center.Y, r)
}

func FillRect(r Rect) {
    doJs("fillRect(%d, %d, %d, %d)", r.X, r.Y, r.W, r.H)
}

func LoadImage(src string) string {
    key := fmt.Sprintf("%x", sha1.Sum([]byte(src)))
    doJs("loadImage('%s', '%s')", key, src)
    return key
}

func DrawImage(image string, p Point) {
    doJs("drawImage('%s', %d, %d)", image, p.X, p.Y)
}

// Clip a rectangular area from an image
// and draw it at the specified position
func DrawImageClip(image string, clip Rect, r Rect) {
    doJs("drawImageClip('%s', %d, %d, %d, %d, %d, %d, %d, %d)",
        image, clip.X, clip.Y, clip.W, clip.H, r.X, r.Y, r.W, r.H)
}

func DrawText(txt string, p Point, size int) {
    doJs("drawText('%s', %d, %d, %d)", txt, p.X, p.Y, size)
}

func DrawTextCentered(txt string, p Point, size int) {
    doJs("drawTextCentered('%s', %d, %d, %d)", txt, p.X, p.Y, size)
}

func LoadAudio(src string) string {
    key := fmt.Sprintf("%x", sha1.Sum([]byte(src)))
    doJs("loadAudio('%s')", key, src)
    return key
}

func PlayAudio(audio string, loop bool) {
    doJs("playAudio('%s', %t)", audio, loop)
}

func PauseAudio(audio string) {
    doJs("pauseAudio('%s')", audio)
}

func MousePosition() Point {
    return mousePos
}

func KeyPressed(key string) bool {
    return keys[key] && !prevKeys[key];
}

func KeyReleased(key string) bool {
    return !keys[key] && prevKeys[key];
}

func SetFrameRate(fps float64) {
    frameRate = fps
}

func UpdateCanvas() {
    if !inited {
        InitCanvas(Size{800, 600})
    }
    code := strings.Join(jss, "")
    //Println(code)
    evalJs(code)
    jss = make([]string, 0)
}

func MainLoop(tick ...func()) {
    if len(tick) == 1 {
        usrTick = tick[0]
    }
    if !done {
        doJs("mainLoop(%f)", frameRate)
        UpdateCanvas()
        waitDone()
        done = true
    }
}

func CloseCanvas() {
    usrTick = nil
    doJs("closeCanvas()")
    UpdateCanvas()
    terminate()
}

func doJs(cmd string, a ...interface{}) {
    jss = append(jss, fmt.Sprintf(cmd+";\n", a...))
}

func handleData(data string) {
    //Println(data)
    args := strings.Split(data, " ")
    if args[0] == "mousemove" {
        mousePos.X, mousePos.Y = ToInt(args[1]), ToInt(args[2])
    } else if args[0] == "keydown" {
        keys[args[1]] = true
    } else if args[0] == "keyup" {
        delete(keys, args[1])
    } else if args[0] == "tick" && usrTick != nil {
        usrTick()
        UpdateCanvas()
        prevKeys = make(map[string]bool)
        for k, v := range keys {
            prevKeys[k] = v
        }
    } else if args[0] == "answer" {
        ans := strings.SplitN(data, " ", 2)[1]
        answers = append(answers, ans)
    } else if args[0] == "connect" {
        inited = true
    }
}
