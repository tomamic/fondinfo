package main

import . "g2d"

func main() {
    InitCanvas(Point{400, 400}) // width, height
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

    MainLoop()
}
