import pygame


class LayerManager:

    def __init__(self, width: int, height: int, count: int = 4):

        self.layers = []

        for _ in range(count):

            surface = pygame.Surface(
                (width, height),
                pygame.SRCALPHA,
            )

            surface.fill((0, 0, 0, 0))

            self.layers.append(surface)

    def get(self, index: int) -> pygame.Surface:
        return self.layers[index - 1]
