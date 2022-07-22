import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.content = []
        for key, value in kwargs.items():
            self.content += [key] * value

    def draw(self, qty):
        drawn = [self.pop_random_item() for i in range(qty)]
        return drawn

    def pop_random_item(self):
        index = random.randrange(len(self.content))
        return self.content.pop(index)


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
hat = Hat(blue=4, red=2, green=6)
print(hat.content)
draw = hat.draw(3)
print(draw)
print(hat.content)
