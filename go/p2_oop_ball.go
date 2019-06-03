package main

import . "g2d"

var screen = Size{480, 360}

type Ball struct {
    x, y, w, h int
    dx, dy     int
}

func NewBall(pos Point) *Ball {
    return &Ball{pos.X, pos.Y, 20, 20, 5, 5}
}

func (b *Ball) Move() {
    if !(0 <= b.x+b.dx && b.x+b.dx <= screen.W-b.w) {
        b.dx = -b.dx
    }
    if !(0 <= b.y+b.dy && b.y+b.dy <= screen.H-b.h) {
        b.dy = -b.dy
    }
    b.x += b.dx
    b.y += b.dy
}

func (b *Ball) Position() Rect {
    return Rect{b.x, b.y, b.w, b.h}
}

// Create two objects, instances of the Ball class
var b1 = NewBall(Point{40, 80})
var b2 = NewBall(Point{80, 40})

func mainConsole() {
    for i := 0; i < 25; i++ {
        Println("Ball 1 @", b1.Position())
        Println("Ball 2 @", b2.Position())
        b1.Move()
        b2.Move()
    }
}

func tick() {
    ClearCanvas()  // BG
    b1.Move()
    b2.Move()
    FillRect(b1.Position())  // FG
    FillRect(b2.Position())  // FG
}

func main() {
    //mainConsole()
    InitCanvas(screen)
    MainLoop(tick)
}
