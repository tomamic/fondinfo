package main

import . "g2d"

var image = LoadImage("ball.png")
var x, dx = 50, 5

func update() {
	FillCanvas(Color{255, 255, 255}) // Draw background
	DrawImage(image, Point{x, 50})   // Draw foreground
	if x+dx < 0 || x+dx+20 > 320 {
		dx = -dx
	}
	x = x + dx // Update ball's position
}

func main() {
	InitCanvas(Size{320, 240})
	MainLoop(update, 1000/30) // Call update 30 times/second
}

