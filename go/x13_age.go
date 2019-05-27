package main

import . "g2d"

func main() {
    birthYear := ToInt(Prompt("Birth year? "))
    birthMonth := ToInt(Prompt("Birth month? "))
    birthDay := ToInt(Prompt("Birth day? "))
    currentYear := ToInt(Prompt("Current year? "))
    currentMonth := ToInt(Prompt("Current month? "))
    currentDay := ToInt(Prompt("Current day? "))

    age := currentYear - birthYear
    if currentMonth < birthMonth || (currentMonth == birthMonth &&
            currentDay < birthDay) {
        age = age - 1
    }

    Alert("Your age is ", age)
}
