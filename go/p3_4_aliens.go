package main

import . "g2d"

var as = Size{300, 300}
var aliens = []*Alien{NewAlien(Point{50, 50}), NewAlien(Point{80, 80})}

type Alien struct {
	x, y, w, h int
	dx, dy, x0 int
}

func NewAlien(pos Point) *Alien {
	return &Alien{pos.X, pos.Y, 20, 20, 5, 5, pos.X}
}

func (b *Alien) Move() {
	if !(b.x0 <= b.x+b.dx && b.x+b.dx <= b.x0+150-b.w) {
		b.y += b.dy
		b.dx = -b.dx
	} else {
		b.x += b.dx
	}
}

func (b *Alien) Position() Rect {
	return Rect{b.x, b.y, b.w, b.h}
}

func update() {
	FillCanvas(Color{255, 255, 255}) // BG
	for _, i := range aliens {
		i.Move()
		DrawRect(Color{100, 100, 100}, i.Position()) // FG
	}
}

func main() {
	InitCanvas(as)
	MainLoop(update, 1000/10)
}

