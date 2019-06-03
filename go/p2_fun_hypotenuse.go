package main

import (
    . "g2d"
    "math"
)

// Return the hypotenuse of a right triangle,
// given both its legs (catheti).
func hypotenuse(cathetus1, cathetus2 float64) float64 {
    return math.Sqrt(cathetus1*cathetus1 + cathetus2*cathetus2)
}

func main() {
    a := ToFloat(Prompt("a? "))
    b := ToFloat(Prompt("b? "))
    c := hypotenuse(a, b)
    Alert(c)
}
