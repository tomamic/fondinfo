// +build !js

package g2d

import (
    "fmt"
    "github.com/gen2brain/dlgs"
    "github.com/zserge/webview"
    "log"
    "net"
    "net/http"
)

var (
    w                    webview.WebView = nil
    done                 = make(chan bool, 1)
)

var indexHTML = `
<!doctype html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<style>* { margin: 0; padding: 0; box-sizing: border-box; overflow: hidden; }</style>
</head>
<body>
<canvas id="g2d-canvas" width="%d" height="%d">
Your browser doesn't support HTML5 canvas element.
</canvas>
</body>
<script>
invokeExternal = window.external.invoke;
%s
</script>
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
            w.Write([]byte(fmt.Sprintf(indexHTML, size.W, size.H, script)))
        })
        http.Handle("/", http.FileServer(http.Dir(".")))
        log.Fatal(http.Serve(ln, nil))
    }()
    return "http://" + ln.Addr().String() + "/index.html"
}

func handleRPC(w webview.WebView, data string) {
    handleData(data)
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

func evalJs(code string) {
    w.Dispatch(func() { w.Eval(code) })
}

func waitDone() {
    <- done
}

func InitCanvas(size Size) {
    go func() {
        index := startServer(size)
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
    <- done
    doJs("initCanvas(%d, %d)", size.W, size.H)
    UpdateCanvas()
}

