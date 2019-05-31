package main

import (
    . "g2d"
    "math"
)

var i, n = 0, 256

func tick() {
    a := float64(i)
    x := 300 + int(a*math.Cos(a*math.Pi/32))
    y := 300 + int(a*math.Sin(a*math.Pi/32))
    ClearCanvas()
    SetColor(Color{255 - i, 0, i})
    FillCircle(Point{x, y}, i/2)
    i = (i + 1) % n
}

func main() {
    InitCanvas(Size{600, 600})
    MainLoop(tick)
}
