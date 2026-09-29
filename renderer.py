from typing import List, Tuple

import math
import pygame


class Renderer:

    def render(
        self,
        image: pygame.Surface,
        layers: List[Tuple[pygame.Surface, Tuple[float, float, float, float, float]]],
        time: float,
    ) -> pygame.Surface:

        result = image.copy()

        for layer, transform in layers:
            x, y, distortion, speed, wave_size, wave_axis = transform

            if distortion == 0:
                result.blit(
                    layer,
                    (round(x), round(y)),
                )
                continue

            width, height = layer.get_size()

            step = 4

            if wave_axis == "x":

                for left in range(0, width, step):
                    current_width = min(
                        step,
                        width - left,
                    )

                    phase = (
                        (left / width) * math.pi * wave_size
                        + time * speed
                    )

                    offset_y = math.sin(phase) * distortion

                    source_rect = pygame.Rect(
                        left,
                        0,
                        current_width,
                        height,
                    )

                    result.blit(
                        layer,
                        (
                            round(x + left),
                            round(y + offset_y),
                        ),
                        source_rect,
                    )

            else:

                for top in range(0, height, step):
                    current_height = min(
                        step,
                        height - top,
                    )

                    phase = (
                        (top / height) * math.pi * wave_size
                        + time * speed
                    )

                    offset_x = math.sin(phase) * distortion

                    source_rect = pygame.Rect(
                        0,
                        top,
                        width,
                        current_height,
                    )

                    result.blit(
                        layer,
                        (
                            round(x + offset_x),
                            round(y + top),
                        ),
                        source_rect,
                    )

        return result