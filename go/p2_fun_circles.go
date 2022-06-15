package main

import . "g2d"

func tick() {
    if MouseClicked() {
        pos := MousePosition()
        SetColor(Color{RandInt(0, 255), RandInt(0, 255), RandInt(0, 255)})
        if pos.X <= 25 && pos.Y <= 25 && Confirm("Exit?") {
            CloseCanvas()
        } else {
            FillCircle(pos, 25)
        }
    }
}

func main() {
    InitCanvas(Point{480, 360})
    MainLoop(tick)  // Call tick 30 times/second
}
