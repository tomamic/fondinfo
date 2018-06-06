package main

import (
	. "g2d"
	"math"
)

type Ellipse struct{ a, b float64 }

func NewEllipse(a, b float64) *Ellipse {
	return &Ellipse{a, b}
}

func (e *Ellipse) Area() float64 {
	return math.Pi * e.a * e.b
}

func (e *Ellipse) FocalDistance() float64 {
	return 2 * math.Sqrt(math.Abs(e.a*e.a-e.b*e.b))
}

func main() {
	a0 := ParseFloat(Prompt("a?"))
	b0 := ParseFloat(Prompt("b?"))
	e := NewEllipse(a0, b0)
	Println("Area: ", e.Area())
	Println("Focal distance: ", e.FocalDistance())
}

