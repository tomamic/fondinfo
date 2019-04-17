package main

import . "g2d"

var image = LoadImage("ball.png")
var x, y, dx = 50, 0, 5

func update() {
    ClearCanvas()                    // Draw background
    DrawImage(image, Point{x, y})    // Draw foreground
    if x+dx < 0 || x+dx+20 > 320 {
        dx = -dx
        y += 5
    } else {
        x += dx                      // Update ball's position
    }
}

func main() {
    InitCanvas(Size{320, 240})
    HandleEvents(update)
    MainLoop(10)  // 10 fps
}
