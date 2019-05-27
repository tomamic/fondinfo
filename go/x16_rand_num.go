package main

import . "g2d"

func main() {
	secret := RandInt(1, 90)

	guess := ToInt(Prompt("Guess? "))
	for guess != secret {
		msg := "Too small. Guess? "
		if guess > secret {
			msg = "Too big. Guess? "
		}
		guess = ToInt(Prompt(msg))
	}
	Alert("Eureka! The secret is ", secret)
}
