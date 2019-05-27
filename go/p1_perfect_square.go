package main

import . "g2d"

func main() {
    n := ToInt(Prompt("n?"))

    i := 1
    for i*i < n {
        i++
    }
    if i*i == n {
        Alert(i)
    } else {
        Alert("No")
    }
}
