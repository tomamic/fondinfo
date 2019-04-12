package main

import . "g2d"

func main() {
    capital := ToFloat(Prompt("Capital?"))
    rate := ToFloat(Prompt("Interest rate?"))
    years := ToInt(Prompt("Years?"))
    i := 0
    for i <= years {
        Println(i, capital)
        capital += capital * rate / 100
        i += 1
    }
}

