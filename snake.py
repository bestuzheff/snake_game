import pygame

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display.fill(green)
    pygame.draw.rect(display, black, [width // 2, height // 2, segment_size, segment_size])
    pygame.display.flip()