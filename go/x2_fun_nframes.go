package main

import . "g2d"

var x, y, dx, count = 50, 50, 5, 0
var ARENA_W, ARENA_H, MARGIN = 480, 360, 100
var image = LoadImage("ball.png")

func tick() {
    ClearCanvas()  // Draw background
    DrawImage(image, Point{x, y})  // Draw foreground
    if KeyPressed("Enter") {
        count = 5
    }
    if count > 0 {
        count -= 1
        if x + dx < -MARGIN {
            x = ARENA_W + MARGIN
        }
        if x + dx > ARENA_W + MARGIN {
            x = -MARGIN
        }
        x += dx  // Update ball's position
    }
}

func main() {
    InitCanvas(Point{ARENA_W, ARENA_H})
    SetFrameRate(10)
    MainLoop(tick)  // call tick 10 times/second
}
