package main

import . "g2d"

func main() {
    n := ToInt(Prompt("How many values?"))
    count := 0
    total := 0

    for count < n {
        val := ToInt(Prompt("Val?"))
        total += val  // total = total + val
        count += 1    // count = count + 1
    }
    if count != 0 {
        Alert("The average is ",
              float64(total) / float64(count))
    }
}
