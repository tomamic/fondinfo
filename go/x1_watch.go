package main

import (
    . "g2d"
    "math"
)

func main() {
    radius1, radius2, radius3 := 300.0, 295.0, 280.0
    x, y := radius1, radius1
    InitCanvas(Point{int(radius1*2), int(radius1*2)})
    SetColor(Color{0, 0, 0})
    for i := 0; i < 12; i++ {
        angle := float64(i) * 2 * math.Pi / 12
        pt1 := Point{int(x + radius1*math.Cos(angle)), int(y + radius1*math.Sin(angle))}
        pt2 := Point{int(x + radius3*math.Cos(angle)), int(y + radius3*math.Sin(angle))}
        DrawLine(pt1, pt2)
    }
    for i := 0; i < 60; i++ {
        angle := float64(i) * 2 * math.Pi / 60
        pt1 := Point{int(x + radius1*math.Cos(angle)), int(y + radius1*math.Sin(angle))}
        pt2 := Point{int(x + radius2*math.Cos(angle)), int(y + radius2*math.Sin(angle))}
        DrawLine(pt1, pt2)
    }
    MainLoop()
}
