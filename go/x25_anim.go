package main

import . "g2d"

var image = LoadImage("ball.png")
var x, dx = 50, 5

func tick() {
    ClearCanvas()                  // Draw background
    DrawImage(image, Point{x, 50}) // Draw foreground
    if x+dx < 0 || x+dx+20 > 480 {
        dx = -dx
    }
    x = x + dx // Update ball's position
}

func main() {
    InitCanvas(Size{480, 360})
    MainLoop(tick)  // 30 fps
}
