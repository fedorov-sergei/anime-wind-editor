from typing import List, Tuple

import pygame


class Renderer:

    def render(
        self,
        image: pygame.Surface,
        layers: List[Tuple[pygame.Surface, Tuple[int, int]]],
    ) -> pygame.Surface:

        result = image.copy()

        for layer, transform in layers:
            x, y, rotation = transform

            if rotation != 0:
                original_size = layer.get_size()

                layer = pygame.transform.rotate(
                    layer,
                    rotation,
                )

                rotated_size = layer.get_size()

                x -= (rotated_size[0] - original_size[0]) / 2
                y -= (rotated_size[1] - original_size[1]) / 2

            result.blit(
                layer,
                (round(x), round(y)),
            )

        return result