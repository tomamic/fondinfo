package main

import (
	. "g2d"
	"math"
)

func hypotenuse(cathetus1, cathetus2 float64) float64 {
	/*
	   Return the hypotenuse of a right triangle,
	   given both its legs (catheti).
	*/
	return math.Sqrt(cathetus1*cathetus1 + cathetus2*cathetus2)
}

func main() {
	a := ParseFloat(Prompt("a? "))
	b := ParseFloat(Prompt("b? "))
	c := hypotenuse(a, b)
	Println(c)
}

