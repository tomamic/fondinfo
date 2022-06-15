package main

import . "g2d"

var x, y, dx = 50, 50, 5
var screen = Point{480, 360}

func tick() {
    ClearCanvas()                  // Draw background
    DrawImage("ball.png", Point{x, y})  // Draw foreground
    //if MouseClicked() { ... }
    //if x + dx > screen.X { ... }
    x += dx                        // Update ball's position
}

func main() {
    InitCanvas(screen)
    MainLoop(tick)  // Call tick 30 times/second
}
