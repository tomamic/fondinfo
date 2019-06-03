package main

import . "g2d"
import "math"

func EllipseArea(a, b float64) float64 {
    return math.Pi * a * b
}

func main() {
    a0 := ToFloat(Prompt("a?"))
    b0 := ToFloat(Prompt("b?"))
    area := EllipseArea(a0, b0)
    Println(area)
}
