package main

import (
	"boardgame/gui"
	"math/rand"
)

// https://en.wikipedia.org/wiki/Lights_Out_(game)

type LightsOut struct {
	cols, rows int
	board      []bool
}

func NewLightsOut(side, level int) *LightsOut {
	g := &LightsOut{side, side, make([]bool, side*side)}
	for i := 0; i < level; i++ {
		g.PlayAt(rand.Intn(side), rand.Intn(side))
	}
	return g
}

func (g *LightsOut) Cols() int {
	return g.cols
}

func (g *LightsOut) Rows() int {
	return g.rows
}

func (g *LightsOut) Finished() bool {
	for y := 0; y < g.rows; y++ {
		for x := 0; x < g.cols; x++ {
			if g.board[y*g.cols+x] {
				return false
			}
		}
	}
	return true
}

func (g *LightsOut) PlayAt(x, y int) {
	// Place (or remove) a light at cell (x, y)
	if 0 <= x && x < g.cols && 0 <= y && y < g.rows {
		for _, d := range [][]int{{0, 0}, {0, -1}, {1, 0},
			{0, 1}, {-1, 0}} {
			x1, y1 := x+d[0], y+d[1]
			if 0 <= x1 && x1 < g.cols && 0 <= y1 && y1 < g.rows {
				g.board[y1*g.cols+x1] = !g.board[y1*g.cols+x1]
			}
		}
	}
}

func (g *LightsOut) FlagAt(x, y int) {
}

func (g *LightsOut) ValueAt(x, y int) string {
	if 0 <= x && x < g.cols && 0 <= y && 0 <= y && y < g.rows && g.board[y*g.cols+x] {
		return "@"
	}
	return "-"
}

func (g *LightsOut) Message() string {
	return "Puzzle solved!"
}

func main() {
	game := NewLightsOut(6, 5)
	ui := gui.NewGui(game)
	ui.MainLoop()
	//boardgame.ConsolePlay(game)
}
