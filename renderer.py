from typing import Tuple

import pygame


class Renderer:

    def render(
        self,
        image: pygame.Surface,
        layer: pygame.Surface,
        offset: Tuple[int, int],
    ) -> pygame.Surface:
         
        result = image.copy()

        result.blit(
            layer,
            offset,
        )

        return result