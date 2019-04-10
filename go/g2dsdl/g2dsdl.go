package g2dsdl

import (
    "fmt"
    "github.com/gen2brain/dlgs"
    "github.com/veandco/go-sdl2/img"
    "github.com/veandco/go-sdl2/mix"
    "github.com/veandco/go-sdl2/sdl"
    "github.com/veandco/go-sdl2/ttf"
    "io"
    "math/rand"
    "net/http"
    "os"
)

type Point struct{ X, Y int }
type Rect struct{ X, Y, W, H int }
type Size struct{ W, H int }
type Color struct{ R, G, B int }

func (c Color) Rgba() (uint8, uint8, uint8, uint8) {
    return uint8(c.R), uint8(c.G), uint8(c.B), 255
}

func (r Rect) Xywh() (int32, int32, int32, int32) {
    return int32(r.X), int32(r.Y), int32(r.W), int32(r.H)
}

var window *sdl.Window
var renderer *sdl.Renderer
var textures = make(map[*sdl.Surface]*sdl.Texture)

var update func()
var usrKeyDown, usrKeyUp func(string)
var usrMouseDown, usrMouseUp, usrMouseMove func(Point, int)

func Prompt(a ...interface{}) string {
    val, _, _ := dlgs.Entry("", fmt.Sprint(a...), "")
    //~ fmt.Println(a...)
    //~ val := ""
    //~ fmt.Scanf("%s", &val)
    return val
}

func Println(a ...interface{}) {
    fmt.Println(a...)
}

func Alert(a ...interface{}) {
    dlgs.Info("", fmt.Sprint(a...))
    //fmt.Println(a...)
}

func ParseInt(text string) int {
    val := 0
    fmt.Sscanf(text, "%d", &val)
    return val
}

func ParseFloat(text string) float64 {
    val := 0.0
    fmt.Sscanf(text, "%f", &val)
    return val
}

func Random() float64 {
    return rand.Float64()
}

func RandInt(min, max int) int {
    return int(Random()*float64(max-min+1)) + min
}

func InitCanvas(size Size) {
    if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
        panic(err)
    }
    ttf.Init()
    w, h := int32(size.W), int32(size.H)
    //win, ren, err := sdl.CreateWindowAndRenderer(w, h, 0)
    window, err := sdl.CreateWindow("", sdl.WINDOWPOS_UNDEFINED,
        sdl.WINDOWPOS_UNDEFINED, w, h, sdl.WINDOW_OPENGL)
    if err != nil {
        panic(err)
    }
    renderer, err = sdl.CreateRenderer(window, -1, sdl.RENDERER_ACCELERATED|sdl.RENDERER_PRESENTVSYNC)
    if err != nil {
        panic(err)
    }
}

func UpdateCanvas() {
    renderer.Present()
}

func FillCanvas(c Color) {
    renderer.SetDrawColor(c.Rgba())
    renderer.Clear()
}

func DrawLine(c Color, pt1, pt2 Point) {
    renderer.SetDrawColor(c.Rgba())
    renderer.DrawLine(int32(pt1.X), int32(pt1.Y), int32(pt2.X), int32(pt2.Y))
}

func DrawCircle(c Color, center Point, radius int) {
    renderer.SetDrawColor(c.Rgba())

    diameter := int32(radius * 2)
    x0, y0 := int32(center.X), int32(center.Y)
    var x, y, tx, ty int32 = int32(radius - 1), 0, 1, 1
    err := tx - diameter
    for x >= y {
        // Each of the following renders an octant of the circle
        renderer.DrawLine(x0+x, y0-y, x0-x, y0-y)
        renderer.DrawLine(x0+x, y0+y, x0-x, y0+y)
        renderer.DrawLine(x0-y, y0-x, x0+y, y0-x)
        renderer.DrawLine(x0-y, y0+x, x0+y, y0+x)

        if err <= 0 {
            y++
            ty += 2
            err += ty
        }
        if err > 0 {
            x--
            tx += 2
            err += tx - diameter
        }
    }
}

func DrawRect(c Color, r Rect) {
    x, y, w, h := r.Xywh()
    renderer.SetDrawColor(c.Rgba())
    renderer.FillRect(&sdl.Rect{x, y, w, h})
}

func LoadImage(url string) *sdl.Surface {
    image, err := img.Load(url)
    if err != nil {
        panic(err)
    }
    return image
}

func DrawImage(img *sdl.Surface, pos Point) {
    DrawImageClip(img, Rect{pos.X, pos.Y, int(img.W), int(img.H)},
        Rect{0, 0, int(img.W), int(img.H)})
}

func DrawImageClip(img *sdl.Surface, pos Rect, area Rect) {
    t, found := textures[img]
    if !found {
        t, err := renderer.CreateTextureFromSurface(img)
        if err != nil {
            panic(err)
        }
        textures[img] = t
    }
    px, py, pw, ph := pos.Xywh()
    ax, ay, aw, ah := area.Xywh()
    renderer.Copy(t, &sdl.Rect{ax, ay, aw, ah}, &sdl.Rect{px, py, pw, ph})
}

func DrawText(txt string, c Color, pos Point, size int) {
    drawText(txt, c, pos, size, false)
}

func DrawTextCentered(txt string, c Color, pos Point, size int) {
    drawText(txt, c, pos, size, true)
}

func drawText(txt string, c Color, pos Point, size int, centered bool) {
    fname := "Roboto-Regular.ttf"
    if _, err := os.Stat(fname); os.IsNotExist(err) {
        out, _ := os.Create(fname)
        defer out.Close()
        resp, _ := http.Get("https://github.com/google/fonts/blob/master/apache/roboto/Roboto-Regular.ttf?raw=true")
        defer resp.Body.Close()
        _, _ = io.Copy(out, resp.Body)
    }
    font, err := ttf.OpenFont(fname, size)
    defer font.Close()
    if err != nil {
        panic(err)
    }
    r, g, b, a := c.Rgba()
    surface, err := font.RenderUTF8Blended(txt, sdl.Color{r, g, b, a})
    if err != nil {
        panic(err)
    }
    if centered {
        pos = Point{pos.X - int(surface.W)/2, pos.Y - int(surface.H)/2}
    }
    fmt.Println(pos.X, pos.Y, surface.W, surface.H)
    DrawImage(surface, pos)
}

func LoadAudio(url string) *mix.Music {
    mus, err := mix.LoadMUS(url)
    if err != nil {
        panic(err)
    }
    return mus
}

func PlayAudio(audio *mix.Music, loop bool) {
    if loop {
        audio.Play(-1)
    } else {
        audio.Play(0)
    }
}

func PauseAudio(audio *mix.Music) {
    mix.HaltMusic()
}

func webkey(e *sdl.KeyboardEvent) string {
    n := sdl.GetKeyName(e.Keysym.Sym)
    if "a" <= n && n <= "a" {
        n = string(n[0]-'a'+'A') + n[1:]
    }
    if len(n) == 1 && "A" <= n && n <= "Z" {
        n = "Key" + n
    } else if len(n) == 1 && "0" <= n && n <= "9" {
        n = "Digit" + n
    } else if n == "Up" || n == "Down" || n == "Right" || n == "Left" {
        n = "Arrow" + n
    }
    return n
}

func HandleKeyboard(keydown, keyup func(string)) {
    usrKeyDown, usrKeyUp = keydown, keyup
}

func HandleMouse(mousedown, mouseup, mousemove func(Point, int)) {
    usrMouseDown, usrMouseUp, usrMouseMove = mousedown, mouseup, mousemove
}

func MainLoop(update func(), delay int) {
    defer sdl.Quit()
    defer window.Destroy()
    running := true
    for running {
        for e := sdl.PollEvent(); e != nil; e = sdl.PollEvent() {
            switch v := e.(type) {
            case *sdl.QuitEvent:
                running = false
                break
            case *sdl.KeyboardEvent:
                if v.Repeat != 0 {
                } else if v.Type == sdl.KEYDOWN && usrKeyDown != nil {
                    usrKeyDown(webkey(v))
                } else if v.Type == sdl.KEYUP && usrKeyUp != nil {
                    usrKeyUp(webkey(v))
                }
            case *sdl.MouseMotionEvent:
                x, y, b := sdl.GetMouseState()
                if usrMouseMove != nil {
                    usrMouseMove(Point{int(x), int(y)}, int(b))
                }
            case *sdl.MouseButtonEvent:
                x, y, b := sdl.GetMouseState()
                if v.State == sdl.PRESSED && usrMouseDown != nil {
                    usrMouseDown(Point{int(x), int(y)}, int(b))
                } else if v.State == sdl.RELEASED && usrMouseUp != nil {
                    usrMouseUp(Point{int(x), int(y)}, int(b))
                }
            }
        }
        if update != nil {
            update()
        }
        renderer.Present()
        sdl.Delay(uint32(delay))
    }
    Exit()
}

func Exit() {
    sdl.Quit()
    os.Exit(0)
}

type Actor interface {
    Move()
    Collide(other Actor)
    Position() Rect
    Symbol() Rect
}

type Arena struct {
    w, h   int
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
    return (r2.X < r1.X+r1.W && r1.X < r2.X+r2.W &&
        r2.Y < r1.Y+r1.H && r1.Y < r2.Y+r2.H &&
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
        actors[len(a.actors)-i-1] = v
    }
    return actors
}

func (a *Arena) Size() Size {
    return Size{a.w, a.h}
}
