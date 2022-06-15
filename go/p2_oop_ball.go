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
var b1 = NewBall(Point{40, 80})
var b2 = NewBall(Point{80, 40})

func mainConsole() {
    for i := 0; i < 25; i++ {
        Println("Ball 1 @", b1.Pos())
        Println("Ball 2 @", b2.Pos())
        b1.Move()
        b2.Move()
    }
}

func tick() {
    ClearCanvas()  // BG
    b1.Move()
    b2.Move()
    DrawImage("ball.png", b1.Pos())  // FG
    DrawImage("ball.png", b2.Pos())  // FG
}

func main() {
    //mainConsole()
    InitCanvas(screen)
    MainLoop(tick)
}
