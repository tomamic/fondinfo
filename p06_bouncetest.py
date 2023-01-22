from unittest import TestCase, main
from unittest.mock import Mock
from p05_bouncegame import Arena, Ball, Ghost, TurtleHero


class BallTest(TestCase):

    def test_corner(self):
        arena = Mock()
        arena.size.return_value = (480, 360)
        arena.collisions.return_value = []
        ball = Ball((460, 340))  # dx = 4, dy = 4
        ball.move(arena)  # dx = -4, dy = -4
        ball.move(arena)
        self.assertEqual(ball.pos(), (452, 332))

    def test_move(self):
        arena = Mock()
        arena.size.return_value = (480, 360)
        arena.collisions.return_value = []
        test_values = ( (40, 80, 44, 84),
                        (40, 215, 44, 219),
                        (40, 340, 44, 336),
                        (295, 80, 299, 84),
                        (460, 80, 456, 84) )
        for param in test_values:
            x0, y0, x1, y1 = param
            ball = Ball((x0, y0))
            ball.move(arena)
            self.assertEqual(ball.pos(), (x1, y1))


class TurtleTest(TestCase):

    def test_right(self):
        arena = Mock()
        arena.size.return_value = (480, 360)
        arena.current_keys.return_value = ["ArrowRight"]
        arena.collisions.return_value = []
        turtle = TurtleHero((230, 170))
        turtle.move(arena)
        turtle.move(arena)
        arena.current_keys.return_value = []
        turtle.move(arena)  # no effect
        self.assertEqual(turtle.pos(), (234, 170))

    def test_collide_ball(self):
        ball = Mock(spec=Ball)  # to fool isinstance
        arena = Mock()
        arena.size.return_value = (480, 360)
        arena.current_keys.return_value = []
        arena.collisions.return_value = [ball]
        turtle = TurtleHero((230, 170))
        turtle.move(arena)
        turtle.move(arena)  # no effect
        self.assertEqual(turtle.lives(), 2)

    def test_collide_ghost(self):
        ghost = Mock(spec=Ghost)  # to fool isinstance
        arena = Mock()
        arena.size.return_value = (480, 360)
        arena.current_keys.return_value = []
        arena.collisions.return_value = [ghost]
        turtle = TurtleHero((230, 170))
        turtle.move(arena)
        self.assertEqual(turtle.lives(), 3)


if __name__ == '__main__':
    main()
