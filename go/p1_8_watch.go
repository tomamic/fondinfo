package main

import (
    . "g2d"
    "math"
)

func main() {
    InitCanvas(Size{400, 400})
    SetColor(Color{0, 0, 0})
    i, angle := 0, 0.0
    for i < 12 {
        pt1 := Point{200 + int(180*math.Cos(angle)), 200 + int(180*math.Sin(angle))}
        pt2 := Point{200 + int(200*math.Cos(angle)), 200 + int(200*math.Sin(angle))}
        DrawLine(pt1, pt2)
        i += 1
        angle += 2 * math.Pi / 12
    }
    i, angle = 0, 0.0
    for i < 60 {
        pt1 := Point{200 + int(195*math.Cos(angle)), 200 + int(195*math.Sin(angle))}
        pt2 := Point{200 + int(200*math.Cos(angle)), 200 + int(200*math.Sin(angle))}
        DrawLine(pt1, pt2)
        i += 1
        angle += 2 * math.Pi / 60
    }
    MainLoop()
}

