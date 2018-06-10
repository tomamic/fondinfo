package main

import "fmt"

func main() {
	max := 10
	for y := 1; y <= max; y++ {
		for x := 1; x <= max; x++ {
			fmt.Printf("%4d", x*y)
		}
		fmt.Println()
	}
}

