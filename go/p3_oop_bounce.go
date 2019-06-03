package main

import . "g2d"

type Ball struct {
    arena         *Arena
    x, y, w, h    int
    speed, dx, dy int
}

func NewBall(arena *Arena, pos Point) *Ball {
    a := &Ball{arena, pos.X, pos.Y, 20, 20, 5, 5, 5}
    arena.Add(a)
    return a
}

func (a *Ball) Move() {
    as := a.arena.Size()
    if !(0 <= a.x+a.dx && a.x+a.dx <= as.W-a.w) {
        a.dx = -a.dx
    }
    if !(0 <= a.y+a.dy && a.y+a.dy <= as.H-a.h) {
        a.dy = -a.dy
    }
    a.x += a.dx
    a.y += a.dy
}

func (a *Ball) Position() Rect {
    return Rect{a.x, a.y, a.w, a.h}
}

func (a *Ball) Symbol() Rect {
    return Rect{0, 0, a.h, a.w}
}

func (a *Ball) Collide(other Actor) {
    _, ok := other.(*Ghost)
    if !ok {
        op := other.Position()
        if op.X < a.x {
            a.dx = a.speed
        } else {
            a.dx = -a.speed
        }
        if op.Y < a.y {
            a.dy = a.speed
        } else {
            a.dy = -a.speed
        }
    }
}

type Ghost struct {
    arena      *Arena
    x, y, w, h int
    speed      int
    visible    bool
}

func NewGhost(arena *Arena, pos Point) *Ghost {
    a := &Ghost{arena, pos.X, pos.Y, 20, 20, 5, true}
    arena.Add(a)
    return a
}

func (a *Ghost) Move() {
    as := a.arena.Size()
    dx := RandInt(-1, 1) * a.speed
    dy := RandInt(-1, 1) * a.speed
    a.x = (a.x + dx + as.W) % as.W
    a.y = (a.y + dy + as.H) % as.H

    if RandInt(0, 99) == 0 {
        a.visible = !a.visible
    }
}

func (a *Ghost) Position() Rect {
    return Rect{a.x, a.y, a.w, a.h}
}

func (a *Ghost) Symbol() Rect {
    if a.visible {
        return Rect{20, 0, a.w, a.h}
    }
    return Rect{20, 20, a.w, a.h}
}

func (a *Ghost) Collide(other Actor) {
}

type Turtle struct {
    arena         *Arena
    x, y, w, h    int
    speed, dx, dy int
}

func NewTurtle(arena *Arena, pos Point) *Turtle {
    a := &Turtle{arena, pos.X, pos.Y, 20, 20, 2, 0, 0}
    arena.Add(a)
    return a
}

func (a *Turtle) Move() {
    as := a.arena.Size()
    a.x += a.dx
    if a.x < 0 {
        a.x = 0
    } else if a.x > as.W-a.w {
        a.x = as.W - a.w
    }
    a.y += a.dy
    if a.y < 0 {
        a.y = 0
    } else if a.y > as.H-a.h {
        a.y = as.H - a.h
    }

}

func (a *Turtle) GoLeft() {
    a.dx, a.dy = -a.speed, 0
}

func (a *Turtle) GoRight() {
    a.dx, a.dy = +a.speed, 0
}

func (a *Turtle) GoUp() {
    a.dx, a.dy = 0, -a.speed
}

func (a *Turtle) GoDown() {
    a.dx, a.dy = 0, +a.speed
}

func (a *Turtle) Stay() {
    a.dx, a.dy = 0, 0
}

func (a *Turtle) Collide(other Actor) {
}

func (a *Turtle) Position() Rect {
    return Rect{a.x, a.y, a.w, a.h}
}

func (a *Turtle) Symbol() Rect {
    return Rect{0, 20, a.w, a.h}
}

/*
type BounceGame struct {
    arena *Arena
    hero  *Turtle
}

func NewBounceGame() *BounceGame {
    a := NewArena(Size{480, 360})
    t := NewTurtle(a, Point{80, 80})
    NewBall(a, Point{40, 80})
    NewBall(a, Point{80, 40})
    NewGhost(a, Point{120, 80})
    return &BounceGame{a, t}
}

func (a *BounceGame) Hero() *Turtle {
    return a.hero
}

func (a *BounceGame) Arena() *Arena {
    return a.arena
}

var game = NewBounceGame()
*/

var arena = NewArena(Size{480, 360})
var hero = NewTurtle(arena, Point{80, 80})
var ball1 = NewBall(arena, Point{40, 80})
var ball2 = NewBall(arena, Point{80, 40})
var ghost = NewGhost(arena, Point{120, 80})

var img = LoadImage("sprites.png")

func tick() {
    if KeyPressed("ArrowUp") {
        hero.GoUp()
    } else if KeyPressed("ArrowRight") {
        hero.GoRight()
    } else if KeyPressed("ArrowDown") {
        hero.GoDown()
    } else if KeyPressed("ArrowLeft") {
        hero.GoLeft()
    } else if KeyReleased("ArrowUp") || KeyReleased("ArrowRight") ||
            KeyReleased("ArrowDown") || KeyReleased("ArrowLeft") {
        hero.Stay()
    }

    arena.MoveAll()
    ClearCanvas()
    for _, a := range arena.Actors() {
        DrawImageClip(img, a.Symbol(), a.Position())
    }
}

func main() {
    InitCanvas(arena.Size())
    MainLoop(tick)
}
