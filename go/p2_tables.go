package main

import . "g2d"

func main() {
    max := 10
    for y := 1; y <= max; y++ {
        for x := 1; x <= max; x++ {
            Printf("%4d", x*y)
        }
        Println()
    }
}
