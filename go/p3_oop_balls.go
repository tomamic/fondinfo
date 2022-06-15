package main

import . "g2d"

var screen = Point{480, 360}
var size = Point{20, 20}

type Ball struct {
    x, y   int
    dx, dy int
}

func NewBall(pos Point) *Ball {
    return &Ball{pos.X, pos.Y, 5, 5}
}

func (b *Ball) Move() {
    if !(0 <= b.x+b.dx && b.x+b.dx <= screen.X-size.X) {
        b.dx = -b.dx
    }
    if !(0 <= b.y+b.dy && b.y+b.dy <= screen.Y-size.Y) {
        b.dy = -b.dy
    }
    b.x += b.dx
    b.y += b.dy
}

func (b *Ball) Pos() Point {
    return Point{b.x, b.y}
}

// Create two objects, instances of the Ball class
var balls = []*Ball{NewBall(Point{40, 80}), NewBall(Point{80, 40})}

func tick() {
    ClearCanvas() // BG
    for _, b := range balls {
        b.Move()
        DrawImage("ball.png", b.Pos()) // FG
    }
}

func main() {
    InitCanvas(screen)
    MainLoop(tick)
}
