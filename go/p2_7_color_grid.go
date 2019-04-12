package main

import . "g2d"

func main() {
    InitCanvas(Size{320, 240})
    rows := ToInt(Prompt("Rows?"))
    cols := ToInt(Prompt("Cols?"))
    w, h := 320 / cols, 240 / rows
    dg, db := 255 / (rows - 1), 255 / (cols - 1)
    for y := 0; y < rows; y++ {
        for x := 0; x < cols; x++ {
            SetColor(Color{0, y * dg, x * db}, )
            FillRect(Rect{x * w, y * h, w - 1, h - 1})
        }
    }
    MainLoop(nil, 0)
}

