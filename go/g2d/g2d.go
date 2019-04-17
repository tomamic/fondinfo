package g2d

import (
    "fmt"
    "math/rand"
    "time"
)

type Point struct{ X, Y int }
type Size struct{ W, H int }
type Rect struct{ X, Y, W, H int }
type Color struct{ R, G, B int }

func init() {
    rand.Seed(time.Now().UnixNano())
}

func ToInt(text string) int {
    val := 0
    fmt.Sscan(text, &val)
    return val
}

func ToFloat(text string) float64 {
    val := 0.0
    fmt.Sscan(text, &val)
    return val
}

func RandInt(min, max int) int {
    return rand.Intn(max-min+1) + min
}
