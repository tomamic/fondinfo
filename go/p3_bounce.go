package main

import (
	. "g2d"
)

type Ball struct {
	arena         *Arena
	x, y, w, h    int
	speed, dx, dy int
}

func NewBall(a *Arena, pos Point) *Ball {
	b := &Ball{a, pos.X, pos.Y, 20, 20, 5, 5, 5}
	a.Add(b)
	return b
}

func (b *Ball) Move() {
	as := b.arena.Size()
	if !(0 <= b.x+b.dx && b.x+b.dx <= as.W-b.w) {
		b.dx = -b.dx
	}
	if !(0 <= b.y+b.dy && b.y+b.dy <= as.H-b.h) {
		b.dy = -b.dy
	}
	b.x += b.dx
	b.y += b.dy
}

func (b *Ball) Position() Rect {
	return Rect{b.x, b.y, b.w, b.h}
}

func (b *Ball) Symbol() Rect {
	return Rect{0, 0, b.h, b.w}
}

func (b *Ball) Collide(other Actor) {
	_, ok := other.(*Ghost)
	if !ok {
		op := other.Position()
		if op.X < b.x {
			b.dx = b.speed
		} else {
			b.dx = -b.speed
		}
		if op.Y < b.y {
			b.dy = b.speed
		} else {
			b.dy = -b.speed
		}
	}
}

type Ghost struct {
	arena      *Arena
	x, y, w, h int
	speed      int
	visible    bool
}

func NewGhost(a *Arena, pos Point) *Ghost {
	g := &Ghost{a, pos.X, pos.Y, 20, 20, 5, true}
	a.Add(g)
	return g
}

func (g *Ghost) Move() {
	as := g.arena.Size()
	dx := RandInt(-1, 1) * g.speed
	dy := RandInt(-1, 1) * g.speed
	g.x = (g.x + dx + as.W) % as.W
	g.y = (g.y + dy + as.H) % as.H

	if RandInt(0, 99) == 0 {
		g.visible = !g.visible
	}
}

func (g *Ghost) Position() Rect {
	return Rect{g.x, g.y, g.w, g.h}
}

func (g *Ghost) Symbol() Rect {
	if g.visible {
		return Rect{20, 0, g.w, g.h}
	}
	return Rect{20, 20, g.w, g.h}
}

func (g *Ghost) Collide(other Actor) {
}

type Turtle struct {
	arena         *Arena
	x, y, w, h    int
	speed, dx, dy int
}

func NewTurtle(a *Arena, pos Point) *Turtle {
	t := &Turtle{a, pos.X, pos.Y, 20, 20, 2, 0, 0}
	a.Add(t)
	return t
}

func (t *Turtle) Move() {
	as := t.arena.Size()
	t.x += t.dx
	if t.x < 0 {
		t.x = 0
	} else if t.x > as.W-t.w {
		t.x = as.W - t.w
	}
	t.y += t.dy
	if t.y < 0 {
		t.y = 0
	} else if t.y > as.H-t.h {
		t.y = as.H - t.h
	}

}

func (t *Turtle) GoLeft() {
	t.dx, t.dy = -t.speed, 0
}

func (t *Turtle) GoRight() {
	t.dx, t.dy = +t.speed, 0
}

func (t *Turtle) GoUp() {
	t.dx, t.dy = 0, -t.speed
}

func (t *Turtle) GoDown() {
	t.dx, t.dy = 0, +t.speed
}

func (t *Turtle) Stay() {
	t.dx, t.dy = 0, 0
}

func (t *Turtle) Collide(other Actor) {
}

func (t *Turtle) Position() Rect {
	return Rect{t.x, t.y, t.w, t.h}
}

func (t *Turtle) Symbol() Rect {
	return Rect{0, 20, t.w, t.h}
}

/*
type BounceGame struct {
	arena *Arena
	hero  *Turtle
}

func NewBounceGame() *BounceGame {
	a := NewArena(Size{320, 240})
	t := NewTurtle(a, Point{80, 80})
	NewBall(a, Point{40, 80})
	NewBall(a, Point{80, 40})
	NewGhost(a, Point{120, 80})
	return &BounceGame{a, t}
}

func (g *BounceGame) Hero() *Turtle {
	return g.hero
}

func (g *BounceGame) Arena() *Arena {
	return g.arena
}

var game = NewBounceGame()
*/

var img = LoadImage("sprites.png")
var arena = NewArena(Size{320, 240})
var hero = NewTurtle(arena, Point{80, 80})

func update() {
	arena.MoveAll()
	FillCanvas(Color{255, 255, 255})
	for _, b := range arena.Actors() {
		DrawImageClip(img, b.Position(), b.Symbol())
	}
}

func keydown(code string) {
	if code == "ArrowUp" {
		hero.GoUp()
	} else if code == "ArrowDown" {
		hero.GoDown()
	} else if code == "ArrowLeft" {
		hero.GoLeft()
	} else if code == "ArrowRight" {
		hero.GoRight()
	}
}

func keyup(code string) {
	hero.Stay()
}

func main() {
	NewBall(arena, Point{40, 80})
	NewBall(arena, Point{80, 40})
	NewGhost(arena, Point{120, 80})
	InitCanvas(arena.Size())
	HandleKeyboard(keydown, keyup)
	MainLoop(update, 1000/60)
}

