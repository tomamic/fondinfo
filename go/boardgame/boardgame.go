package boardgame

import "fmt"

type Game interface {
    PlayAt(x, y int)
    FlagAt(x, y int)
    ValueAt(x, y int) string
    Cols() int
    Rows() int
    Finished() bool
    Message() string
}

func ConsolePrint(game Game) {
    for y := 0; y < game.Rows(); y++ {
        for x := 0; x < game.Cols(); x++ {
            fmt.Printf("%3s", game.ValueAt(x, y))
        }
        fmt.Println()
    }
}

func ConsolePlay(game Game) {
    ConsolePrint(game)

    for ! game.Finished() {
        var x, y int
        fmt.Scan(&x, &y)
        game.PlayAt(x, y)
        ConsolePrint(game)
    }

    fmt.Println(game.Message())
}
