package main

import . "g2d"

var arena = NewArena(Point{480, 360})
var a1 = NewVehicle(arena, Point{40, 40}, 5)
var a2 = NewVehicle(arena, Point{120, 40}, 5)
var a3 = NewVehicle(arena, Point{80, 80}, -5)

type Vehicle struct {
    x, y, w, h      int
    dx, left, right int
}

func NewVehicle(arena *Arena, pos Point, dx int) *Vehicle {
    a := &Vehicle{pos.X, pos.Y, 20, 20, dx, -100, arena.Size().X+100}
    arena.Add(a)
    return a
}

func (a *Vehicle) Move() {
    if a.x + a.dx < a.left {
        a.x = a.right
    }
    if a.x + a.dx > a.right {
        a.x = a.left
    }
    a.x += a.dx
}

func (a *Vehicle) Position() Point {
    return Point{a.x, a.y}
}

func (a *Vehicle) Size() Point {
    return Point{a.w, a.h}
}

func (a *Vehicle) Symbol() Point {
    return Point{0, 0}
}

func (a *Vehicle) Collide(other Actor) {
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
