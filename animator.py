import math


class Animator:

    def __init__(self):
        self.time = 0.0

        self.layers = {
            1: {
                "amplitude": 10.0,
                "speed": 2.0,
                "angle": 0.0,
                "distortion": 0.0,
                "wave_size": 128.0,
                "wave_axis": "x",
            },
            2: {
                "amplitude": 6.0,
                "speed": 1.5,
                "angle": 0.0,
                "distortion": 0.0,
                "wave_size": 128.0,
                "wave_axis": "x",
            },
            3: {
                "amplitude": 0.0,
                "speed": 0.0,
                "angle": 0.0,
                "distortion": 0.0,
                "wave_size": 128.0,
                "wave_axis": "x",
            },
            4: {
                "amplitude": 0.0,
                "speed": 0.0,
                "angle": 0.0,
                "distortion": 0.0,
                "wave_size": 128.0,
                "wave_axis": "x",
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

    def set_distortion(self, layer_index, value):
        settings = self.layers.get(layer_index)

        if settings is not None:
            settings["distortion"] = value

    def get_distortion(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return 0.0

        return settings["distortion"]

    def set_wave_size(self, layer_index, value):
        settings = self.layers.get(layer_index)

        if settings is not None:
            settings["wave_size"] = value


    def get_wave_size(self, layer_index):
        settings = self.layers.get(layer_index)

        if settings is None:
            return 128.0

        return settings["wave_size"]

    def update(self, dt):
        self.time += dt

    def get_transform(self, layer_index):

        settings = self.layers.get(layer_index)

        if settings is None:
            return (0, 0, 0, 0, 128.0, "x")

        value = math.sin(
            self.time * settings["speed"]
        ) * settings["amplitude"]

        angle = math.radians(settings["angle"])

        x = math.cos(angle) * value
        y = math.sin(angle) * value

        distortion = settings["distortion"]

        return (
            x,
            y,
            distortion,
            settings["speed"],
            settings["wave_size"],
            settings["wave_axis"],
        )

    def set_wave_axis(self, layer_index, axis):
        settings = self.layers.get(layer_index)
        if settings is not None and axis in ("x", "y"):
            settings["wave_axis"] = axis

    def get_wave_axis(self, layer_index):
        settings = self.layers.get(layer_index)
        if settings is None:
            return "x"
        return settings["wave_axis"]