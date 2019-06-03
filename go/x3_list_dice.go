package main

import . "g2d"

func main() {
    dieSides := 6
    numResults := 11
    n := ToInt(Prompt("n?"))
    results := make([]int, numResults)

    for i := 0; i < n; i++ {
        die1 := RandInt(1, dieSides)
        die2 := RandInt(1, dieSides)
        val := die1 + die2
        results[val - 2] += 1
    }

    for i, v := range results {
        Printf("Result %d has come out %d times.\n", i+2, v)
    }
}
