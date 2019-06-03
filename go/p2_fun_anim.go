package main

import . "g2d"

var image = LoadImage("ball.png")
var x, y, dx = 50, 50, 5
const arenaW, arenaH, ballW, ballH = 480, 360, 20, 20

func tick() {
    //if KeyPressed("Enter") { ... }
    //if x + dx < 0 or x + dx + ballW > arenaW { ... }
    ClearCanvas()                  // Draw background
    DrawImage(image, Point{x, y})  // Draw foreground
    x += dx                        // Update ball's position
}

func main() {
    InitCanvas(Size{arenaW, arenaH})
    MainLoop(tick)  // Call tick 30 times/second
}
