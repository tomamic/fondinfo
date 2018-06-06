package main

import . "g2d"

func main() {
	capital := ParseFloat(Prompt("Capital?"))
	rate := ParseFloat(Prompt("Interest rate?"))
	years := ParseInt(Prompt("Years?"))
	i := 0
	for i <= years {
		Println(i, capital)
		capital += capital * rate / 100
		i += 1
	}
}

