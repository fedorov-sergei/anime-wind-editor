from dataclasses import dataclass


@dataclass
class Camera:
    zoom: float = 1.0
    offset_x: float = 0.0
    offset_y: float = 0.0

    def world_to_screen(self, x: float, y: float) -> tuple[float, float]:
        """Convert image coordinates to screen coordinates."""
        return (
            x * self.zoom + self.offset_x,
            y * self.zoom + self.offset_y,
        )

    def screen_to_world(self, x: float, y: float) -> tuple[float, float]:
        """Convert screen coordinates to image coordinates."""
        return (
            (x - self.offset_x) / self.zoom,
            (y - self.offset_y) / self.zoom,
        )

    def pan(self, dx: float, dy: float) -> None:
        """Move camera."""
        self.offset_x += dx
        self.offset_y += dy

    def zoom_at(
        self,
        factor: float,
        mouse_x: float,
        mouse_y: float,
        min_zoom: float,
        max_zoom: float,
    ) -> None:
        """Zoom while keeping the point under the cursor fixed."""

        world_x, world_y = self.screen_to_world(mouse_x, mouse_y)

        new_zoom = self.zoom * factor
        new_zoom = max(min_zoom, min(max_zoom, new_zoom))

        self.zoom = new_zoom

        self.offset_x = mouse_x - world_x * self.zoom
        self.offset_y = mouse_y - world_y * self.zoom
	
if __name__ == "__main__":
    cam = Camera()

    print(cam.screen_to_world(100, 100))

    cam.zoom_at(
        factor=2.0,
        mouse_x=100,
        mouse_y=100,
        min_zoom=0.1,
        max_zoom=8.0,
    )

    print(cam.zoom)
    print(cam.offset_x, cam.offset_y)