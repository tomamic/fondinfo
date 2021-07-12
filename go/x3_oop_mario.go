package main

import . "g2d"

type Wall struct {
    arena         *Arena
    x, y, w, h    int
}

func NewWall(arena *Arena, pos Point) *Wall {
    a := &Wall{arena, pos.X, pos.Y, 100, 20}
    arena.Add(a)
    return a
}

func (a *Wall) Move() {
}

func (a *Wall) Position() Point {
    return Point{a.x, a.y}
}

func (a *Wall) Size() Point {
    return Point{a.w, a.h}
}

func (a *Wall) Symbol() Point {
    return Point{0, 0}
}

func (a *Wall) Collide(other Actor) {
}


type Mario struct {
    arena            *Arena
    x, y, w, h       int
    dx, dy, speed, g float64
    landed           bool
}

func NewMario(arena *Arena, pos Point) *Mario {
    a := &Mario{arena, pos.X, pos.Y, 20, 20, 0, 0, 5, 0.5, false}
    arena.Add(a)
    return a
}

func (a *Mario) Move() {
    screen := a.arena.Size()
    a.x += int(a.dx)
    if a.x < 0 {
        a.x = 0
    } else if a.x > screen.X - a.w {
        a.x = screen.X - a.w
    }
    a.y += int(a.dy)
    if a.y < 0 {
        a.y = 0
    } else if a.y > screen.Y - a.h {
        a.y = screen.Y - a.h
        a.landed = true
    }
    a.dy += a.g
}

func (a *Mario) GoLeft() {
    a.dx = -a.speed
}

func (a *Mario) GoRight() {
    a.dx = a.speed
}

func (a *Mario) Jump() {
    if a.landed {
        a.dy = -2 * a.speed
        a.landed = false
    }
}

func (a *Mario) Stay() {
    a.dx = 0
}

func (a *Mario) Collide(other Actor) {
    if _, ok := other.(*Wall); ok {
        p1, p2 := a.Position(), other.Position()
        borders := [][]int{{p1.X+p1.W - p2.X, -1, 0}, {p2.X+p2.W - p1.X, 1, 0},
                           {p1.Y+p1.H - p2.Y, 0, -1}, {p2.Y+p2.H - p1.Y, 0, 1}}
        move := borders[0]  // find nearest border: ← → ↑ ↓
        for _, val := range borders {
            if val[0] < move[0] {
                move = val
            }
        }
        a.x += move[1] * move[0]  // sign_dx * distance
        a.y += move[2] * move[0]  // sign_dy * distance
        if move[2] < 0 {
            a.landed = true
        }
        if move[2] != 0 {
            a.dy = 1
        }
    }
}

func (a *Mario) Position() Point {
    return Point{a.x, a.y}
}

func (a *Mario) Size() Point {
    return Point{a.w, a.h}
}

func (a *Mario) Symbol() Point {
    return Point{0, 20}
}

var arena = NewArena(Point{480, 360})
var w1 = NewWall(arena, Point{300, 300})
var w2 = NewWall(arena, Point{80, 240})
var hero = NewMario(arena, Point{230, 170})
var img = LoadImage("sprites.png")

func tick() {
    if KeyPressed("ArrowUp") {
        hero.Jump()
    } else if KeyPressed("ArrowRight") {
        hero.GoRight()
    } else if KeyPressed("ArrowLeft") {
        hero.GoLeft()
    } else if KeyReleased("ArrowRight") || KeyReleased("ArrowLeft") {
        hero.Stay()
    }

    arena.MoveAll()
    ClearCanvas()
    for _, a := range arena.Actors() {
        if a.Symbol().H > 0 {
            DrawImageClip(img, a.Symbol(), a.Size(), a.Position())
        } else {
            FillRect(a.Position(), a.Size())
        }
    }
}

func main() {
    InitCanvas(arena.Size())
    MainLoop(tick)
}
