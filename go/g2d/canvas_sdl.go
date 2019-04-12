// +build !js

package g2d

import (
    "fmt"
    "github.com/gen2brain/dlgs"
    "github.com/veandco/go-sdl2/img"
    "github.com/veandco/go-sdl2/mix"
    "github.com/veandco/go-sdl2/sdl"
    "github.com/veandco/go-sdl2/ttf"
    "io"
    "net/http"
    "os"
)

var window *sdl.Window
var renderer *sdl.Renderer
var textures = make(map[*sdl.Surface]*sdl.Texture)
var update func()
var usrKeyDown, usrKeyUp func(string)
var mousePos = Point{0, 0}
var mouseCodes = []string{"LeftButton", "MiddleButton", "RightButton"}

func rgba(c Color) (uint8, uint8, uint8, uint8) {
    return uint8(c.R), uint8(c.G), uint8(c.B), 255
}

func xywh(r Rect) (int32, int32, int32, int32) {
    return int32(r.X), int32(r.Y), int32(r.W), int32(r.H)
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
    renderer, err = sdl.CreateRenderer(window, -1,
        sdl.RENDERER_ACCELERATED|sdl.RENDERER_PRESENTVSYNC)
    if err != nil {
        panic(err)
    }
    SetColor(Color{255, 255, 255})
    ClearCanvas()
}

func Prompt(a ...interface{}) string {
    val, _, _ := dlgs.Entry("", fmt.Sprint(a...), "")
    return val
}

func Confirm(a ...interface{}) bool {
    val, _ := dlgs.Question("", fmt.Sprint(a...), true)
    return val
}

func Alert(a ...interface{}) {
    dlgs.Info("", fmt.Sprint(a...))
    //fmt.Println(a...)
}

func UpdateCanvas() {
    renderer.Present()
}

func SetColor(c Color) {
    renderer.SetDrawColor(rgba(c))
}

func ClearCanvas() {
    renderer.Clear()
}

func DrawLine(pt1, pt2 Point) {
    renderer.DrawLine(int32(pt1.X), int32(pt1.Y), int32(pt2.X), int32(pt2.Y))
}

func FillCircle(center Point, radius int) {
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

func FillRect(r Rect) {
    x, y, w, h := xywh(r)
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
    DrawImageClip(img, Rect{0, 0, int(img.W), int(img.H)},
        Rect{pos.X, pos.Y, int(img.W), int(img.H)})
}

func DrawImageClip(img *sdl.Surface, area Rect, pos Rect) {
    t, found := textures[img]
    if !found {
        t, err := renderer.CreateTextureFromSurface(img)
        if err != nil {
            panic(err)
        }
        textures[img] = t
    }
    px, py, pw, ph := xywh(pos)
    ax, ay, aw, ah := xywh(area)
    renderer.Copy(t, &sdl.Rect{ax, ay, aw, ah}, &sdl.Rect{px, py, pw, ph})
}

func DrawText(txt string, pos Point, size int) {
    drawText(txt, pos, size, false)
}

func DrawTextCentered(txt string, pos Point, size int) {
    drawText(txt, pos, size, true)
}

func drawText(txt string, pos Point, size int, centered bool) {
    fname := "~Roboto-Regular.ttf"
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
    r, g, b, a, _ := renderer.GetDrawColor()
    sur, err := font.RenderUTF8Blended(txt, sdl.Color{r, g, b, a})
    if err != nil {
        panic(err)
    }
    x, y, w, h := int32(pos.X), int32(pos.Y), sur.W, sur.H
    if centered {
        x, y = x-w/2, y-h/2
    }
    //DrawImage(surface, pos)

    t, err := renderer.CreateTextureFromSurface(sur)
    if err != nil {
        panic(err)
    }
    renderer.Copy(t, &sdl.Rect{0, 0, w, h}, &sdl.Rect{x, y, w, h})
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

func HandleKeys(keydown, keyup func(string)) {
    usrKeyDown, usrKeyUp = keydown, keyup
}

func MousePosition() Point {
    return mousePos
}

func MainLoop(update func(), delay int) {
    if delay < 1000/60 {
        delay = 1000 / 60
    }
    defer sdl.Quit()
    defer window.Destroy()
    renderer.Present()
    for running := true; running; {
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
                mousePos.X, mousePos.Y = int(v.X), int(v.Y)
            case *sdl.MouseButtonEvent:
                if v.Button < 1 || 3 < v.Button {
                } else if v.State == sdl.PRESSED && usrKeyDown != nil {
                    usrKeyDown(mouseCodes[v.Button-1])
                } else if v.State == sdl.RELEASED && usrKeyUp != nil {
                    usrKeyUp(mouseCodes[v.Button-1])
                }
            }
        }
        if update != nil {
            update()
            renderer.Present()
        }
        sdl.Delay(uint32(delay))
    }
    Exit()
}

func Exit() {
    sdl.Quit()
    os.Exit(0)
}
