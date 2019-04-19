// +build js

package g2d

import (
    "fmt"
    "github.com/gopherjs/gopherjs/js"
)

var doc = js.Global.Get("document")

func init() {
    js.Global.Set("invokeExternal", handleData)
    out := doc.Call("getElementById", "output")
    out.Set("innerHTML", "")
    elem := doc.Call("createElement", "SCRIPT")
    elem.Set("innerHTML", script)
    doc.Call("getElementsByTagName", "body").Call("item", 0).Call("appendChild", elem)
}

func Prompt(a ...interface{}) string {
    UpdateCanvas()
    return js.Global.Call("prompt", fmt.Sprint(a...)).String()
}

func Confirm(a ...interface{}) bool {
    UpdateCanvas()
    return js.Global.Call("confirm", fmt.Sprint(a...)).Bool()
}

func Alert(a ...interface{}) {
    UpdateCanvas()
    js.Global.Call("alert", fmt.Sprint(a...))
}

func Println(a ...interface{}) {
    //fmt.Println(a...)
    out := doc.Call("getElementById", "output")
    txt := out.Get("innerHTML").String()
    txt += "<pre>" + fmt.Sprint(a...) + "</pre>"
    out.Set("innerHTML", txt)
    out.Set("scrollTop", out.Get("scrollHeight"))
}

func InitCanvas(size Size) {
    doJs("initCanvas(%d, %d)", size.W, size.H)
    UpdateCanvas()
}

func evalJs(code string) {
    js.Global.Call("eval", code)
}

func waitDone() {
}
