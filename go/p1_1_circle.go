package main

import (
	. "g2d"
	"math"
)

func main() {
	r := ToFloat(Prompt("Radius? "))
	if r >= 0 {
		Println("Area: ", math.Pi*r*r)
		Println("Perimeter: ", 2*math.Pi*r)
	} else {
		Alert("Error: negative radius")
	}
}
