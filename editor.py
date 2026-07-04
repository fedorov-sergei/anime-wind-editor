import pygame
import numpy as np

IMAGE = "17110752_xl_optimized.webp"

pygame.init()

# ---------- load image ----------
img = pygame.image.load(IMAGE)

iw, ih = img.get_size()

MAX_W = 1400
MAX_H = 900

scale = min(MAX_W / iw, MAX_H / ih, 1.0)

sw = int(iw * scale)
sh = int(ih * scale)

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Mask Editor")

# Теперь можно convert()
img = img.convert()

display_img = pygame.transform.smoothscale(img, (sw, sh))

clock = pygame.time.Clock()

# ---------- mask ----------
mask = pygame.Surface((sw, sh), pygame.SRCALPHA)

brush = 18
show_mask = True

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_s:
                arr = pygame.surfarray.array_alpha(mask)

                binary = np.where(arr > 0, 255, 0).astype(np.uint8)

                surf = pygame.Surface((sw, sh))
                pygame.surfarray.blit_array(
                    surf,
                    np.dstack([binary]*3)
                )

                pygame.image.save(surf, "mask_preview.png")
                print("Saved mask_preview.png")

            elif event.key == pygame.K_TAB:
                show_mask = not show_mask

        elif event.type == pygame.MOUSEWHEEL:

            brush += event.y * 2
            brush = max(2, min(150, brush))

    buttons = pygame.mouse.get_pressed()

    if buttons[0] or buttons[2]:

        x, y = pygame.mouse.get_pos()

        color = (255,0,0,120)

        if buttons[2]:
            color = (0,0,0,0)

        pygame.draw.circle(mask, color, (x,y), brush)

    screen.blit(display_img, (0,0))

    if show_mask:
        screen.blit(mask, (0,0))

    mx, my = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (255,255,255), (mx,my), brush, 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()