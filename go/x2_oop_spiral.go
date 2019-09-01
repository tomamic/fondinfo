package main

import . "g2d"
import "math"

var size = Point{600, 600}
var s = NewSpiral()

type Spiral struct {
    w    float64  // angular velocity
    i, n int
}

func NewSpiral() *Spiral {
    return &Spiral{math.Pi / 32.0, 0, 256}
}

func (s *Spiral) Move() {
    s.i = (s.i + 1) % s.n
}

func (s *Spiral) Center() Point {
    i := float64(s.i)
    x := size.X/2 + int(i * math.Cos(i * s.w))
    y := size.Y/2 + int(i * math.Sin(i * s.w))
    return Point{x, y}
}

func (s *Spiral) Radius() int {
    return s.i / 2
}

func (s *Spiral) Color() Color {
    return Color{255 - s.i, 0, s.i}
}

func tick() {
    ClearCanvas()
    s.Move()
    SetColor(s.Color())
    FillCircle(s.Center(), s.Radius())
}

func main() {
    InitCanvas(size)
    MainLoop(tick)
}
