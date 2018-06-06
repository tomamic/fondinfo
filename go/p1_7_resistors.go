package main

import . "g2d"

func main() {
	val := ParseFloat(Prompt("Resistance?"))
	sum, inv := 0.0, 0.0
	for val != 0 {
		sum += val
		inv += 1 / val
		val = ParseFloat(Prompt("Resistance?"))
	}
	Println("Series: ", sum)
	Println("Parallel: ", 1/inv)
}

