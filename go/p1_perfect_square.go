package main

import . "g2d"

func main() {
    n := ToInt(Prompt("n? "))
    result := 0

    i := 1
    for i * i <= n {
        if i * i == n {
            result = i
        }
        i += 1
    }

    if result == 0 {
        Alert("No")
    } else {
        Alert(result)
    }
}
