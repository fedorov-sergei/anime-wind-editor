import sys

import pygame

import config
import paths
from camera import Camera


class Editor:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(config.WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 22)

        self.camera = Camera()

        self.image = pygame.image.load(str(paths.IMAGE)).convert()

        self.camera = Camera()

        self.camera.offset_x = (
            config.WINDOW_WIDTH - self.image.get_width()
        ) / 2

        self.camera.offset_y = (
            config.WINDOW_HEIGHT - self.image.get_height()
        ) / 2

        self.running = True

        self.panning = False
        self.last_mouse_pos = (0, 0)

    def handle_events(self) -> None:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # middle mouse button
                if event.button == 2:
                    self.panning = True
                    self.last_mouse_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:

                # middle mouse button release
                if event.button == 2:
                    self.panning = False

            elif event.type == pygame.MOUSEMOTION:

                if self.panning:
                    dx = event.pos[0] - self.last_mouse_pos[0]
                    dy = event.pos[1] - self.last_mouse_pos[1]

                    self.camera.pan(dx, dy)

                    self.last_mouse_pos = event.pos
            
            elif event.type == pygame.MOUSEWHEEL:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                if event.y > 0:
                    factor = config.ZOOM_STEP
                else:
                    factor = 1 / config.ZOOM_STEP

                self.camera.zoom_at(
                    factor=factor,
                    mouse_x=mouse_x,
                    mouse_y=mouse_y,
                    min_zoom=config.MIN_ZOOM,
                    max_zoom=config.MAX_ZOOM,
                )

    def draw(self) -> None:

        self.screen.fill(config.BACKGROUND_COLOR)

        x, y = self.camera.world_to_screen(0, 0)

        image = pygame.transform.smoothscale(
            self.image,
            (
                int(self.image.get_width() * self.camera.zoom),
                int(self.image.get_height() * self.camera.zoom),
            ),
        )

        self.screen.blit(image, (x, y))

        mx, my = pygame.mouse.get_pos()
        wx, wy = self.camera.screen_to_world(mx, my)

        status = (
            f"Zoom {self.camera.zoom:.2f}   "
            f"World ({int(wx)}, {int(wy)})"
        )

        text = self.font.render(
            status,
            True,
            config.STATUS_TEXT_COLOR,
        )

        pygame.draw.rect(
            self.screen,
            config.STATUS_BAR_COLOR,
            (
                0,
                config.WINDOW_HEIGHT - config.STATUS_BAR_HEIGHT,
                config.WINDOW_WIDTH,
                config.STATUS_BAR_HEIGHT,
            ),
        )

        self.screen.blit(
            text,
            (
                10,
                config.WINDOW_HEIGHT - config.STATUS_BAR_HEIGHT + 4,
            ),
        )

        pygame.display.flip()

    def run(self) -> None:

        while self.running:

            self.handle_events()

            self.draw()

            self.clock.tick(60)

        pygame.quit()
        sys.exit()


def main() -> None:
    editor = Editor()
    editor.run()


if __name__ == "__main__":
    main()