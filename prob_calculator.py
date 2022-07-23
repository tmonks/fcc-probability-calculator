import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.content = []
        for key, value in kwargs.items():
            self.content += [key] * value

    def draw(self, qty):
        if qty >= len(self.content):
            drawn = self.content
            self.content = []
        else:
            drawn = [self.pop_random_item() for i in range(qty)]
        return drawn

    def pop_random_item(self):
        index = random.randrange(len(self.content))
        return self.content.pop(index)


def count_balls(balls):
    counts = {}
    for ball in balls:
        counts[ball] = (counts.get(ball) or 0) + 1
    return counts


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
hat = Hat(blue=4, red=2, green=6)
print(hat.content)
draw = hat.draw(33)
print(draw)
print(count_balls(draw))
# print(hat.content)
