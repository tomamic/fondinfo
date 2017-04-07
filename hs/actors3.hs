import System.Random
import Control.Monad

class (Show a) => Actor a where
    move :: a -> a

data Arena a = Arena { actors :: [a]
                     } deriving (Show)

moveAll :: (Actor a) => Arena a -> Arena a
moveAll (Arena actors) = Arena (map move actors)

operateArena :: (Actor a) => Arena a -> IO ()
operateArena a = do
    print a
    line <- getLine
    when (null line) $ operateArena (moveAll a)

----

maxX = 320
maxY = 240

data BasicActor = Ball { x :: Int
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

instance Actor BasicActor where
    move = moveX . moveY 

----

data Wall = Wall { wx :: Int
                 , wy :: Int
                 } deriving (Show)

instance Actor Wall where
    move = id    -- move w = w
        
----

main = do
    rnd <- newStdGen
    operateArena (Arena [Ball 200 100 5 5, Ghost 100 100 rnd])
    -- try to add a Wall to the actors

