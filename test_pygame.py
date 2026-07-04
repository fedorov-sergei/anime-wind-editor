import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Test")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40))
    pygame.draw.rect(screen, (220, 40, 40), (150, 100, 300, 180))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
