package main

import . "g2d"

var arena = NewArena(Point{480, 360})
var a1 = NewAlien(arena, Point{40, 40})
var a2 = NewAlien(arena, Point{80, 80})

type Alien struct {
    arena      *Arena
    x, y, w, h int
    xmin, xmax int
    dx, dy     int
}

func NewAlien(arena *Arena, pos Point) *Alien {
    a := &Alien{arena, pos.X, pos.Y, 20, 20, pos.X, pos.X+150, 5, 5}
    arena.Add(a)
    return a
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

func (a *Alien) Size() Point {
    return Point{a.w, a.h}
}

func (a *Alien) Symbol() Point {
    return Point{0, 0}
}

func (a *Alien) Collide(other Actor) {
}

func tick() {
    ClearCanvas()
    arena.MoveAll()
    for _, actor := range arena.Actors()  {
        FillRect(actor.Position(), actor.Size())
    }
}

func main() {
    InitCanvas(arena.Size())
    MainLoop(tick)
}
