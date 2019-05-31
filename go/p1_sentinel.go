package main

import . "g2d"

func main() {
    count := 0
    total := 0

    val := ToInt(Prompt("Val? [0 to end]"))
    for val != 0 {
        total += val  // total = total + val
        count += 1    // count = count + 1
        val = ToInt(Prompt("Val? [0 to end]"))
    }
    if count != 0 {
        Alert("The average is ",
              float64(total) / float64(count))
    }
}
