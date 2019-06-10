package main

import . "g2d"

var image = LoadImage("ball.png")
var x, y, dx = 50, 50, 5
var screen = Size{480, 360}

func tick() {
    //if KeyPressed("Enter") { ... }
    //if x + dx > screen.W { ... }
    ClearCanvas()                  // Draw background
    DrawImage(image, Point{x, y})  // Draw foreground
    x += dx                        // Update ball's position
}

func main() {
    InitCanvas(screen)
    MainLoop(tick)  // Call tick 30 times/second
}
