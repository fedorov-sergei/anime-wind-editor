import math


class Animator:

    def __init__(self):
        self.time = 0.0

        self.layers = {
            1: {
                "axis": "x",
                "amplitude": 10.0,
                "speed": 2.0,
            },
            2: {
                "axis": "y",
                "amplitude": 6.0,
                "speed": 1.5,
            },
        }

    def update(self, dt):
        self.time += dt

    def get_offset(self, layer_index):

        settings = self.layers.get(layer_index)

        if settings is None:
            return (0, 0)

        value = math.sin(self.time * settings["speed"]) * settings["amplitude"]

        if settings["axis"] == "x":
            return (value, 0)

        if settings["axis"] == "y":
            return (0, value)

        return (0, 0)
