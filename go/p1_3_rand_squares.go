package main

import . "g2d"

func main() {
    w, h := 640, 480
    side := 100

    n := ToInt(Prompt("N? "))

    InitCanvas(Size{w, h})
    i := 0
    for i < n {
        r, g, b := RandInt(0, 255), RandInt(0, 255), RandInt(0, 255)
        x, y := RandInt(0, w - side), RandInt(0, h - side)
        SetColor(Color{r, g, b})
        FillRect(Rect{x, y, side, side})
        i += 1
    }
    MainLoop(nil, 0)
}

