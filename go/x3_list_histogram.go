package main

import . "g2d"

func main() {
    values := []int{}
    max := 0
    val := ToInt(Prompt("Val? "))
    for val > 0 {
        values = append(values, val)
        if val > max {
            max = val
        }
        val = ToInt(Prompt("Val? "))
    }

    w, h, n := 600, 400, len(values)
    InitCanvas(Point{w, h})
    SetColor(Color{100, 100, 100})
    for i, v := range values {
        FillRect(Point{0, i*h/n}, Point{v*w/max, h/n - 1})
    }
    MainLoop()
}
