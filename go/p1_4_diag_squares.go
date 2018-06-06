package main

import . "g2d"

func main() {
	n := ParseInt(Prompt("N? "))
	InitCanvas(Size{400, 400})
	i := 0
	for i < n {
		c := i * 255 / (n - 1)
		p := i * 300 / (n - 1)
		DrawRect(Color{c, 0, 0}, Rect{p, p, 100, 100})
		i += 1
	}
}

