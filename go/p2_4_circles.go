package main

import . "g2d"

func main() {
    n := ToInt(Prompt("N?"))
    InitCanvas(Size{400, 400})
    dr := 200.0 / n
    dc := 255.0 / (n - 1)
    for i := 0; i < n; i++ {
        SetColor(Color{255 - i*dc, 0, 0})
        FillCircle(Point{200, 200}, 200-i*dr)
    }
    MainLoop(nil, 0)
}

