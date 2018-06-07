package main

import . "g2d"

func main() {
    w, h := 640, 480
    side := 100

	n := ParseInt(Prompt("N? "))

	InitCanvas(Size{w, h})
    i := 0
    for i < n {
		r, g, b := RandInt(0, 255), RandInt(0, 255), RandInt(0, 255)
		x, y := RandInt(0, w - side), RandInt(0, h - side)
		DrawRect(Color{r, g, b}, Rect{x, y, side, sice})
		i += 1
    }
}

