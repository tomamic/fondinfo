package main

import . "g2d"

var arenaW, arenaH = 480, 360

var b1 = NewBall(Point{40, 80})
var b2 = NewBall(Point{80, 40})

type Ball struct {
    x, y, w, h, dx, dy, count int
}

func NewBall(pos Point) *Ball {
    return &Ball{pos.X, pos.Y, 20, 20, 5, 5, 0}
}

func (b *Ball) Move() {
    if b.count > 0 {
        b.count -= 1
        if b.x+b.dx < 0 || arenaW - b.w < b.x+b.dx {
            b.dx = -b.dx
        }
        if b.y+b.dy < 0 || arenaH - b.h < b.y+b.dy {
            b.dy = -b.dy
        }

        b.x += b.dx
        b.y += b.dy
    }
}

func (b *Ball) Start() {
    b.count = 5
}

func (b *Ball) Position() Rect {
    return Rect{b.x, b.y, b.w, b.h}
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
    FillRect(b1.Position())
    FillRect(b2.Position())
}

func main() {
    InitCanvas(Point{arenaW, arenaH})
    MainLoop(tick)
}
