import math


class Animator:

    def __init__(self):
        self.time = 0.0

        self.layers = {
            1: {
                "axis": "x",
                "amplitude": 10.0,
                "speed": 2.0,
                "angle": 0.0,
            },
            2: {
                "axis": "y",
                "amplitude": 6.0,
                "speed": 1.5,
                "angle": 0.0,
            },
            3: {
                "axis": "x",
                "amplitude": 0.0,
                "speed": 0.0,
                "angle": 0.0,
            },
            4: {
                "axis": "x",
                "amplitude": 0.0,
                "speed": 0.0,
                "angle": 0.0,
            },
        }

    def set_amplitude(self, layer_index, value):
        settings = self.layers.get(layer_index)

        if settings is not None:
            settings["amplitude"] = value

    def set_speed(self, layer_index, value):
        settings = self.layers.get(layer_index)

        if settings is not None:
            settings["speed"] = value

    def get_amplitude(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return 0.0

        return settings["amplitude"]


    def get_speed(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return 0.0

        return settings["speed"]

    def set_angle(self, layer_index, value):
        settings = self.layers.get(layer_index)

        if settings is not None:
            settings["angle"] = value

    def get_angle(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return 0.0

        return settings["angle"]

    def update(self, dt):
        self.time += dt

    def get_transform(self, layer_index):

        settings = self.layers.get(layer_index)

        if settings is None:
            return (0, 0, 0)

        value = math.sin(
            self.time * settings["speed"]
        ) * settings["amplitude"]

        angle = math.radians(settings["angle"])

        x = math.cos(angle) * value
        y = math.sin(angle) * value

        return (x, y, 0)

    def set_axis(self, layer_index, axis):
        settings = self.layers.get(layer_index)

        if settings is not None and axis in ("x", "y"):
            settings["axis"] = axis

    def get_axis(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return "x"

        return settings["axis"]