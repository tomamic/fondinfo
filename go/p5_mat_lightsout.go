package main

import (
    "g2d"
    "math/rand"
)

// <https://en.wikipedia.org/wiki/Lights_Out_(game)>
type LightsOut struct {
    w, h int
    board      []bool
}

func NewLightsOut(w, h, level int) *LightsOut {
    g := &LightsOut{w, h, make([]bool, w*h)}
    for i := 0; i < level; i++ {
        g.PlayAt(rand.Intn(w), rand.Intn(h))
    }
    return g
}

func (g *LightsOut) Cols() int {
    return g.w
}

func (g *LightsOut) Rows() int {
    return g.h
}

func (g *LightsOut) Finished() bool {
    for y := 0; y < g.h; y++ {
        for x := 0; x < g.w; x++ {
            if g.board[y*g.w+x] {
                return false
            }
        }
    }
    return true
}

func (g *LightsOut) PlayAt(x, y int) {
    // Place (or remove) a light at cell (x, y)
    if 0 <= x && x < g.w && 0 <= y && y < g.h {
        for _, d := range [][]int{{0, 0}, {0, -1}, {1, 0},
            {0, 1}, {-1, 0}} {
            x1, y1 := x+d[0], y+d[1]
            if 0 <= x1 && x1 < g.w && 0 <= y1 && y1 < g.h {
                g.board[y1*g.w+x1] = !g.board[y1*g.w+x1]
            }
        }
    }
}

func (g *LightsOut) FlagAt(x, y int) {
}

func (g *LightsOut) ValueAt(x, y int) string {
    if 0 <= x && x < g.w && 0 <= y && 0 <= y && y < g.h && g.board[y*g.w+x] {
        return "@"
    }
    return "-"
}

func (g *LightsOut) Message() string {
    return "Puzzle solved!"
}

func main() {
    game := NewLightsOut(5, 5, 4)
    g2d.GuiPlay(game)
    //boardgame.ConsolePlay(game)
}
