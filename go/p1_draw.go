package main

import . "g2d"

func main() {
    InitCanvas(Size{600, 400})

    // Yellow rectangle, left=150, top=100, w=250, h=200
    // red=255 (max), green=255 (max), blue=0 (min)
    DrawRect(Color{255, 255, 0}, Rect{150, 100, 250, 200})

    // Green diagonal
    DrawLine(Color{0, 255, 0}, Point{150, 100}, Point{400, 300})

    // Blue circle, center=(400, 300), radius=20
    DrawCircle(Color{0, 0, 255}, Point{400, 300}, 20)

    // Red text, pos=(150, 100), size=40
    DrawText("Hello", Color{255, 0, 0}, Point{150, 100}, 40)
}
