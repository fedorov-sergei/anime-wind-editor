import math


class Animator:

    def __init__(self):

        self.time = 0.0

    def update(self, dt):

        self.time += dt
