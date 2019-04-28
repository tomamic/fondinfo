package main

import . "g2d"

func main() {
	InitCanvas(Size{600, 400}) // width, height

	SetColor(Color{255, 255, 0})       // red + green = yellow
	FillRect(Rect{150, 100, 250, 200}) // left, top, width, height

	SetColor(Color{0, 255, 0})
	DrawLine(Point{150, 100}, Point{400, 300})

	SetColor(Color{0, 0, 255})
	FillCircle(Point{400, 300}, 20) // center, radius

	SetColor(Color{255, 0, 0})
	DrawText("Hello", Point{150, 100}, 40) // text, left-top, font-size

	MainLoop() // manage the window/canvas
}
