import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value

    def draw(self, qty):
        if qty >= len(self.contents):
            drawn = copy.copy(self.contents)
            self.contents = []
        else:
            drawn = [self.pop_random_item() for i in range(qty)]

        return drawn

    def pop_random_item(self):
        index = random.randrange(len(self.contents))
        return self.contents.pop(index)


def contains_at_least(balls, expected_balls):
    counts = copy.copy(expected_balls)

    for ball in balls:
        if ball in counts:
            counts[ball] -= 1

    return all(value <= 0 for value in counts.values())


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass_count = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        if(contains_at_least(draw, expected_balls)):
            pass_count += 1

    return pass_count / num_experiments
