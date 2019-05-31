package boardgame

import (
    . "g2d"
    "time"
)

type Gui struct {
    game Game
    bw, bh int
    pressed time.Time
    longPress float64
}

func (ui *Gui) Tick() {
    if KeyPressed("LeftButton") {
        ui.pressed = time.Now()
    } else if KeyReleased("LeftButton") {
        pos := MousePosition()
        if time.Now().Sub(ui.pressed).Seconds() > ui.longPress {
            ui.game.FlagAt(pos.X/ui.bw, pos.Y/ui.bh)
        } else {
            ui.game.PlayAt(pos.X/ui.bw, pos.Y/ui.bh)
            ui.Update()
        }
    }
}

func (ui *Gui) Update() {
    SetColor(Color{255, 255, 255})
    ClearCanvas()
    SetColor(Color{0, 0, 0})
    rows, cols := ui.game.Rows(), ui.game.Cols()
    for y := 1; y < rows; y++ {
        DrawLine(Point{0, y*ui.bh}, Point{cols*ui.bw, y*ui.bh})
    }
    for x := 1; x < cols; x++ {
        DrawLine(Point{x*ui.bw, 0}, Point{x*ui.bw, rows*ui.bh})
    }
    for y := 0; y < rows; y++ {
        for x := 0; x < cols; x++ {
            center := Point{x*ui.bw + ui.bw/2, y*ui.bh + ui.bh/2}
            DrawTextCentered(ui.game.ValueAt(x, y), center, ui.bh/2)
        }
    }
    UpdateCanvas()
    if ui.game.Finished() {
        Alert(ui.game.Message())
        CloseCanvas()
    }
}

func GuiPlay(game Game) {
    InitCanvas(Size{game.Cols()*40, game.Rows()*40})
    ui := &Gui{game, 40, 40, time.Time{}, 0.5}
    ui.Update()
    SetFrameRate(60)
    MainLoop(ui.Tick)
}
