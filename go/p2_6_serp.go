package main

import . "g2d"

var image = LoadImage("ball.png")
var x, y, dx = 50, 0, 5

func update() {
	FillCanvas(Color{255, 255, 255}) // Draw background
	DrawImage(image, Point{x, y})    // Draw foreground
	if x+dx < 0 || x+dx+20 > 320 {
		dx = -dx
		y += 5
	} else {
		x = x + dx // Update ball's position
	}
}

func main() {
	InitCanvas(Size{320, 240})
	MainLoop(update, 1000/10) // Call update 30 times/second
}

