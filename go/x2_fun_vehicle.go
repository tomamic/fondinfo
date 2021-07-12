package main

import . "g2d"

var x, y, dx, count = 50, 50, 5, 0
var ARENA_W, ARENA_H, MARGIN = 480, 360, 100

func tick() {
    ClearCanvas()  // Draw background
    DrawImage("ball.png", Point{x, y})  // Draw foreground

    if x + dx < -MARGIN {
        x = ARENA_W + MARGIN
    }
    if x + dx > ARENA_W + MARGIN {
        x = -MARGIN
    }
    x += dx  // Update ball's position
}

func main() {
    InitCanvas(Point{ARENA_W, ARENA_H})
    MainLoop(tick)
}
