package main

import . "g2d"
//import "fmt"

var image = LoadImage("ball.png")
var x, dx = 50, 5

func update() {
    //fmt.Println(image)
    ClearCanvas()                    // Draw background
    DrawImage(image, Point{x, 50})   // Draw foreground
    if x+dx < 0 || x+dx+20 > 320 {
        dx = -dx
    }
    x = x + dx // Update ball's position
}

func main() {
    InitCanvas(Size{320, 240})
    HandleEvents(update)
    MainLoop(30)  // 30 fps
}

