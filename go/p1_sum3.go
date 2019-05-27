package main

import . "g2d"

func main() {
    a := ToFloat(Prompt("Insert 1st val"))
    b := ToFloat(Prompt("Insert 2nd val"))
    c := ToFloat(Prompt("Insert 3rd val"))

    total := a + b + c
    Alert("The sum is ", total)
}
