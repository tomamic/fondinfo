package boardgame

import . "g2d"
import "time"

var W, H int = 40, 40
var LONG_PRESS float64 = 0.5

type BoardGameGui struct {
    game BoardGame
    downtime time.Time
}

func NewBoardGameGui(game BoardGame) *BoardGameGui {
    gui := &BoardGameGui{game, time.Time{}}
    InitCanvas(Size{game.Cols() * W, game.Rows() * H})
    gui.Update()
    HandleKeys(gui.keydown, gui.keyup)
    return gui
}

func (gui *BoardGameGui) MainLoop() {
    MainLoop(nil, 1000/30)
}

func (gui *BoardGameGui) keydown(code string, pos Point) {
    if code == "LeftButton" {
        gui.downtime = time.Now()
    }
}

func (gui *BoardGameGui) keyup(code string, pos Point) {
    if code == "LeftButton" {
        if time.Now().Sub(gui.downtime).Seconds() > LONG_PRESS {
            gui.game.FlagAt(pos.X, pos.Y)
        } else {
            gui.game.PlayAt(pos.X, pos.Y)
            gui.Update()
        }
    }
}

func (gui *BoardGameGui) Update() {
    FillCanvas(Color{255, 255, 255})
    rows, cols := gui.game.Rows(), gui.game.Cols()
    for y := 1; y < rows; y++ {
        DrawLine(Color{0, 0, 0}, Point{0, y * H}, Point{cols * W, y * H})
    }
    for x := 1; x < cols; x++ {
        DrawLine(Color{0, 0, 0}, Point{x * W, 0}, Point{x * W, rows * H})
    }
    for y := 0; y < rows; y++ {
        for x := 0; x < cols; x++ {
            DrawTextCentered(gui.game.GetVal(x, y), Color{0, 0, 0},
                Point{x * W + W/2, y * H + H/2}, H/2)
        }
    }
    UpdateCanvas()
    if gui.game.Finished() {
        Alert(gui.game.Message())
        // g2d.draw_text_centered(self._game.message(), (0, 0, 255),
        //     (cols * W/2, rows * H/2), H/2)
        Exit()
    }
}
