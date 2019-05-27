package main

import (
    . "g2d"
    "math"
)

func main() {
    r := ToFloat(Prompt("Radius? "))
    if r >= 0 {
        Alert("Area: ", math.Pi*r*r)
        Alert("Perimeter: ", 2*math.Pi*r)
    } else {
        Alert("Error: negative radius")
    }
}
