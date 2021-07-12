package main

import . "g2d"

func main() {
    InitCanvas(Point{400, 400})
    n := ToInt(Prompt("N?"))

    for i := 0; i < n; i++ {
        c, p := 0, 0
        if n > 1 {
            c = i * 255 / (n - 1)
            p = i * 300 / (n - 1)
        }
        SetColor(Color{c, 0, 0})
        FillRect(Point{p, p}, Point{100, 100})
    }
    MainLoop()
}
