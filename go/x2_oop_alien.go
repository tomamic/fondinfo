package main

import . "g2d"

var a = NewAlien(Point{40, 40})

type Alien struct {
    x, y int
    xmin, xmax int
    dx, dy     int
}

func NewAlien(pos Point) *Alien {
    return &Alien{pos.X, pos.Y, pos.X, pos.X+150, 5, 5}
}

func (a *Alien) Move() {
    if a.xmin <= a.x+a.dx && a.x+a.dx <= a.xmax {
        a.x += a.dx
    } else {
        a.dx = -a.dx
        a.y += a.dy
    }
}

func (a *Alien) Position() Point {
    return Point{a.x, a.y}
}

func tick() {
    ClearCanvas()
    a.Move()
    DrawImage("ball.png", a.Position())
}

func main() {
    InitCanvas(Point{480, 360})
    SetFrameRate(10)
    MainLoop(tick)
}
