package main

import . "g2d"

func main() {
	values := []int{}
	max := 0
	val := ParseInt(Prompt("Val? "))
	for val > 0 {
		values = append(values, val)
		if val > max {
			max = val
		}
		val = ParseInt(Prompt("Val? "))
	}

	width, height := 600, 400
	InitCanvas(Size{width, height})
	if len(values) > 0 {
		for i, v := range values {
			rect := Rect{0, i * height/len(values), v * width / max, height/len(values) - 1}
			DrawRect(Color{100, 100, 100}, rect)
		}
	}
}

