import math


class Animator:

    def __init__(self):

        self.time = 0.0

    def update(self, dt):

        self.time += dt

    def get_offset(self, layer_index):

        if layer_index != 0:
            return (0, 0)

        x = math.sin(self.time * 2.0) * 10

        return (x, 0)
