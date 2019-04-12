package gui

import (
    "boardgame"
    . "g2d"
    "time"
)

var W, H int = 40, 40
var LONG_PRESS float64 = 0.5

type Gui struct {
    game     boardgame.Game
    downtime time.Time
}

func NewGui(game boardgame.Game) *Gui {
    ui := &Gui{game, time.Time{}}
    InitCanvas(Size{game.Cols() * W, game.Rows() * H})
    ui.Update()
    UpdateCanvas()
    HandleKeys(ui.keydown, ui.keyup)
    return ui
}

func (ui *Gui) MainLoop() {
    MainLoop(nil, 0)
}

func (ui *Gui) keydown(code string) {
    if code == "LeftButton" {
        ui.downtime = time.Now()
    }
}

func (ui *Gui) keyup(code string) {
    if code == "LeftButton" {
        pos := MousePosition()
        if time.Now().Sub(ui.downtime).Seconds() > LONG_PRESS {
            ui.game.FlagAt(pos.X/W, pos.Y/H)
        } else {
            ui.game.PlayAt(pos.X/W, pos.Y/H)
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
        DrawLine(Point{0, y * H}, Point{cols * W, y * H})
    }
    for x := 1; x < cols; x++ {
        DrawLine(Point{x * W, 0}, Point{x * W, rows * H})
    }
    for y := 0; y < rows; y++ {
        for x := 0; x < cols; x++ {
            center := Point{x*W + W/2, y*H + H/2}
            DrawTextCentered(ui.game.ValueAt(x, y), center, H/2)
        }
    }
    UpdateCanvas()
    if ui.game.Finished() {
        Alert(ui.game.Message())
        Exit()
    }
}
