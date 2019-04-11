package g2d

import (
    "fmt"
    "github.com/gopherjs/gopherjs/js"
    "math"
)

type Point struct{ X, Y int }
type Size struct{ W, H int }
type Rect struct{ X, Y, W, H int }
type Color struct{ R, G, B int }

var doc = js.Global.Get("document")
var canvas *js.Object
var ctx *js.Object
var usrKeyDown func(string) = nil
var usrKeyUp func(string) = nil
var keyPressed = make(map[string]interface{})
var mousePos = Point{0, 0}
var mouseCodes = []string{"LeftButton", "MiddleButton", "RightButton"}
var timer = -1

func init() {
    out := doc.Call("getElementById", "output")
    out.Set("innerHTML", "")
}

func Prompt(a ...interface{}) string {
    return js.Global.Call("prompt", fmt.Sprint(a...)).String()
}

func Println(a ...interface{}) {
    //fmt.Println(a...)
    out := doc.Call("getElementById", "output")
    txt := out.Get("innerHTML").String()
    txt += "<pre>" + fmt.Sprint(a...) + "</pre>"
    out.Set("innerHTML", txt)
    out.Set("scrollTop", out.Get("scrollHeight"))
}

func Alert(a ...interface{}) {
    js.Global.Call("alert", fmt.Sprint(a...))
}

func ParseInt(text string) int {
    return js.Global.Call("parseInt", text).Int()
}

func ParseFloat(text string) float64 {
    return js.Global.Call("parseFloat", text).Float()
}

func Random() float64 {
    return js.Global.Get("Math").Call("random").Float()
}

func RandInt(min, max int) int {
    return int(Random() * float64(max - min + 1)) + min;
}

func InitCanvas(size Size) {
    canvas = doc.Call("getElementById", "g2d-canvas")
    if canvas == nil {
        canvas = doc.Call("createElement", "canvas");
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
}

func FillCanvas(c Color) {
    w := canvas.Get("width").Int()
    h := canvas.Get("height").Int()
    DrawRect(c, Rect{0, 0, w, h})
}

func DrawLine(c Color, pt1, pt2 Point) {
    ctx.Set("strokeStyle", fmt.Sprintf("rgb(%d, %d, %d)", c.R, c.G, c.B))
    ctx.Call("moveTo", pt1.X, pt1.Y)
    ctx.Call("lineTo", pt2.X, pt2.Y)
    ctx.Call("stroke")
}

func DrawCircle(c Color, p Point, r int) {
    ctx.Set("fillStyle", fmt.Sprintf("rgb(%d, %d, %d)", c.R, c.G, c.B))
    ctx.Call("beginPath")
    ctx.Call("arc", p.X, p.Y, r, 0, 2 * math.Pi)
    ctx.Call("closePath")
    ctx.Call("fill")
}

func DrawRect(c Color, r Rect) {
    ctx.Set("fillStyle", fmt.Sprintf("rgb(%d, %d, %d)", c.R, c.G, c.B))
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

func DrawImageClip(img *js.Object, r Rect, clip Rect) {
    ctx.Call("drawImage", img, clip.X, clip.Y, clip.W, clip.H, r.X, r.Y, r.W, r.H)
}

func DrawText(txt string, c Color, p Point, size int) {
    ctx.Set("font", fmt.Sprintf("%dpx sans-serif", size))

    // draw background rect assuming height of font
    /*
    ctx.Set("fillStyle", "rgb(255, 255, 255)")
    width := ctx.Call("measureText", txt).Get("width").Int()
    ctx.Call("fillRect", p.X, p.Y, width, size)
    */

    ctx.Set("fillStyle", fmt.Sprintf("rgb(%d, %d, %d)", c.R, c.G, c.B))
    ctx.Set("textBaseline", "top")
    ctx.Set("textAlign", "left")
    ctx.Call("fillText", txt, p.X, p.Y)
}

func DrawTextCentered(txt string, c Color, p Point, size int) {
    ctx.Set("font", fmt.Sprintf("%dpx sans-serif", size))

    // draw background rect assuming height of font
    /*
    ctx.Set("fillStyle", "rgb(255, 255, 255)")
    width := ctx.Call("measureText", txt).Get("width").Int()
    ctx.Call("fillRect", p.X-width/2, p.Y-size/2, width, size)
    */

    ctx.Set("fillStyle", fmt.Sprintf("rgb(%d, %d, %d)", c.R, c.G, c.B))
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

func MainLoop(f func(), millis int) {
    if timer >= 0 {
        js.Global.Call("clearInterval", timer)
        timer = -1
    }
    if f != nil {
        timer = js.Global.Call("setInterval", f, millis).Int()
    }
}

func UpdateCanvas() {
}

func Exit() {
    HandleKeys(nil, nil)
    MainLoop(nil, 0)
}

func HandleKeys(keydown func(string), keyup func(string)) {
    doc.Set("onkeydown", g2dKeyDown)
    doc.Set("onkeyup", g2dKeyUp)
    doc.Set("onfocus", g2dFocus)
    doc.Set("onmousedown", g2dMouseDown)
    doc.Set("onmouseup", g2dMouseUp)
    doc.Set("onmousemove", g2dMouseMove)

    usrKeyDown = keydown
    usrKeyUp = keyup
}

func GetMousePos() Point {
    return mousePos
}

func g2dMouseMove(e *js.Object) {
    rect := canvas.Call("getBoundingClientRect")
    mousePos.X = e.Get("clientX").Int() - rect.Get("left").Int()
    mousePos.Y = e.Get("clientY").Int() - rect.Get("top").Int()
}

func g2dMouseDown(e *js.Object) {
    b := e.Get("button").Int()
    if 0 <= b && b < 3 {
        e.Set("code", mouseCodes[b])
        g2dKeyDown(e)
    }
}

func g2dMouseUp(e *js.Object) {
    b := e.Get("button").Int()
    if 0 <= b && b < 3 {
        e.Set("code", mouseCodes[b])
        g2dKeyUp(e)
    }
}

func g2dKeyDown(e *js.Object) {
    code := e.Get("code").String()
    _, pressed := keyPressed[code]
    if pressed {
        return
    }
    keyPressed[code] = true
    if usrKeyDown != nil {
        usrKeyDown(code)
    }
}

func g2dKeyUp(e *js.Object) {
    code := e.Get("code").String()
    _, pressed := keyPressed[code]
    if pressed {
        delete(keyPressed, code)
    }
    if usrKeyUp != nil {
        usrKeyUp(code)
    }
}

func g2dFocus(e *js.Object) {
    keyPressed = make(map[string]interface{})
}

type Actor interface {
    Move()
    Collide(other Actor)
    Position() Rect
    Symbol() Rect
}

type Arena struct {
    w, h int
    actors []Actor
}

func NewArena(size Size) *Arena {
    a := &Arena{size.W, size.H, []Actor{}}
    return a
}

func (a *Arena) Add(actor Actor) {
    if !a.Contains(actor) {
        a.actors = append(a.actors, actor)
    }
}

func (a *Arena) Remove(actor Actor) {
    for i, v := range a.actors {
        if v == actor {
            a.actors = append(a.actors[:i], a.actors[i+1:]...)
            return
        }
    }
}

func (a *Arena) Contains(actor Actor) bool {
    for _, v := range a.actors {
        if v == actor {
            return true
        }
    }
    return false
}

func (a *Arena) MoveAll() {
    actors := a.ReversedActors()
    for _, actor := range actors {
        actor.Move()
        for _, other := range actors {
            if actor != other && a.CheckCollision(actor, other) {
                actor.Collide(other)
                other.Collide(actor)
            }
        }
    }
}

func (a *Arena) CheckCollision(a1, a2 Actor) bool {
    r1 := a1.Position()
    r2 := a2.Position()
    return (r2.X < r1.X + r1.W && r1.X < r2.X + r2.W &&
            r2.Y < r1.Y + r1.H && r1.Y < r2.Y + r2.H &&
            a.Contains(a1) && a.Contains(a2))
}

func (a *Arena) Actors() []Actor {
    actors := make([]Actor, len(a.actors))
    for i, v := range a.actors {
        actors[i] = v
    }
    return actors
}

func (a *Arena) ReversedActors() []Actor {
    actors := make([]Actor, len(a.actors))
    for i, v := range a.actors {
        actors[len(a.actors) - i - 1] = v
    }
    return actors
}

func (a *Arena) Size() Size {
     return Size{a.w, a.h}
}
