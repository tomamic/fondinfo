package main

import . "g2d"

var screen = Size{480, 360}
var margin = 100

var actors = []*Vehicle { NewVehicle(Point{40, 40}, 5),
    NewVehicle(Point{80, 80}, -5), NewVehicle(Point{120, 40}, 5) }

type Vehicle struct {
    x, y, w, h      int
    dx, left, right int
}

func NewVehicle(pos Point, dx int) *Vehicle {
    return &Vehicle{pos.X, pos.Y, 20, 20, dx, -margin, screen.W+margin}
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

func (a *Vehicle) Position() Rect {
    return Rect{a.x, a.y, a.w, a.h}
}

func tick() {
    ClearCanvas()
    for _, a := range actors {
        a.Move()
        FillRect(a.Position())
    }
}

func main() {
    InitCanvas(screen)
    MainLoop(tick)
}

