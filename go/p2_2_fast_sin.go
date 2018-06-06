package main

import (
	. "g2d"
	"math"
)

func main() {
	vect := make([]float64, 360)
	for x := 0; x < 360; x++ {
		vect[x] = math.Sin(float64(x) * math.Pi / 180)
	}
	angle := ParseInt(Prompt("Angle?"))
	for 0 <= angle && angle < 360 {
		Println()
		angle = ParseInt(Prompt("Sin(", angle, ") = ", vect[angle], "\nNew angle?"))
	}
}

