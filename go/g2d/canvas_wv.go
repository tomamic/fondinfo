// +build !js

package g2d

import (
    "fmt"
    "github.com/gen2brain/dlgs"
    "github.com/zserge/webview"
    "log"
    "net"
    "net/http"
    "os"
    "strings"
)

var (
    w                    webview.WebView = nil
    usrKeydown, usrKeyup func(string)
    usrUpdate            func()
    keyPressed           = make(map[string]interface{})
    mousePos             = Point{0, 0}
    mouseCodes           = []string{"LeftButton", "MiddleButton", "RightButton"}
    done                 = make(chan bool, 1)
    js                   = make([]string, 0)
)

var indexHTML = `
<!doctype html>
<html>
    <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <style>* { margin: 0; padding: 0; box-sizing: border-box; overflow: hidden; }</style>
    </head>
    <body>
        <canvas id="canvas" width="%d" height="%d">
            Your browser doesn't support HTML5 canvas element.
        </canvas>
        <script type="text/javascript">
            loaded = {};
            keyPressed = {};
            mouseCodes = ["LeftButton", "MiddleButton", "RightButton"];
            canvas = document.getElementById('canvas');
            ctx = canvas.getContext('2d');
            timer = -1;

            function clearCanvas() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            }
            function setColor(r, g, b) {
                ctx.strokeStyle = "rgb("+r+", "+g+", "+b+")";
                ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
            }
            function drawLine(x1, x1, x2, y2) {
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
            function loadImage(src) {
                img = document.createElement("IMG");
                img.src = src;
                loaded[src] = img;
            }
            function drawImage(src, x, y) {
                img = loaded[src];
                ctx.drawImage(img, x, y);
            }
            function drawImageClip(src, x0, y0, w0, h0, x1, y1, w1, h1) {
                img = loaded[src];
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
            function loadAudio(src) {
                audio = document.createElement("AUDIO");
                audio.src = src;
                loaded[src] = audio;
            }
            function playAudio(src, loop) {
                audio = loaded[src];
                audio.loop = loop;
                audio.play();
            }
            function pauseAudio(src) {
                audio = loaded[src];
                audio.pause();
            }

            function mainLoop(fps) {
                document.onkeydown = function(e) {
                    if (keyPressed[e.key]) return;
                    keyPressed[e.key] = true
                    window.external.invoke('keydown ' + e.key);
                };
                document.onkeyup = function(e) {
                    if (keyPressed[e.key]) keyPressed[e.key] = false;
                    window.external.invoke('keyup ' + e.key);
                };
                document.onmousedown = function(e) {
                    if (0 <= e.button && e.button < 3) {
                        window.external.invoke('keydown ' + mouseCodes[e.button]);
                    }
                };
                document.onmouseup = function(e) {
                    if (0 <= e.button && e.button < 3) {
                        window.external.invoke('keyup ' + mouseCodes[e.button]);
                    }
                };
                document.onmousemove = function(e) {
                    window.external.invoke('mousemove ' + e.clientX + ' ' + e.clientY);
                };
                document.onfocus = function(e) {
                    keyPressed = {}
                };

                if (timer >= 0) {
                    clearInterval(timer);
                    timer = -1;
                }
                if (fps >= 0) {
                    timer = setInterval(function(e) {
                        window.external.invoke('update');
                    }, 1000/fps);
                }
            }
            /*setColor(100, 100, 100);
            fillCircle(100, 100, 50);*/
        </script>
    </body>
</html>
`

func startServer(size Size) string {
    ln, err := net.Listen("tcp", "127.0.0.1:0")
    if err != nil {
        log.Fatal(err)
    }
    go func() {
        defer ln.Close()
        http.HandleFunc("/index.html", func(w http.ResponseWriter, r *http.Request) {
            w.Write([]byte(fmt.Sprintf(indexHTML, size.W, size.H)))
        })
        http.Handle("/", http.FileServer(http.Dir(".")))
        log.Fatal(http.Serve(ln, nil))
    }()
    return "http://" + ln.Addr().String() + "/index.html"
}

func handleRPC(w webview.WebView, data string) {
    args := strings.Split(data, " ")
    if args[0] == "mousemove" {
        mousePos.X, mousePos.Y = ToInt(args[1]), ToInt(args[2])
    } else if args[0] == "keydown" && usrKeydown != nil {
        usrKeydown(args[1])
        UpdateCanvas()
    } else if args[0] == "keyup" && usrKeyup != nil {
        usrKeyup(args[1])
        UpdateCanvas()
    } else if args[0] == "update" && usrUpdate != nil {
        usrUpdate()
        UpdateCanvas()
    }
}

func doJs(cmd string, a ...interface{}) {
    js = append(js, fmt.Sprintf(cmd+";\n", a...))
}

func Prompt(a ...interface{}) string {
    if w != nil {
        UpdateCanvas()
    }
    val, _, _ := dlgs.Entry("", fmt.Sprint(a...), "")
    return val
}

func Confirm(a ...interface{}) bool {
    if w != nil {
        UpdateCanvas()
    }
    val, _ := dlgs.Question("", fmt.Sprint(a...), true)
    return val
}

func Alert(a ...interface{}) {
    if w != nil {
        UpdateCanvas()
    }
    dlgs.Info("", fmt.Sprint(a...))
    //fmt.Println(a...)
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

func FillCircle(p Point, r int) {
    doJs("fillCircle(%d, %d, %d)", p.X, p.Y, r)
}

func FillRect(r Rect) {
    doJs("fillRect(%d, %d, %d, %d)", r.X, r.Y, r.W, r.H)
}

func LoadImage(src string) string {
    if _, err := os.Stat(src); err != nil {
        src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/" + src
    }
    doJs("loadImage('%s')", src)
    return src
}

func DrawImage(src string, p Point) {
    doJs("drawImage('%s', %d, %d)", src, p.X, p.Y)
}

func DrawImageClip(src string, clip Rect, r Rect) {
    doJs("drawImageClip('%s', %d, %d, %d, %d, %d, %d, %d, %d)",
        src, clip.X, clip.Y, clip.W, clip.H, r.X, r.Y, r.W, r.H)
}

func DrawText(txt string, p Point, size int) {
    doJs("drawText('%s', %d, %d, %d)", txt, p.X, p.Y, size)
}

func DrawTextCentered(txt string, p Point, size int) {
    doJs("drawTextCentered('%s', %d, %d, %d)", txt, p.X, p.Y, size)
}

func LoadAudio(src string) string {
    doJs("loadAudio('%s', %d, %d, %d)", src)
    return src
}

func PlayAudio(audio string, loop bool) {
    doJs("playAudio('%s', %t)", audio, loop)
}

func PauseAudio(audio string) {
    doJs("pauseAudio('%s')", audio)
}

func HandleEvents(update func(), keyFuncs ...func(string)) {
    usrUpdate, usrKeydown, usrKeyup = update, nil, nil
    if len(keyFuncs) >= 2 {
        usrKeydown, usrKeyup = keyFuncs[0], keyFuncs[1]
    } else if len(keyFuncs) == 1 {
        usrKeydown = keyFuncs[0]
    }
}

func MousePosition() Point {
    return mousePos
}

func InitCanvas(size Size) {
    go func() {
        index := startServer(size)
        /*html := "data:text/html," + url.PathEscape(
            fmt.Sprintf(indexHTML, size.W, size.H))*/
        w = webview.New(webview.Settings{
            Width:                  size.W,
            Height:                 size.H,
            Title:                  "G2D WebView",
            URL:                    index,
            ExternalInvokeCallback: handleRPC,
        })
        done <- true
        defer w.Exit()
        w.Run()
        done <- true
    }()
    <-done
}

func UpdateCanvas() {
    code := strings.Join(js, "")
    w.Dispatch(func() { w.Eval(code) })
    js = make([]string, 0)
}

func MainLoop(fps ...int) {
    UpdateCanvas()
    fps_ := 60
    if len(fps) > 0 {
        fps_ = fps[0]
    }
    w.Dispatch(func() {
        w.Eval(fmt.Sprintf(
            `mainLoop(%d);`, fps_))
    })
    <-done
}

func CloseCanvas() {
    HandleEvents(nil, nil, nil)
    MainLoop()
}
