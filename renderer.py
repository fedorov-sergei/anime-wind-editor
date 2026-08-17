from typing import List, Tuple

import pygame


class Renderer:

    def render(
        self,
        image: pygame.Surface,
        layers: List[Tuple[pygame.Surface, Tuple[int, int]]],
    ) -> pygame.Surface:

        result = image.copy()

        for layer, offset in layers:
            result.blit(
                layer,
                offset,
            )

        return result