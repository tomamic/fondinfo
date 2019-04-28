package main

import . "g2d"

func main() {
	InitCanvas(Size{400, 400})

	i := 0
	for i < 10 {
		x := i * 25
		y := i * 25
		red := i * 25
		SetColor(Color{red, 0, 0})
		FillRect(Rect{x, y, 100, 100})
		i += 1
	}
	MainLoop()
}
