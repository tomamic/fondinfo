package main

import . "g2d"

var screen = Point{480, 360}

type Ball struct {
    x, y, w, h int
    dx, dy     int
}

func NewBall(pos Point) *Ball {
    return &Ball{pos.X, pos.Y, 20, 20, 5, 5}
}

func (b *Ball) Move() {
    if !(0 <= b.x+b.dx && b.x+b.dx <= screen.X-b.w) {
        b.dx = -b.dx
    }
    if !(0 <= b.y+b.dy && b.y+b.dy <= screen.Y-b.h) {
        b.dy = -b.dy
    }
    b.x += b.dx
    b.y += b.dy
}

func (b *Ball) Position() Rect {
    return Rect{b.x, b.y, b.w, b.h}
}

// Create two objects, instances of the Ball class
var balls = []*Ball{NewBall(Point{40, 80}), NewBall(Point{80, 40})}

func tick() {
    ClearCanvas() // BG
    for _, b := range balls {
        b.Move()
        FillRect(b.Position()) // FG
    }
}

func main() {
    InitCanvas(screen)
    MainLoop(tick)
}
