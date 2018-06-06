package main

import . "g2d"

func main() {
	txt := Prompt("Text?")
	count, sum := 0, 0
	for _, c := range txt {
		if '0' <= c && c <= '9' {
			count += 1
			sum += int(c - '0')
		}
	}
	Println(count, sum)
}

