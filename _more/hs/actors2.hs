import System.Random
import Control.Monad

maxX = 320
maxY = 240

data BasicActor = Ball    { x :: Int
                          , y :: Int
                          , dx :: Int
                          , dy :: Int
                  }
                  | Ghost { x :: Int
                          , y :: Int
                          , rnd :: StdGen
                  } deriving (Show)

moveX :: BasicActor -> BasicActor
moveX (Ball x y dx dy)
    | 0 <= x + dx && x + dx < maxX = Ball (x + dx) y dx dy
    | otherwise                    = Ball (x - dx) y (-dx) dy
moveX (Ghost x y rnd) = Ghost x' y rnd'
    where (d, rnd') = randomR (-1,1) rnd
          x' = (x + 5 * d) `mod` maxX

moveY :: BasicActor -> BasicActor
moveY (Ball x y dx dy)
    | 0 <= y + dy && y + dy < maxY = Ball x (y + dy) dx dy
    | otherwise                    = Ball x (y - dy) dx (-dy)
moveY (Ghost x y rnd) = Ghost x y' rnd'
    where (d, rnd') = randomR (-1,1) rnd
          y' = (y + 5 * d) `mod` maxY

move :: BasicActor -> BasicActor
move = moveX . moveY 

data BasicArena = BasicArena { actors :: [BasicActor]
                             } deriving (Show)

moveAll :: BasicArena -> BasicArena
moveAll (BasicArena actors) = BasicArena (map move actors)


operateBasicArena :: BasicArena -> IO ()
operateBasicArena a = do
    print a
    line <- getLine
    when (null line) $ operateBasicArena (moveAll a)
        
main = do
    rnd <- newStdGen
    operateBasicArena (BasicArena [Ball 200 100 5 5, Ghost 100 100 rnd])

