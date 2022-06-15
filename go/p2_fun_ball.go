package main

import . "g2d"

// way too much global stuff!
var x1, y1, dx1, dy1 = 40, 80, 5, 5
var x2, y2, dx2, dy2 = 80, 40, 5, 5
var screen = Point{480, 360}
var size = Point{20, 20}

// encapsulates behaviour, but exposes data
func moveBall(x, y, dx, dy int) (int, int, int, int) {
    if x + dx < 0 || x + dx + size.X > screen.X {
        dx = -dx
    }
    x += dx
    if y + dy < 0 || y + dy + size.Y > screen.Y {
        dy = -dy
    }
    y += dy
    return x, y, dx, dy
}

func tick() {
    ClearCanvas()                    // Draw background
    DrawImage("ball.png", Point{x1, y1})  // Draw foreground
    DrawImage("ball.png", Point{x2, y2})  // Draw foreground
    x1, y1, dx1, dy1 = moveBall(x1, y1, dx1, dy1)
    x2, y2, dx2, dy2 = moveBall(x2, y2, dx2, dy2)
}

func main() {
    InitCanvas(screen)
    MainLoop(tick)
}
