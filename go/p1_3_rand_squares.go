package main

import . "g2d"

func main() {
	n := ParseInt(Prompt("N? "))

	InitCanvas(Size{400, 400})
	i := 0
	for i < n {
		c := Color{RandInt(0, 255), RandInt(0, 255), RandInt(0, 255)}
		r := Rect{RandInt(0, 300), RandInt(0, 300), 100, 100}
		DrawRect(c, r)
		i += 1
	}
}

