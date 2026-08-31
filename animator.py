import math


class Animator:

    def __init__(self):
        self.time = 0.0

        self.layers = {
            1: {
                "axis": "x",
                "amplitude": 10.0,
                "speed": 2.0,
                "rotation_amplitude": 0.0,
            },
            2: {
                "axis": "y",
                "amplitude": 6.0,
                "speed": 1.5,
                "rotation_amplitude": 0.0,
            },
            3: {
                "axis": "x",
                "amplitude": 0.0,
                "speed": 0.0,
                "rotation_amplitude": 0.0,
            },
            4: {
                "axis": "x",
                "amplitude": 0.0,
                "speed": 0.0,
                "rotation_amplitude": 0.0,
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

    def set_rotation(self, layer_index, value):
        settings = self.layers.get(layer_index)

        if settings is not None:
            settings["rotation_amplitude"] = value

    def get_rotation(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return 0.0

        return settings["rotation_amplitude"]

    def update(self, dt):
        self.time += dt

    def get_transform(self, layer_index):

        settings = self.layers.get(layer_index)

        if settings is None:
            return (0, 0, 0)

        value = math.sin(
            self.time * settings["speed"]
        ) * settings["amplitude"]

        rotation = math.sin(
            self.time * settings["speed"]
        ) * settings["rotation_amplitude"]

        if settings["axis"] == "x":
            return (value, 0, rotation)

        if settings["axis"] == "y":
            return (0, value, rotation)

        return (0, 0, rotation)

    def set_axis(self, layer_index, axis):
        settings = self.layers.get(layer_index)

        if settings is not None and axis in ("x", "y"):
            settings["axis"] = axis

    def get_axis(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return "x"

        return settings["axis"]