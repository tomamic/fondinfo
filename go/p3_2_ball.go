package main

import . "g2d"

var as = Size{400, 400}
var b = NewBall(Point{100, 100})

type Ball struct {
    x, y, w, h int
    dx, dy     int
}

func NewBall(pos Point) *Ball {
    return &Ball{pos.X, pos.Y, 20, 20, -5, 5}
}

func (b *Ball) Move() {
    b.x = (b.x + b.dx + as.W) % as.W
}

func (b *Ball) Position() Rect {
    return Rect{b.x, b.y, b.w, b.h}
}

func update() {
    SetColor(Color{255, 255, 255})
    ClearCanvas() // BG
    b.Move()
    SetColor(Color{100, 100, 100})
    FillRect(b.Position()) // FG
}

func main() {
    InitCanvas(as)
    MainLoop(update, 1000/30)
}

