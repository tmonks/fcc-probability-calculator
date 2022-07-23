import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value

    def draw(self, qty):
        """ removes and returns `qty` balls from contents """
        if qty >= len(self.contents):
            balls = copy.copy(self.contents)
            self.contents = []
        else:
            balls = [self._draw_random_ball() for i in range(qty)]

        return balls

    def _draw_random_ball(self):
        """ removes and returns one random ball from contents """
        index = random.randrange(len(self.contents))
        return self.contents.pop(index)


def contains(balls, expected_balls):
    """ Checks if the list of balls contains the number of each color specified in `expected_balls`"""

    expected_balls = copy.copy(expected_balls)

    for ball in balls:
        if ball in expected_balls:
            expected_balls[ball] -= 1

    return all(value <= 0 for value in expected_balls.values())


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    passed = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        if(contains(draw, expected_balls)):
            passed += 1

    return passed / num_experiments
