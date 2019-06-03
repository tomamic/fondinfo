// +build !js

package g2d

import (
    "fmt"
    //"github.com/gen2brain/dlgs"
    "github.com/zserge/webview"
    "log"
    "net"
    "net/http"
)

var w webview.WebView = nil

var indexHTML = `
<!doctype html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<style>
    body { margin: 0; padding: 0; }
    canvas { position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%);
             margin: 0; padding: 0; border: 1px solid silver; }
</style>
</head>
<body>
</body>
<script>
function invokeExternal(data) {
    window.external.invoke(data);
}
` + script + `
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
            w.Write([]byte(indexHTML))
        })
        http.Handle("/", http.FileServer(http.Dir(".")))
        log.Fatal(http.Serve(ln, nil))
    }()
    return "http://" + ln.Addr().String() + "/index.html"
}

func handleRPC(w webview.WebView, data string) {
    handleData(data)
}

func Println(a ...interface{}) {
    fmt.Println(a...)
}

func Printf(format string, a ...interface{}) {
    fmt.Printf(format, a...)
}

func dialog(cmd string, a ...interface{}) string {
    doJs(cmd+"('%s')", fmt.Sprint(a...))
    UpdateCanvas()
    for len(answers) == 0 {
        w.Loop(true)
    }
    ans := answers[0]
    answers = answers[1:]
    return ans
}

func Prompt(a ...interface{}) string {
    if !inited {
        Println(a...)
        line := ""
        fmt.Scanln(&line)
        return line
    }
    return dialog("doPrompt", a...)
    //if w != nil {
    //    UpdateCanvas()
    //}
    //val, _, _ := dlgs.Entry("", fmt.Sprint(a...), "")
    //return val
}

func Confirm(a ...interface{}) bool {
    return dialog("doConfirm", a...) == "true"
    //if w != nil {
    //    UpdateCanvas()
    //}
    //val, _ := dlgs.Question("", fmt.Sprint(a...), true)
    //return val
}

func Alert(a ...interface{}) {
    dialog("doAlert", a...)
    //if w != nil {
    //    UpdateCanvas()
    //}
    //dlgs.Info("", fmt.Sprint(a...))
}

func evalJs(code string) {
    w.Eval(code)
}

func waitDone() {
    if inited {
        defer w.Exit()
        w.Run()
    }
}

func terminate() {
    if inited {
        w.Terminate()
    }
}

func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}

func InitCanvas(size Size) {
    if !inited {
        index := startServer(size)
        fmt.Println(index)
        w = webview.New(webview.Settings{
            Width:                  max(size.W, 480),
            Height:                 max(size.H, 360),
            Title:                  "G2D WebView",
            URL:                    index,
            ExternalInvokeCallback: handleRPC,
        })
        for !inited {
            w.Loop(true)
        }
    }
    js := fmt.Sprintf("initCanvas(%d, %d);\n", size.W, size.H)
    jss = append([]string{js}, jss...)
    UpdateCanvas()
}
