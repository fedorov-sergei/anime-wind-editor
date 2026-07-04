import pygame
import sys

IMAGE = "17110752_xl_optimized.webp"

pygame.init()

img = pygame.image.load(IMAGE)

iw, ih = img.get_size()

MAX_W = 1400
MAX_H = 900

scale = min(MAX_W / iw, MAX_H / ih, 1.0)

sw = int(iw * scale)
sh = int(ih * scale)

img = pygame.transform.smoothscale(img, (sw, sh))

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Anime Viewer")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    screen.blit(img, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
