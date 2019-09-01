package main

import . "g2d"

func main() {
    InitCanvas(Point{400, 400}) // width, height

    radius := ToInt(Prompt("Radius? [50-99]"))

    if 50 <= radius && radius <= 99 {
        SetColor(Color{0, 0, 255})
        FillCircle(Point{200, 200}, radius)
    } else {
        Alert("Out of range!")
    }

    SetColor(Color{255, 255, 0})
    FillCircle(Point{200, 200}, 25)

    MainLoop()
}
