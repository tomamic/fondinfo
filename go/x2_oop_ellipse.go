package main

import "math"
import . "g2d"

type Ellipse struct {
    a, b float64
}

func NewEllipse(a, b float64) *Ellipse {
    return &Ellipse{a, b}
}

func (e *Ellipse) Area() float64 {
    return math.Pi * e.a * e.b
}

func (e *Ellipse) FocalDistance() float64 {
    return 2 * math.Sqrt(math.Abs(e.a*e.a - e.b*e.b))
}

func main() {
    val_a := ToFloat(Prompt("a?"))
    val_b := ToFloat(Prompt("b?"))
    e := NewEllipse(val_a, val_b)
    area := e.Area()
    dist := e.FocalDistance()
    Println("Area: ", area)
    Println("Dist: ", dist)
}
