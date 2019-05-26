package main

import . "g2d"

func main() {
    InitCanvas(Size{300, 300})

    for i := 0; i < 5; i++ {
        x := i * 40
        y := x
        red := i * 60
        SetColor(Color{red, 0, 0})
        DrawRect(Rect{x, y, 140, 140})
    }
    i := 0

    MainLoop()
}
