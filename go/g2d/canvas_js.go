// +build js

package g2d

import (
    "fmt"
    "github.com/gopherjs/gopherjs/js"
    "math"
)

var doc = js.Global.Get("document")
var canvas *js.Object
var ctx *js.Object
var usrKeydown, usrKeyup func(string)
var usrUpdate func()
var keyPressed = make(map[string]interface{})
var mousePos = Point{0, 0}
var mouseCodes = []string{"LeftButton", "MiddleButton", "RightButton"}
var delay, timer = 1000/30, -1

func init() {
    out := doc.Call("getElementById", "output")
    out.Set("innerHTML", "")
}

func Prompt(a ...interface{}) string {
    return js.Global.Call("prompt", fmt.Sprint(a...)).String()
}

func Confirm(a ...interface{}) bool {
    return js.Global.Call("confirm", fmt.Sprint(a...)).Bool()
}

func Alert(a ...interface{}) {
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
    canvas = doc.Call("getElementById", "g2d-canvas")
    if canvas == nil {
        canvas = doc.Call("createElement", "canvas")
        canvas.Set("id", "g2d-canvas")
        canvas.Get("style").Set("background", "white")
        canvas.Get("style").Set("border", "1px solid silver")
        canvas.Get("style").Set("position", "absolute")
        canvas.Get("style").Set("right", "40px")
        canvas.Get("style").Set("top", "40px")
        canvas.Get("style").Set("z-index", "100")
        doc.Call("getElementsByTagName", "body").Call("item", 0).Call("appendChild", canvas)
    }
    ctx = canvas.Call("getContext", "2d")
    canvas.Set("width", size.W)
    canvas.Set("height", size.H)
    SetColor(Color{127, 127, 127})
    ClearCanvas()
}

func SetColor(c Color) {
    rgb := fmt.Sprintf("rgb(%d, %d, %d)", c.R, c.G, c.B)
    ctx.Set("strokeStyle", rgb)
    ctx.Set("fillStyle", rgb)
}

func ClearCanvas() {
    w := canvas.Get("width").Int()
    h := canvas.Get("height").Int()
    ctx.Call("clearRect", 0, 0, w, h)
}

func DrawLine(pt1, pt2 Point) {
    ctx.Call("moveTo", pt1.X, pt1.Y)
    ctx.Call("lineTo", pt2.X, pt2.Y)
    ctx.Call("stroke")
}

func FillCircle(p Point, r int) {
    ctx.Call("beginPath")
    ctx.Call("arc", p.X, p.Y, r, 0, 2*math.Pi)
    ctx.Call("closePath")
    ctx.Call("fill")
}

func FillRect(r Rect) {
    ctx.Call("fillRect", r.X, r.Y, r.W, r.H)
}

func LoadImage(src string) *js.Object {
    img := js.Global.Get("document").Call("createElement", "IMG")
    img.Set("src", src)
    return img
}

func DrawImage(img *js.Object, p Point) {
    ctx.Call("drawImage", img, p.X, p.Y)
}

func DrawImageClip(img *js.Object, clip Rect, r Rect) {
    ctx.Call("drawImage", img, clip.X, clip.Y, clip.W, clip.H, r.X, r.Y, r.W, r.H)
}

func DrawText(txt string, p Point, size int) {
    ctx.Set("font", fmt.Sprintf("%dpx sans-serif", size))

    // draw background rect assuming height of font
    /*
       width := ctx.Call("measureText", txt).Get("width").Int()
       ctx.Call("clearRect", p.X, p.Y, width, size)
    */

    ctx.Set("textBaseline", "top")
    ctx.Set("textAlign", "left")
    ctx.Call("fillText", txt, p.X, p.Y)
}

func DrawTextCentered(txt string, p Point, size int) {
    ctx.Set("font", fmt.Sprintf("%dpx sans-serif", size))

    // draw background rect assuming height of font
    /*
       width := ctx.Call("measureText", txt).Get("width").Int()
       ctx.Call("clearRect", p.X-width/2, p.Y-size/2, width, size)
    */

    ctx.Set("textBaseline", "middle")
    ctx.Set("textAlign", "center")
    ctx.Call("fillText", txt, p.X, p.Y)
}

func LoadAudio(src string) *js.Object {
    audio := js.Global.Get("document").Call("createElement", "AUDIO")
    audio.Set("src", src)
    return audio
}

func PlayAudio(audio *js.Object, loop bool) {
    audio.Set("loop", loop)
    audio.Call("play")
}

func PauseAudio(audio *js.Object) {
    audio.Call("pause")
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

func UpdateCanvas() {
}

func MainLoop(fps ...int) {
    doc.Set("onkeydown", g2dKeydown)
    doc.Set("onkeyup", g2dKeyup)
    doc.Set("onfocus", g2dFocus)
    doc.Set("onmousedown", g2dMousedown)
    doc.Set("onmouseup", g2dMouseup)
    doc.Set("onmousemove", g2dMousemove)

    if len(fps) > 0 {
        delay = 1000/fps[0]
    }
    if timer >= 0 {
        js.Global.Call("clearInterval", timer)
        timer = -1
    }
    if usrUpdate != nil {
        timer = js.Global.Call("setInterval", usrUpdate, delay).Int()
    }
}

func CloseCanvas() {
    HandleEvents(nil, nil, nil)
    MainLoop()
}

func g2dMousemove(e *js.Object) {
    rect := canvas.Call("getBoundingClientRect")
    mousePos.X = e.Get("clientX").Int() - rect.Get("left").Int()
    mousePos.Y = e.Get("clientY").Int() - rect.Get("top").Int()
}

func g2dMousedown(e *js.Object) {
    b := e.Get("button").Int()
    if 0 <= b && b < 3 {
        e.Set("code", mouseCodes[b])
        g2dKeydown(e)
    }
}

func g2dMouseup(e *js.Object) {
    b := e.Get("button").Int()
    if 0 <= b && b < 3 {
        e.Set("code", mouseCodes[b])
        g2dKeyup(e)
    }
}

func g2dKeydown(e *js.Object) {
    code := e.Get("code").String()
    _, pressed := keyPressed[code]
    if pressed {
        return
    }
    keyPressed[code] = true
    if usrKeydown != nil {
        usrKeydown(code)
    }
}

func g2dKeyup(e *js.Object) {
    code := e.Get("code").String()
    _, pressed := keyPressed[code]
    if pressed {
        delete(keyPressed, code)
    }
    if usrKeyup != nil {
        usrKeyup(code)
    }
}

func g2dFocus(e *js.Object) {
    keyPressed = make(map[string]interface{})
}
