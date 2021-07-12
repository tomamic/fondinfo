package main

import . "g2d"

var arenaW, arenaH, ballW, ballH = 480, 360, 20, 20

var b1 = NewBall(Point{40, 80})
var b2 = NewBall(Point{80, 40})

type Ball struct {
    x, y, dx, dy, count int
}

func NewBall(pos Point) *Ball {
    return &Ball{pos.X, pos.Y, 5, 5, 0}
}

func (b *Ball) Move() {
    if b.count > 0 {
        b.count -= 1
        if b.x+b.dx < 0 || arenaW - ballW < b.x+b.dx {
            b.dx = -b.dx
        }
        if b.y+b.dy < 0 || arenaH - ballH < b.y+b.dy {
            b.dy = -b.dy
        }

        b.x += b.dx
        b.y += b.dy
    }
}

func (b *Ball) Start() {
    b.count = 5
}

func (b *Ball) Position() Point {
    return Point{b.x, b.y}
}

func tick() {
    if KeyPressed("1") {
        b1.Start()
    }
    if KeyPressed("2") {
        b2.Start()
    }
    ClearCanvas()
    b1.Move()
    b2.Move()
    DrawImage("ball.png", b1.Position())
    DrawImage("ball.png", b2.Position())
}

func main() {
    InitCanvas(Point{arenaW, arenaH})
    MainLoop(tick)
}
