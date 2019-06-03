package main

import . "g2d"

func main() {
	a := RandInt(1, 6)
	b := RandInt(1, 6)
	c := RandInt(1, 6)
	Println(a, b, c)
	if a <= b && a <= c {
		Println(a)
	} else if b <= c {
		Println(b)
	} else {
		Println(c)
	}
}
