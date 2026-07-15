from pathlib import Path
import pygame


def save_layers(output_dir: Path, layer_manager) -> None:

    output_dir.mkdir(parents=True, exist_ok=True)

    for index, layer in enumerate(layer_manager.layers, start=1):

        start = pygame.time.get_ticks()

        filename = output_dir / f"layer{index}.png"
        pygame.image.save(layer, str(filename))

        print(
            f"layer{index}:",
            pygame.time.get_ticks() - start,
            "ms",
        )