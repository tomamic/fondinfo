package main

import . "g2d"

var arena = NewArena(Point{480, 360})
var hero = NewFrog(arena, Point{160, 160})
var a1 = NewVehicle(arena, Point{40, 40}, 5)
var a2 = NewVehicle(arena, Point{120, 40}, 5)
var a3 = NewVehicle(arena, Point{80, 80}, -5)


//// Frog

type Frog struct {
    arena               *Arena
    x, y, w, h          int
    x0, y0, dx, dy      int
    speed, steps, count int
}

func NewFrog(arena *Arena, pos Point) *Frog {
    a := &Frog{arena,
               pos.X, pos.Y, 20, 20,
               pos.X, pos.Y, 0, 0,
               4, 5, 0}
    arena.Add(a)
    return a
}

func (a *Frog) Move() {
    if a.count > 0 {
        a.count--
        as := a.arena.Size()
        a.x += a.dx
        if a.x < 0 {
            a.x = 0
        } else if a.x > as.X-a.w {
            a.x = as.X - a.w
        }
        a.y += a.dy
        if a.y < 0 {
            a.y = 0
        } else if a.y > as.Y-a.h {
            a.y = as.Y - a.h
        }
    }
}

func (a *Frog) JumpLeft() {
    if a.count == 0 {
        a. count = a.steps
        a.dx, a.dy = -a.speed, 0
    }
}

func (a *Frog) JumpRight() {
    if a.count == 0 {
        a. count = a.steps
        a.dx, a.dy = +a.speed, 0
    }
}

func (a *Frog) JumpUp() {
    if a.count == 0 {
        a. count = a.steps
        a.dx, a.dy = 0, -a.speed
    }
}

func (a *Frog) JumpDown() {
    if a.count == 0 {
        a. count = a.steps
        a.dx, a.dy = 0, +a.speed
    }
}

func (a *Frog) Collide(other Actor) {
    a.x = a.x0
    a.y = a.y0
}

func (a *Frog) Position() Point {
    return Point{a.x, a.y}
}

func (a *Frog) Size() Point {
    return Point{a.w, a.h}
}

func (a *Frog) Symbol() Point {
    return Point{0, 20}
}


//// Vehicle

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


//// main

func tick() {
    if KeyPressed("ArrowUp") {
        hero.JumpUp()
    } else if KeyPressed("ArrowRight") {
        hero.JumpRight()
    } else if KeyPressed("ArrowDown") {
        hero.JumpDown()
    } else if KeyPressed("ArrowLeft") {
        hero.JumpLeft()
    }

    arena.MoveAll()
    ClearCanvas()
    for _, a := range arena.Actors() {
        FillRect(a.Position(), a.Size())
    }
}

func main() {
    InitCanvas(arena.Size())
    MainLoop(tick)
}
