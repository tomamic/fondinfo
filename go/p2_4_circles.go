package main

import . "g2d"

func main() {
    radius, color := 300.0, 255.0
    center := Point{int(radius), int(radius)}
    InitCanvas(Size{int(radius*2), int(radius*2)})
    n := ToInt(Prompt("N?"))
    dr, dc := radius / float64(n), color / (float64(n) - 1.0)
    for i := 0; i < n; i++ {
        SetColor(Color{int(color - float64(i)*dc), 0, 0})
        FillCircle(center, int(radius - float64(i)*dr))
    }
    MainLoop()
}
