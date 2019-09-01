package main

import . "g2d"

func main() {
    radius := 300
    InitCanvas(Point{radius*2, radius*2})
    n := ToInt(Prompt("N?"))
    for i := n; i > 0; i-- {
        r := i * radius / n
        c := 0
        if n > 1 {
            c = (i-1) * 255 / (n-1)
        }
        SetColor(Color{c, 0, 0})
        FillCircle(Point{radius, radius}, r)
    }
    MainLoop()
}
