import Control.Monad

maxX = 320
maxY = 240

data Ball = Ball { x :: Int
                 , y :: Int
                 , dx :: Int
                 , dy :: Int
                 } deriving (Show)

moveX :: Ball -> Ball
moveX (Ball x y dx dy)
    | 0 <= x + dx && x + dx < maxX = Ball (x + dx) y dx dy
    | otherwise                    = Ball (x - dx) y (-dx) dy

moveY :: Ball -> Ball
moveY (Ball x y dx dy)
    | 0 <= y + dy && y + dy < maxY = Ball x (y + dy) dx dy
    | otherwise                    = Ball x (y - dy) dx (-dy)

move :: Ball -> Ball
move = moveX . moveY 

data BallArena = BallArena { balls :: [Ball]
                           } deriving (Show)

moveAll :: BallArena -> BallArena
moveAll (BallArena balls) = BallArena (map move balls)

operateArena :: BallArena -> IO ()
operateArena a = do
    print a
    line <- getLine
    when (null line) $ operateArena (moveAll a)
        
main = do
    operateArena (BallArena [Ball 200 100 5 5, Ball 300 200 10 0])

