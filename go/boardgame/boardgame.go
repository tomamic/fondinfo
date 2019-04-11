package boardgame

import "fmt"

type BoardGame interface {
    PlayAt(x, y int)
    FlagAt(x, y int)
    GetVal(x, y int) string
    Cols() int
    Rows() int
    Finished() bool
    Message() string
}

func PrintGame(game BoardGame) {
    for y := 0; y < game.Rows(); y++ {
        for x := 0; x < game.Cols(); x++ {
            fmt.Printf("%3d", game.GetVal(x, y))
        }
        fmt.Println()
    }
}

func ConsolePlay(game BoardGame) {
    PrintGame(game)

    for ! game.Finished() {
        var x, y int
        fmt.Scan(&x, &y)
        game.PlayAt(x, y)
        PrintGame(game)
    }

    fmt.Println(game.Message())
}
