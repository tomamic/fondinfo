package main

import (
	. "g2d"
	"math"
)

func EllipseArea(a, b float64) float64 {
	return math.Pi * a * b
}

func main() {
	a0 := ParseFloat(Prompt("a?"))
	b0 := ParseFloat(Prompt("b?"))
	area := EllipseArea(a0, b0)
	Println(area)
}

